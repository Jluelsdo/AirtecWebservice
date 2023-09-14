from django.shortcuts import render

from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView
from django.conf import settings

from .models import Patient
from django.http import FileResponse
from django.conf import settings
import os

class HomeView(TemplateView):
    template_name = 'patients/home.html'

class CreatePatientView(CreateView):
    """Create a new patient, display a success message when done."""
    template_name = 'patients/create_patient.html'
    success_url = '/patients/add'
    model = Patient
    fields = ['patient_id', 'größe', 'gewicht', 'geschlecht', 'alter', 'andere_informationen', 'gesichtstyp', 'prothesenträger', 'prothese', 'abdruck_zeitpunkt', 'abdruck_ort']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ViewPatient(DetailView):
    template_name = 'patients/view_patient.html'
    model = Patient
    slug_field = 'id'
    slug_url_kwarg = 'id'


def stl_view(request):
    """
    Proof of concept for serving STL files.
    """
    stl_path = os.path.join(settings.BASE_DIR, 'patients/beispielscan.stl')
    return FileResponse(open(stl_path, 'rb'), content_type='application/octet-stream')
