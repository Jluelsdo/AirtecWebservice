# Generated by Django 4.2.4 on 2023-11-09 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0006_remove_uebergabe_zustaendiger_mitarbeiter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='stl_file',
            field=models.FileField(blank=True, null=True, upload_to='stl/'),
        ),
    ]