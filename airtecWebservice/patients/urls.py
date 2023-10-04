from django.urls import path, include

from .views import HomeView, CreatePatientView, DetailPatientView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('patients/', CreatePatientView.as_view(), name='create_patient'),
    path('patients/<slug:patient_id>/', DetailPatientView.as_view(), name='detail'),
]