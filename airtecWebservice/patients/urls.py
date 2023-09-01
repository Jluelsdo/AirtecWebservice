from django.urls import path, include

from .views import HomeView, CreatePatientView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('patients/', CreatePatientView.as_view(), name='create_patient')
]