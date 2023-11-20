"""Views for the patients app."""
from typing import Any
from django.core.files.storage import default_storage

from django.urls import reverse_lazy

from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Patient, Maske
from django.http import FileResponse, Http404, HttpRequest, HttpResponse
from django.conf import settings
import os

class HomeView(TemplateView):
    """Home page view."""
    template_name = 'patients/home.html'

class CreatePatientView(CreateView):
    """Create a new patient, display a success message when done."""
    template_name = 'patients/create_patient.html'
    success_url = '/patients/{patient_id}'
    model = Patient
    fields = ['patient_id', 'größe', 'gewicht', 'geschlecht', 'alter',
              'andere_informationen', 'gesichtstyp', 'prothesenträger',
              'prothese','schlaf_unterkiefer_mm', 'stl_file']

    def form_valid(self, form):
        """Set the created_by field to the current user."""
        form.instance.created_by = self.request.user

        uploaded_file = self.request.FILES.get('stl_file')

        if uploaded_file:
            file_path = f'stl/{form.instance.patient_id}.stl'
            file_path = default_storage.save(file_path, uploaded_file)

            form.instance.stl_file = file_path

        return super().form_valid(form)

class ListPatientView(ListView):
    """List all patients."""
    template_name = 'patients/list_patients.html'
    model = Patient
    context_object_name = 'patients'
    ordering = ['patient_id']

    def get_queryset(self):
        """Filter the queryset by the search query if given."""
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(patient_id__icontains=search_query)
        return queryset

class DetailPatientView(DetailView):
    """Display details of a patient."""
    template_name = 'patients/detail.html'
    model = Patient
    fields = ['patient_id', 'größe', 'gewicht', 'geschlecht',
              'alter', 'andere_informationen', 'gesichtstyp',
              'prothesenträger', 'prothese', 'abdruck_zeitpunkt',
              'abdruck_ort', 'schlaf_unterkiefer_mm', 'stl_file']
    slug_field = 'patient_id'
    slug_url_kwarg = 'patient_id'



class CreateMaskView(CreateView):
    """
    Create a new mask, forward to Patientdetailpage when done.
    Use the patient id for foreign key.
    """
    template_name = 'patients/create_mask.html'
    model = Maske
    fields = ['masken_typ', 'anschluss', 'gerätetyp',
              'druck_mbar', 'ausatemventil',
              'ausatemventil_sonstige', 'kopf_Mund_Baender',
              'kopf_Mund_Baender_sonstige', 'hartschale'
            ]

    def form_valid(self, form):
        """Set the created_by field to the current user."""
        form.instance.created_by = self.request.user
        form.instance.patient = Patient.objects.get(patient_id=self.kwargs['patient_id'])
        return super().form_valid(form)

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        return reverse_lazy('detail', kwargs={'patient_id': self.kwargs['patient_id']})

def stl_view(request):
    """
    Proof of concept for serving STL files.
    """
    stl_path = os.path.join(settings.BASE_DIR, 'patients/beispielscan.stl')
    return FileResponse(open(stl_path, 'rb'), content_type='application/octet-stream')

class STLFileView(View):
    """
    Class-based view to serve an STL file based on a given patient ID.
    """
    def get(self, request, *args, **kwargs):
        patient_id = self.kwargs.get('patient_id')
        patient = Patient.objects.get(patient_id=patient_id)
        stl_file_path = patient.stl_file.path

        if os.path.exists(stl_file_path):
            return FileResponse(open(stl_file_path, 'rb'), content_type='application/octet-stream')
        else:
            raise Http404("STL file does not exist.")