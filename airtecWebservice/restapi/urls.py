from django.urls import path, include
from .views import PatientsViewSet, PatientDetailView, MaskeViewSet, MaskeDetailView

urlpatterns = [
    path('patients/', PatientsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('patients/<int:patient_id>/', PatientDetailView.as_view()),
    path('maske/', MaskeViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('maske/<int:id>/', MaskeDetailView.as_view()),
    path('api-auth/', include('rest_framework.urls'))
    ]
