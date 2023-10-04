from django.urls import path, include

from .views import HomeView, CreatePatientView, ListPatientView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('patients/', ListPatientView.as_view(), name='list_patients'),
    path('patients/add', CreatePatientView.as_view(), name='create_patient')
]