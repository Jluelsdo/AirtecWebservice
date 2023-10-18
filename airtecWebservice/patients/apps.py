"""Patients app configuration."""
from django.apps import AppConfig

class PatientsConfig(AppConfig):
    """Configure the patients app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'patients'
