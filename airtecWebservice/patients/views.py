"""Views for the patients app."""
import os
from typing import Any

from django.core.files.storage import default_storage
from django.db import models

from django.urls import reverse_lazy

from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView

from django.http import FileResponse, Http404
from django.conf import settings
from patients.models import Patient, Maske


class HomeView(TemplateView):
    """Home page view."""
    template_name = 'patients/home.html'

class CreatePatientView(CreateView):
    """Create a new patient, display a success message when done."""
    template_name = 'patients/create_patient.html'
    model = Patient
    fields = ['patient_id', 'groeße', 'gewicht', 'geschlecht', 'alter',
              'andere_informationen', 'gesichtstyp', 'prothesentraeger',
              'prothese','schlaf_unterkiefer_mm', 'stl_file']

    def form_valid(self, form):
        """Set the created_by field to the current user."""
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
            """Return the URL to redirect to after processing a valid form."""
            return reverse_lazy('detail', kwargs={'patient_id': self.object.patient_id})

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
    fields = ['patient_id', 'groeße', 'gewicht', 'geschlecht',
              'alter', 'andere_informationen', 'gesichtstyp',
              'prothesentraeger', 'prothese', 'abdruck_zeitpunkt',
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
    fields = ['masken_typ', 'anschluss', 'geraetetyp',
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

class STLFileView(View):
    """
    Class-based view to serve an STL file based on a given patient ID.
    """
    def get(self, request, *args, **kwargs):
        """Return the STL file for the patient with the given ID."""
        patient_id = self.kwargs.get('patient_id')
        patient = Patient.objects.get(patient_id=patient_id)
        stl_file_path = patient.stl_file.path

        if os.path.exists(stl_file_path):
            return FileResponse(open(stl_file_path, 'rb'), content_type='application/octet-stream')
        raise Http404("STL file does not exist.")
