from django.urls import path, include


from .views import HomeView, CreatePatientView, ViewPatient, stl_view

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('patients/add', CreatePatientView.as_view(), name='create_patient'),
    path('patients/patient/view/<int:pk>', ViewPatient.as_view(), name='view_patient'),
    path('load', stl_view, name='stl_view'),

]