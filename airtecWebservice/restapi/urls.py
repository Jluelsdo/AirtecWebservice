"""airtecWebservice restapi URL Configuration"""
from django.urls import path, include
from restapi.views import PatientsViewSet, PatientDetailView, MaskeViewSet, MaskeDetailView

urlpatterns = [
    path('patienten/', PatientsViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='api-patient-list'),
    path('patienten/<int:patient_id>/', PatientDetailView.as_view(), name='api-patient-detail'),
    path('masken/', MaskeViewSet.as_view({'get': 'list', 'post': 'create'}), name='api-maske-list'),
    path('masken/<int:object_id>/', MaskeDetailView.as_view(), name='api-maske-detail'),
    path('api-auth/', include('rest_framework.urls'))
    ]
