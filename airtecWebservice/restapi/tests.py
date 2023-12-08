"""
Test module for the restapi app.

This module contains test cases for the restapi app in the AirtecWebservice project.
It includes tests for the PatientsTest and MaskTest classes, which test the functionality
of the API endpoints related to patients and masks, respectively.
"""
#pylint: disable=missing-function-docstring, imported-auth-user
import os
import json

import django
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase
from patients.models import Patient, Maske
from restapi.serializers import PatientSerializer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airtecWebservice.settings')
django.setup()

class PatientsTest(APITestCase):
    """
    Test case for the Patients API endpoints.
    """
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.patient = Patient.objects.create(
            patient_id=1,
            groeße=180,
            gewicht=75,
            geschlecht='M',
            alter=30,
            andere_informationen='Test Information',
            gesichtstyp='Test Gesichtstyp',
            prothesentraeger=True,
            prothese='Test Prothese',
            stl_file='test_file.stl',
            schlaf_unterkiefer_mm=10
        )
        self.valid_payload = {
                'patient_id': 1,
                'groeße': 180,
                'gewicht': 75,
                'geschlecht': 'M',
                'alter': 30,
                'andere_informationen': 'Test Information',
                'gesichtstyp': 'Test Gesichtstyp',
                'prothesentraeger': True,
                'prothese': 'Test Prothese',
                'stl_file': 'test_file.stl',
                'schlaf_unterkiefer_mm': 10
            }
        self.invalid_payload = {
            'patient_id': '',
            'groeße': '',
            'gewicht': '',
            'geschlecht': '',
            'alter': '',
            'andere_informationen': '',
            'gesichtstyp': '',
            'prothesentraeger': '',
            'prothese': '',
            'stl_file': '',
            'schlaf_unterkiefer_mm': ''
        }

    def test_get_all_patients(self):
        response = self.client.get(reverse('api-patient-list'))
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        for data in serializer.data:
            data['stl_file'] = 'http://testserver'+data['stl_file']
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
    """
    Test case for the Mask model and API endpoints.
    """
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.patient = Patient.objects.create(
            patient_id=1,
            groeße=180,
            gewicht=75,
            geschlecht='M',
            alter=30,
            andere_informationen='Test Information',
            gesichtstyp='Test Gesichtstyp',
            prothesentraeger=True,
            prothese='Test Prothese',
            stl_file='test_file.stl',
            schlaf_unterkiefer_mm=10
        )
        self.maske = Maske.objects.create(
            patient_id = self.patient.patient_id,
            masken_typ='Test Masken Typ',
            anschluss='1, 15',
            geraetetyp='Test Gerätetyp',
            druck_mbar=10,
            ausatemventil='8901, Respironics',
            ausatemventil_sonstige='Test Ausatemventil Sonstige',
            kopf_Mund_Baender='8652S, Full-Face Band',
            kopf_Mund_Baender_sonstige='Test Kopf Mund Bänder Sonstige'
        )
        self.valid_payload = {
            'masken_typ': 'Test Masken Typ',
            'anschluss': '1, 15',
            'geraetetyp': 'Test Gerätetyp',
            'druck_mbar': 10,
            'ausatemventil': '8901, Respironics',
            'ausatemventil_sonstige': 'Test Ausatemventil Sonstige',
            'kopf_Mund_Baender': '8652S, Full-Face Band',
            'kopf_Mund_Baender_sonstige': 'Test Kopf Mund Bänder Sonstige'
        }
        self.invalid_payload = {
            'masken_typ': '',
            'anschluss': '',
            'geraetetyp': '',
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
