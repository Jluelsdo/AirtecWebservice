from django.urls import path, include
from .views import PatientsViewSet, PatientDetailView

urlpatterns = [
    path('patients/', PatientsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('patients/<int:patient_id>/', PatientDetailView.as_view()),
    path('api-auth/', include('rest_framework.urls'))
    ]
