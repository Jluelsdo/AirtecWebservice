from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase
from patients.models import Patient, Maske
from .serializers import PatientSerializer
import json
import os
import django
from airtecWebservice import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airtecWebservice.settings')
django.setup()

class PatientsTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.patient = Patient.objects.create(
            patient_id=1,
            größe=180,
            gewicht=75,
            geschlecht='M',
            alter=30,
            andere_informationen='Test Information',
            gesichtstyp='Test Gesichtstyp',
            prothesenträger=True,
            prothese='Test Prothese',
            stl_file='test_file.stl',
            schlaf_unterkiefer_mm=10
        )
        self.valid_payload = {
                'patient_id': 1,
                'größe': 180,
                'gewicht': 75,
                'geschlecht': 'M',
                'alter': 30,
                'andere_informationen': 'Test Information',
                'gesichtstyp': 'Test Gesichtstyp',
                'prothesenträger': True,
                'prothese': 'Test Prothese',
                'stl_file': 'test_file.stl',
                'schlaf_unterkiefer_mm': 10
            }
        self.invalid_payload = {
            'patient_id': '',
            'größe': '',
            'gewicht': '',
            'geschlecht': '',
            'alter': '',
            'andere_informationen': '',
            'gesichtstyp': '',
            'prothesenträger': '',
            'prothese': '',
            'stl_file': '',
            'schlaf_unterkiefer_mm': ''
        }

    def test_get_all_patients(self):
        response = self.client.get(reverse('api-patient-list'))
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        for i in range(len(serializer.data)):
            serializer.data[i]['stl_file'] = 'http://testserver'+serializer.data[i]['stl_file']
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_valid_patient(self):
        response = self.client.get(
            reverse('api-patient-detail', args=[self.patient.patient_id]),
            content_type='application/json'
        )
        serializer = PatientSerializer(self.patient)
        serializer.data['stl_file'] = 'http://testserver'+serializer.data['stl_file']
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invalid_patient(self):
        response = self.client.post(
            reverse('api-patient-list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class MaskTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.patient = Patient.objects.create(
            patient_id=1,
            größe=180,
            gewicht=75,
            geschlecht='M',
            alter=30,
            andere_informationen='Test Information',
            gesichtstyp='Test Gesichtstyp',
            prothesenträger=True,
            prothese='Test Prothese',
            stl_file='test_file.stl',
            schlaf_unterkiefer_mm=10
        )
        self.maske = Maske.objects.create(
            patient_id = self.patient.patient_id,
            masken_typ='Test Masken Typ',
            anschluss='1, 15',
            gerätetyp='Test Gerätetyp',
            druck_mbar=10,
            ausatemventil='8901, Respironics',
            ausatemventil_sonstige='Test Ausatemventil Sonstige',
            kopf_Mund_Baender='8652S, Full-Face Band',
            kopf_Mund_Baender_sonstige='Test Kopf Mund Bänder Sonstige'
        )
        self.valid_payload = {
            'masken_typ': 'Test Masken Typ',
            'anschluss': '1, 15',
            'gerätetyp': 'Test Gerätetyp',
            'druck_mbar': 10,
            'ausatemventil': '8901, Respironics',
            'ausatemventil_sonstige': 'Test Ausatemventil Sonstige',
            'kopf_Mund_Baender': '8652S, Full-Face Band',
            'kopf_Mund_Baender_sonstige': 'Test Kopf Mund Bänder Sonstige'
        }
        self.invalid_payload = {
            'masken_typ': '',
            'anschluss': '',
            'gerätetyp': '',
            'druck_mbar': '',
            'ausatemventil': '',
            'ausatemventil_sonstige': '',
            'kopf_Mund_Baender': '',
            'kopf_Mund_Baender_sonstige': ''
        }

    def test_get_all_masks(self):
        response = self.client.get(reverse('api-maske-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_valid_mask(self):
        response = self.client.get(
            reverse('api-maske-detail', args=[self.maske.id]),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invalid_mask(self):
        response = self.client.post(
            reverse('api-maske-list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)