"""Patients URLs."""
# pylint: disable=line-too-long
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.urls.base import reverse_lazy

from patients.views import HomeView, CreatePatientView, ListPatientView, DetailPatientView, CreateMaskView, STLFileView

login_url = reverse_lazy('login')
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    #only for looged in user
    path('patienten/', login_required(ListPatientView.as_view(), login_url=login_url), name='list_patients'),
    path('patienten/hinzufuegen', login_required(CreatePatientView.as_view(), login_url=login_url), name='create_patient'),
    path('patienten/<slug:patient_id>/', login_required(DetailPatientView.as_view(), login_url=login_url), name='detail'),
    path('patienten/<slug:patient_id>/masken/hinzufuegen', login_required(CreateMaskView.as_view(), login_url=login_url), name='create_mask'),
    path('patienten/<slug:patient_id>/facestl', login_required(STLFileView.as_view(), login_url=login_url), name='stl_view'),
]
