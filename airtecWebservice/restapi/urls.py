from django.urls import path, include
from .views import PatientsViewSet, PatientDetailView, MaskeViewSet, MaskeDetailView

urlpatterns = [
    path('patients/', PatientsViewSet.as_view({'get': 'list', 'post': 'create'}), name='api-patient-list'),
    path('patients/<int:patient_id>/', PatientDetailView.as_view(), name='api-patient-detail'),
    path('masken/', MaskeViewSet.as_view({'get': 'list', 'post': 'create'}), name='api-maske-list'),
    path('masken/<int:id>/', MaskeDetailView.as_view(), name='api-maske-detail'),
    path('api-auth/', include('rest_framework.urls'))
    ]
