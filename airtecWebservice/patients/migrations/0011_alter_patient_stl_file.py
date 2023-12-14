# Generated by Django 4.2.4 on 2023-12-14 11:01

from django.db import migrations, models
import patients.models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0010_alter_patient_patient_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='stl_file',
            field=models.FileField(blank=True, null=True, upload_to=patients.models.get_patient_facescan_upload_path),
        ),
    ]
