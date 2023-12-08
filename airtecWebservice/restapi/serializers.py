"""
Serializers for the restapi.
"""
from rest_framework import serializers
from patients.models import Patient, Maske

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the Patient model."""
    class Meta:
        model = Patient
        fields = ['patient_id', 'größe', 'gewicht', 'geschlecht',
                  'alter', 'andere_informationen', 'gesichtstyp',
                  'prothesenträger', 'prothese', 'stl_file', 'schlaf_unterkiefer_mm']

class MaskeSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the Maske model."""
    class Meta:
        model = Maske
        fields = ['id', 'masken_typ', 'anschluss', 'gerätetyp',
                  'druck_mbar', 'ausatemventil', 'ausatemventil_sonstige',
                  'kopf_Mund_Baender', 'kopf_Mund_Baender_sonstige']
