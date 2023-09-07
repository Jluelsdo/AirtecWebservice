from django.shortcuts import render

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .models import Patient

class HomeView(TemplateView):
    template_name = 'patients/home.html'

class CreatePatientView(CreateView):
    """Create a new patient, display a success message when done."""
    template_name = 'patients/create_patient.html'
    success_url = '/patients/'
    model = Patient
    fields = ['height', 'weight', 'gender', 'age', 'other_information']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)