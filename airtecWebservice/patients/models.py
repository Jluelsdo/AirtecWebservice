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
    gesichtstyp = models.CharField(choices=((1, 'pyknisch'), (2, 'athletisch'), (3, 'leptosom')), max_length=1)

    # Todo: In Betracht ziehen, eine eigene Tabelle für Prothesenträger hinzuzufügen
    prothesenträger = models.BooleanField(default=False)
    prothese = models.CharField(max_length=100, blank=True, null=True)

    abdruck_zeitpunkt = models.DateTimeField(blank=True, null=True)
    abdruck_ort = models.CharField(selection=((1, 'im Labor'), (2, 'in der Klinik'), (3, 'beim Patienten')), max_length=1)

class Uebergabe(models.Model):
    abholung_zeitpunkt = models.DateTimeField()
    lieferung_zeitpunkt = models.DateTimeField()
    zustaendiger_mitarbeiter = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class Lieferung(models.Model):
    lieferung_datum = models.DateField()
    lieferung_art = models.CharField(selection=((1, 'UPS'), (2, 'DHL'), (3, 'Lieferung'), (4, 'Abholung')), max_length=1)
    alternative_lieferadresse = models.CharField(max_length=100, blank=True, null=True)


class Maske(models.Model):
    """
    Digital twin of the mask.
    """
    masken_typ = models.CharField(max_length=100)
    anschluss = models.CharField(choices=((1, '15'), (2, '22')), max_length=1)
    # Gerätetyp Todo: Erstelle ein Auswahl-Feld, sobald bekannt ist, welche Gerätetypen existieren.
    gerätetyp = models.CharField(max_length=100)
    # Lieferant Todo: Erstelle entweder ein Auswahlfeld oder eine neue Tabelle für Lieferanten
    lieferant = models.CharField(max_length=100)
    druck_mbar = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    material_shore_lot = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    gaensegurgeln_select = ((1, ))

    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    hartschale = models.BooleanField(default=False)
    uebergabe = models.OneToOneField(Uebergabe, on_delete=models.CASCADE, null=True, blank=True)
    lieferung = models.OneToOneField(Lieferung, on_delete=models.CASCADE, null=True, blank=True)

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