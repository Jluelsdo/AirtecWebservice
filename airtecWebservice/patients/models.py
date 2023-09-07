from django.db import models

class Patient(models.Model):
    patient_key = models.CharField(max_length=100, unique=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    gender = models.CharField(max_length=10)
    age = models.PositiveIntegerField(blank=True, null=True)
    other_information = models.TextField(blank=True)