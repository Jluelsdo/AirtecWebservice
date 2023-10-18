"""This file is used to register the Patient model in the admin interface."""
from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    """Configure the Patient model for the admin interface."""
    pass

admin.site.register(Patient, PatientAdmin)
