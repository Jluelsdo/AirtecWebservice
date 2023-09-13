from django.urls import path, include

from .views import HomeView, CreatePatientView, ViewPatient

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('patients/add', CreatePatientView.as_view(), name='create_patient'),
    path('patients/patient/view/<int:pk>', ViewPatient.as_view(), name='view_patient'),
]