"""Patients URLs."""
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.urls.base import reverse_lazy

from .views import HomeView, CreatePatientView, ListPatientView, DetailPatientView, CreateMaskView, stl_view

login_url = reverse_lazy('login')
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    #only for looged in user
    path('patients/', login_required(ListPatientView.as_view(), login_url=login_url), name='list_patients'),
    path('patients/add', login_required(CreatePatientView.as_view(), login_url=login_url), name='create_patient'),
    path('patients/<slug:patient_id>/', login_required(DetailPatientView.as_view(), login_url=login_url), name='detail'),
    path('patients/<slug:patient_id>/masks/add', login_required(CreateMaskView.as_view(), login_url=login_url), name='create_mask'),
    path('load', stl_view, name='stl_view'),
]
