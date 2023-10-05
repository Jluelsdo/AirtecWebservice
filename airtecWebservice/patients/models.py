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

    def __str__(self):
        return self.patient_id

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

class SensitivePatientData(models.Model):
    """
    Prototype for sensitive patient data database.
    """
    patient_id = models.CharField(max_length=100, unique=True, primary_key=True)
    vorname = models.CharField(max_length=100)
    nachname = models.CharField(max_length=100)
    strasse = models.CharField(max_length=100)
    postleitzahl = models.CharField(max_length=100)
    stadt = models.CharField(max_length=100)
    geburtsdatum = models.DateField()
    telefon_nummer = models.CharField(max_length=100)
    handy_nummer = models.CharField(max_length=100)

    # Versicherungsnummer
    kv_nummer = models.CharField(max_length=100)
    # "Verordnungsdatum" -> Datum an dem die Maske verschrieben wurde
    vo_datum = models.DateField()
    # Datum an dem die Maske geliefert wurde
    kv_datum = models.DateField()
    # Gen. Datum?
    gen_datum = models.DateField()

    versicherungsunternehmen = models.ForeignKey(Versicherungsunternehmen, on_delete=models.PROTECT)
    # Verordner -> Arzt der die Maske verordnet hat
    verordner = models.CharField(max_length=100)






###Fragen
# 1 Wofür steht kv_number? (Krankenversicherungsnummer? Kommt mehrmals vor)
# 2 Wofür steht VO-Datum? (Verordnungsdatum?)
# 3 Wofür steht Gen.-Datum?
# 4 Wie soll die Patient-ID umgesetzt werden?
# 5 Welche Maskentypen gibt es? (Selector field)
# 6 Welche Gerätetypen gibt es? (Selector field)