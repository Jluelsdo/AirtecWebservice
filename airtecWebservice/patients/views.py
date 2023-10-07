from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect

from .models import Patient, Maske, Versicherungsunternehmen, SensitivePatientData

class HomeView(TemplateView):
    template_name = 'patients/home.html'

class CreatePatientView(CreateView):
    """Create a new patient, display a success message when done."""
    template_name = 'patients/create_patient.html'
    success_url = '/patients/{patient_id}'
    model = Patient
    fields = ['patient_id', 'größe', 'gewicht', 'geschlecht', 'alter',
              'andere_informationen', 'gesichtstyp', 'prothesenträger',
              'prothese', 'abdruck_zeitpunkt', 'abdruck_ort']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ListPatientView(ListView):
    """List all patients."""
    template_name = 'patients/list_patients.html'
    model = Patient
    context_object_name = 'patients'
    ordering = ['patient_id']

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(patient_id__icontains=search_query)
        return queryset

class DetailPatientView(DetailView):
    """Display details of a patient."""
    template_name = 'patients/detail.html'
    model = Patient
    fields = ['patient_id', 'größe', 'gewicht', 'geschlecht',
              'alter', 'andere_informationen', 'gesichtstyp',
              'prothesenträger', 'prothese', 'abdruck_zeitpunkt',
              'abdruck_ort']
    slug_field = 'patient_id'
    slug_url_kwarg = 'patient_id'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Versuchen, sensiblen Patientendaten basierend auf patient_id abzurufen
        try:
            sensitive_data = SensitivePatientData.objects.get(patient_id=self.object.patient_id)
            context['sensitive_data'] = sensitive_data
        except SensitivePatientData.DoesNotExist:
            context['sensitive_data'] = None

        # Falls es sensible Patientendaten gibt, versuchen Sie, das zugehörige Versicherungsunternehmen abzurufen
        if context['sensitive_data']:
            try:
                insurance_company = Versicherungsunternehmen.objects.get(pk=context['sensitive_data'].versicherungsunternehmen.pk)
                context['insurance_company'] = insurance_company
            except Versicherungsunternehmen.DoesNotExist:
                context['insurance_company'] = None

        # Hinzufügen der Liste der Versicherungsunternehmen zur Vorlage
        context['versicherungsunternehmen_list'] = Versicherungsunternehmen.objects.all()

        return context
    def post(self, request, *args, **kwargs):
        # Patientenobjekt abrufen
        patient = self.get_object()
        print(request.POST)

        # Überprüfen, ob das Formular mit dem Namen "Versicherungsunternehmen" gesendet wurde
        if 'Versicherungsunternehmen' in request.POST:
            # Versicherungsunternehmen aus dem Formular abrufen
            versicherungsunternehmen_id = request.POST['Versicherungsunternehmen']
            print(versicherungsunternehmen_id)

            try:
                # Versicherungsunternehmen anhand der ID abrufen
                versicherungsunternehmen = Versicherungsunternehmen.objects.get(pk=versicherungsunternehmen_id)
            except Versicherungsunternehmen.DoesNotExist:
                # Wenn das Versicherungsunternehmen nicht existiert, können Sie hier entsprechende Fehlerbehandlung hinzufügen.
                pass

            # Eintrag in SensitivePatientData erstellen oder aktualisieren
            sensitive_data, created = SensitivePatientData.objects.get_or_create(patient_id=patient.patient_id)

            # Setzen Sie das Versicherungsunternehmen-Feld, wenn ein gültiges Versicherungsunternehmen abgerufen wurde
            if versicherungsunternehmen:
                sensitive_data.versicherungsunternehmen = versicherungsunternehmen
            else:
                sensitive_data.versicherungsunternehmen = None  # oder den Standardwert, den Sie verwenden möchten

            sensitive_data.save()
            print(patient.patient_id)
            print(versicherungsunternehmen)
            print("HAAAAALLLOOOO")

        # Weiterleitung zur Detailansicht des Patienten, um die Änderungen anzuzeigen
        return redirect('detail', patient_id=patient.patient_id)


class CreateMaskView(CreateView):
    """Create a new mask, forward to Patientdetailpage when done. Use the patient id for foreign key."""
    template_name = 'patients/create_mask.html'
    model = Maske
    fields = ['masken_id', 'masken_typ', 'anschluss', 'gerätetyp',
              'lieferant', 'druck_mbar', 'material_shore_lot',
              'gaensegurgeln', 'ganesegurgel_sonstige', 'tuben',
              'konnektoren', 'konnektoren_sonstige', 'ausatemventil',
              'ausatemventil_sonstige', 'kopf_Mund_Baender', 'kopf_Mund_Baender_sonstige',
              'hartschale']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.patient = Patient.objects.get(patient_id=self.kwargs['patient_id'])
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse_lazy('detail', kwargs={'patient_id': self.kwargs['patient_id']})
    
class CreateInsuranceView(CreateView):
    """Create a new insurance company, display a success message when done."""
    template_name = 'insurance/create_insurance.html'
    success_url = '/' 
    model = Versicherungsunternehmen  
    fields = ['versicherungsunternehmen', 'strasse', 'postleitzahl', 'stadt', 'telefon', 'fax_nummer']

    def form_valid(self, form):
        # Hier wird das ausgewählte Versicherungsunternehmen gespeichert
        insurance_company = form.save()

        # Überprüfen , ob eine patient_id in der Sitzung gespeichert ist
        patient_id = self.request.session.get('patient_id')

        if patient_id:
            try:
                # Hole die zugehörigen sensiblen Patientendaten
                patient_data = SensitivePatientData.objects.get(patient_id=patient_id)
                # Speichern des ausgewählten Versicherungsunternehmen
                patient_data.versicherungsunternehmen = insurance_company
                patient_data.save()
            except SensitivePatientData.DoesNotExist:
                pass  # Möglicherweise gibt es keine passenden sensiblen Patientendaten

        return super().form_valid(form)