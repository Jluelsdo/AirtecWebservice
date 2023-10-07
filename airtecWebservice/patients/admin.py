from django.contrib import admin
from .models import Patient, Versicherungsunternehmen, SensitivePatientData

class PatientAdmin(admin.ModelAdmin):
    pass
class VersicherungsunternehmenAdmin(admin.ModelAdmin):
    pass
class SensitivePatientDataAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)
admin.site.register(Versicherungsunternehmen,VersicherungsunternehmenAdmin)
admin.site.register(SensitivePatientData, SensitivePatientDataAdmin)