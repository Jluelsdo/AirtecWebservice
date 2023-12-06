from rest_framework import serializers
from patients.models import Patient

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields =         fields = ['patient_id', 'größe', 'gewicht', 'geschlecht', 'alter', 'andere_informationen', 'gesichtstyp', 'prothesenträger', 'prothese', 'stl_file', 'schlaf_unterkiefer_mm']