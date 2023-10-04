from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Patient

class HomeView(TemplateView):
    template_name = 'patients/home.html'

class CreatePatientView(CreateView):
    """Create a new patient, display a success message when done."""
    template_name = 'patients/create_patient.html'
    success_url = '/patients/'
    model = Patient
    fields = ['patient_id', 'größe', 'gewicht', 'geschlecht', 'alter',
              'andere_informationen', 'gesichtstyp', 'prothesenträger',
              'prothese', 'abdruck_zeitpunkt', 'abdruck_ort']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ListPatientView(ListView):
    """List all patients."""
    template_name = 'patients/list_patients.html'
    model = Patient
    context_object_name = 'patients'
    ordering = ['patient_id']

    def get_queryset(self):
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
              'abdruck_ort']
    slug_field = 'patient_id'
    slug_url_kwarg = 'patient_id'
