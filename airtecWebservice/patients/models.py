"""
Model file for the patients app.
"""
#Since the form is used through german speaking countries, all fields are in german.
from django.db import models
from django.core.exceptions import ValidationError

def validate_no_whitespace(value):
    if any(char.isspace() for char in value):
        raise ValidationError('This field cannot contain whitespace')

class Patient(models.Model):
    """
    Allgemeine Patienteninformationen.
    Erforderlich für die Erstellung der Maske.
    Nicht direkt mit sensiblen Patientendaten verbunden, nur über patient_id.
    """
    patient_id = models.CharField(max_length=100, unique=True, validators=[validate_no_whitespace])
    groeße = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    gewicht = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    geschlecht = models.CharField(max_length=10)
    alter = models.PositiveIntegerField(blank=True, null=True)
    andere_informationen = models.TextField(blank=True)
    gesichtstyp = models.CharField(
        choices=(('pyknisch', 'pyknisch'), ('athletisch', 'athletisch'), ('leptosom', 'leptosom')),
                max_length=14, default='pyknisch')
    prothesentraeger = models.BooleanField(default=False)
    prothese = models.CharField(max_length=100, blank=True, null=True)
    stl_file = models.FileField(upload_to='stl/', blank=True, null=True)
    schlaf_unterkiefer_mm = models.FloatField(blank=True, null=True)
    def __str__(self):
        return self.patient_id

class Maske(models.Model):
    """
    Digital twin of the mask.
    """
    # All select fields that get zipped
    anschluss_select = [
        '1, 15',
        '2, 22'
        ]
    tuben_select = [
        '1, 6',
        '2, 6.5',
        '3, 8'
        ]
    ausatemventil_select = [
        '8901, Respironics',
        '8902, Weinmann Sf',
        '8912, Schalldämpfer',
        '8922, F&P',
        '8923, F&P Aclaim FF',
        '1, sonstige'
        ]
    kopf_Mund_Baender_select = [
        '8652S, Full-Face Band',
        '8652, Full-Face Band',
        '8653, Full-Face Band',
        '8642, EasyFit, 5 P."M"',
        '8154, Kopfband',
        '8120, Endlosband',
        '8132, Kopfband (3P.)',
        '8133, Kopfband (3P.)',
        '8134, Kopfband (3P.)',
        '8554, F&P Aclaim FF',
        '2, Kopfhaube',
        '1, sonstige'
        ]

    masken_typ = models.CharField(max_length=100)
    anschluss = models.CharField(choices=zip(anschluss_select, anschluss_select), max_length=5)
    geraetetyp = models.CharField(max_length=100)
    druck_mbar = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    ausatemventil = models.CharField(
        choices=zip(ausatemventil_select,ausatemventil_select),
        max_length=19)
    ausatemventil_sonstige = models.CharField(max_length=100, blank=True, null=True)

    kopf_Mund_Baender = models.CharField(
        choices=zip(kopf_Mund_Baender_select, kopf_Mund_Baender_select),
        max_length=22)
    kopf_Mund_Baender_sonstige = models.CharField(max_length=100, blank=True, null=True)

    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='masken')
    hartschale = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.ausatemventil_select != 'sonstige':
            self.ausatemventil_sonstige = ''

        if self.kopf_Mund_Baender != 'sonstige':
            self.kopf_Mund_Baender_sonstige = ''

        super().save(*args, **kwargs)

class SensitivePatientData(models.Model):
    """
    Prototype for sensitive patient data database.
    """
    patient_id = models.CharField(max_length=100, unique=True, primary_key=True)
    geburtsdatum = models.DateField()
