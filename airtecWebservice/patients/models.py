#Since the form is used through german speaking countries, all fields are in german.
from django.db import models

class Patient(models.Model):
    """
    Allgemeine Patienteninformationen.
    Erforderlich für die Erstellung der Maske.
    Nicht direkt mit sensiblen Patientendaten verbunden, nur über patient_id.
    """
    erstellungs_datum = models.DateField(auto_now_add=True)
    patient_id = models.CharField(max_length=100, unique=True)
    größe = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    gewicht = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    geschlecht = models.CharField(max_length=10)
    alter = models.PositiveIntegerField(blank=True, null=True)
    andere_informationen = models.TextField(blank=True)
    gesichtstyp = models.CharField(choices=(('pyknisch', 'pyknisch'), ('athletisch', 'athletisch'), ('leptosom', 'leptosom')), max_length=14, default='pyknisch')

    # Todo: In Betracht ziehen, eine eigene Tabelle für Prothesenträger hinzuzufügen
    prothesenträger = models.BooleanField(default=False)
    prothese = models.CharField(max_length=100, blank=True, null=True)

    abdruck_zeitpunkt = models.DateTimeField(blank=True, null=True)
    abdruck_ort = models.CharField(choices=(('im Labor', 'im Labor'), ('in der Klinik', 'in der Klinik'), ('beim Patienten', 'beim Patienten')),
                                    max_length=14, null=True, blank=True)

class Uebergabe(models.Model):
    abholung_zeitpunkt = models.DateTimeField()
    lieferung_zeitpunkt = models.DateTimeField()
    zustaendiger_mitarbeiter = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class Lieferung(models.Model):
    lieferung_datum = models.DateField()
    lieferung_art = models.CharField(choices=((1, 'UPS'), (2, 'DHL'), (3, 'Lieferung'), (4, 'Abholung')), max_length=1)
    alternative_lieferadresse = models.CharField(max_length=100, blank=True, null=True)


class Maske(models.Model):
    """
    Digital twin of the mask.
    """
    masken_id = models.CharField(max_length=100, unique=True)
    masken_typ = models.CharField(max_length=100)
    anschluss = models.CharField(choices=((1, '15'), (2, '22')), max_length=1)
    # Gerätetyp Todo: Erstelle ein Auswahl-Feld, sobald bekannt ist, welche Gerätetypen existieren.
    gerätetyp = models.CharField(max_length=100)
    # Lieferant Todo: Erstelle entweder ein Auswahlfeld oder eine neue Tabelle für Lieferanten
    lieferant = models.CharField(max_length=100)
    druck_mbar = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    material_shore_lot = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    gaensegurgeln_select = (
        (8811, '13cm, 15'),
        (8812, '13cm, 22'),
        (8813, '15cm, 15, PV'),
        (8814, '20cm, 15, PV'),
        (8821, '20cm, 15'),
        (8754, 'Silikonadapter'),
        (1, 'sonstige'),
        )
    gaensegurgeln = models.CharField(choices=gaensegurgeln_select, max_length=1)
    ganesegurgel_sonstige = models.CharField(max_length=100, blank=True, null=True)

    tuben_select = (
        (1, 6),
        (2, 6.5),
        (3, 8)
        )
    tuben = models.CharField(choices=tuben_select, max_length=1)

    konnektoren_select = (
        (8721, '15 mm'),
        (8722, '22 mm'),
        (8723, 'Rückatemsperrung'),
        (8752, 'Doppelnippel'),
        (8702, 'Titrationsadapter'),
        (1, 'sonstige')
        )
    konnektoren = models.CharField(choices=konnektoren_select, max_length=4)
    konnektoren_sonstige = models.CharField(max_length=100, blank=True, null=True)

    ausatemventil_select = (
        (8901, 'Respironics'),
        (8902, 'Weinmann Sf'),
        (8912, 'Schalldämpfer'),
        (8922, 'F&P'),
        (8923, 'F&P Aclaim FF'),
        (1, 'sonstige')
        )
    ausatemventil = models.CharField(choices=ausatemventil_select, max_length=4)
    ausatemventil_sonstige = models.CharField(max_length=100, blank=True, null=True)

    kopf_Mund_Baender_select = (
        ('8652S', 'Full-Face Band'),
        ('8652', 'Full-Face Band'),
        ('8653', 'Full-Face Band'),
        ('8642', 'EasyFit, 5 P."M"'),
        ('8154', 'Kopfband'),
        ('8120', 'Endlosband'),
        ('8132', 'Kopfband (3P.)'),
        ('8133', 'Kopfband (3P.)'),
        ('8134', 'Kopfband (3P.)'),
        ('8554', 'F&P Aclaim FF'),
        ('2', 'Kopfhaube'),
        ('1', 'sonstige')
        )
    kopf_Mund_Baender = models.CharField(choices=kopf_Mund_Baender_select, max_length=5)
    kopf_Mund_Baender_sonstige = models.CharField(max_length=100, blank=True, null=True)

    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    hartschale = models.BooleanField(default=False)
    uebergabe = models.OneToOneField(Uebergabe, on_delete=models.CASCADE, null=True, blank=True)
    lieferung = models.OneToOneField(Lieferung, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.gaensegurgeln != 'sonstige':
            self.other_field = ''
        
        if self.konnektoren != 'sonstige':
            self.konnektoren_sonstige = ''

        if self.ausatemventil_select != 'sonstige':
            self.ausatemventil_sonstige = ''

        if self.kopf_Mund_Baender != 'sonstige':
            self.kopf_Mund_Baender_sonstige = ''

        super().save(*args, **kwargs)

class Versicherungsunternehmen(models.Model):
    """
    Prototyp für eine Datenbank mit Versicherungsunternehmensinformationen.
    Wiederkehrende Informationen für jedes Versicherungsunternehmen.
    Muss nicht jedes Mal vollständig ausgefüllt werden, wenn das Versicherungsunternehmen verwendet wird.
    Todo: Durchsuchbar machen durch Suchleiste.
    """
    versicherungsunternehmen = models.CharField(max_length=100)
    strasse = models.CharField(max_length=100)
    postleitzahl = models.CharField(max_length=100)
    stadt = models.CharField(max_length=100)
    telefon = models.CharField(max_length=100)
    fax_nummer = models.CharField(max_length=100)

class Maske(models.Model):

    # All select fields that get zipped
    gaensegurgeln_select = [
        '8811 13cm, 15',
        '8812 13cm, 22',
        '8813 15cm, 15, PV',
        '8814 20cm, 15, PV',
        '8821 20cm, 15',
        '8754 Silikonadapter',
        '1 sonstige',
        ]
    anschluss_select = [
        '1, 15',
        '2, 22'
        ]
    tuben_select = [
        '1, 6',
        '2, 6.5',
        '3, 8'
        ]
    konnektoren_select = [
        '8721, 15 mm',
        '8722, 22 mm',
        '8723, Rückatemsperrung',
        '8752, Doppelnippel',
        '8702, Titrationsadapter',
        '1, sonstige'
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

    masken_id = models.CharField(max_length=100, unique=True)
    masken_typ = models.CharField(max_length=100)
    anschluss = models.CharField(choices=zip(anschluss_select, anschluss_select), max_length=5)
    # Gerätetyp Todo: Erstelle ein Auswahl-Feld, sobald bekannt ist, welche Gerätetypen existieren.
    gerätetyp = models.CharField(max_length=100)
    # Lieferant Todo: Erstelle entweder ein Auswahlfeld oder eine neue Tabelle für Lieferanten
    lieferant = models.CharField(max_length=100)
    druck_mbar = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    material_shore_lot = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    gaensegurgeln = models.CharField(choices=zip(gaensegurgeln_select, gaensegurgeln_select), max_length=19)
    ganesegurgel_sonstige = models.CharField(max_length=100, blank=True, null=True)
    tuben = models.CharField(choices=zip(tuben_select, tuben_select), max_length=6)
    konnektoren = models.CharField(choices=zip(konnektoren_select, konnektoren_select), max_length=23)
    konnektoren_sonstige = models.CharField(max_length=100, blank=True, null=True)

    ausatemventil = models.CharField(choices=zip(ausatemventil_select,ausatemventil_select), max_length=19)
    ausatemventil_sonstige = models.CharField(max_length=100, blank=True, null=True)

    kopf_Mund_Baender = models.CharField(choices=zip(kopf_Mund_Baender_select, kopf_Mund_Baender_select), max_length=22)
    kopf_Mund_Baender_sonstige = models.CharField(max_length=100, blank=True, null=True)

    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='masken')
    hartschale = models.BooleanField(default=False)
    uebergabe = models.OneToOneField(Uebergabe, on_delete=models.CASCADE, null=True, blank=True)
    lieferung = models.OneToOneField(Lieferung, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.gaensegurgeln != 'sonstige':
            self.other_field = ''
        
        if self.konnektoren != 'sonstige':
            self.konnektoren_sonstige = ''

        if self.ausatemventil_select != 'sonstige':
            self.ausatemventil_sonstige = ''

        if self.kopf_Mund_Baender != 'sonstige':
            self.kopf_Mund_Baender_sonstige = ''

        super().save(*args, **kwargs)

class Versicherungsunternehmen(models.Model):
    """
    Prototyp für eine Datenbank mit Versicherungsunternehmensinformationen.
    Wiederkehrende Informationen für jedes Versicherungsunternehmen.
    Muss nicht jedes Mal vollständig ausgefüllt werden, wenn das Versicherungsunternehmen verwendet wird.
    Todo: Durchsuchbar machen durch Suchleiste.
    """
    versicherungsunternehmen = models.CharField(max_length=100)
    strasse = models.CharField(max_length=100)
    postleitzahl = models.CharField(max_length=100)
    stadt = models.CharField(max_length=100)
    telefon = models.CharField(max_length=100)
    fax_nummer = models.CharField(max_length=100)

class SensitivePatientData(models.Model):
    """
    Prototype for sensitive patient data database.
    """
    patient_id = models.CharField(max_length=100, unique=True, primary_key=True)
    vorname = models.CharField(max_length=100, blank=True, null=True)
    nachname = models.CharField(max_length=100, blank=True, null=True)
    strasse = models.CharField(max_length=100, blank=True, null=True)
    postleitzahl = models.CharField(max_length=100, blank=True, null=True)
    stadt = models.CharField(max_length=100, blank=True, null=True)
    geburtsdatum = models.DateField(blank=True, null=True)
    telefon_nummer = models.CharField(max_length=100, blank=True, null=True)
    handy_nummer = models.CharField(max_length=100, blank=True, null=True)

    # Versicherungsnummer
    kv_nummer = models.CharField(max_length=100, blank=True, null=True)
    # "Verordnungsdatum" -> Datum an dem die Maske verschrieben wurde
    vo_datum = models.DateField(blank=True, null=True)
    # Datum an dem die Maske geliefert wurde
    kv_datum = models.DateField(blank=True, null=True)
    # Gen. Datum?
    gen_datum = models.DateField(blank=True, null=True)

    versicherungsunternehmen = models.ForeignKey(Versicherungsunternehmen, on_delete=models.PROTECT, null=True, blank=True)
    def __str__(self):
        return f"{self.patient_id}"  # Oder eine geeignete Darstellung des Patienten-Namens

    class Meta:
        verbose_name = "Sensitive Patient Data"
        verbose_name_plural = "Sensitive Patient Data"
    # Verordner -> Arzt der die Maske verordnet hat
    verordner = models.CharField(max_length=100, blank=True, null=True)






###Fragen
# 1 Wofür steht kv_number? (Krankenversicherungsnummer? Kommt mehrmals vor)
# 2 Wofür steht VO-Datum? (Verordnungsdatum?)
# 3 Wofür steht Gen.-Datum?
# 4 Wie soll die Patient-ID umgesetzt werden?
# 5 Welche Maskentypen gibt es? (Selector field)
# 6 Welche Gerätetypen gibt es? (Selector field)