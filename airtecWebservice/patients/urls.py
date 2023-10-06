from django.urls import path, include

from .views import HomeView, CreatePatientView, ListPatientView, DetailPatientView, CreateMaskView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('patients/', ListPatientView.as_view(), name='list_patients'),
    path('patients/add', CreatePatientView.as_view(), name='create_patient'),
    path('patients/<slug:patient_id>/', DetailPatientView.as_view(), name='detail'),
    path('patients/<slug:patient_id>/masks/add', CreateMaskView.as_view(), name='create_mask'),
]