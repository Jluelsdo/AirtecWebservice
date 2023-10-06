# Generated by Django 4.2.4 on 2023-10-06 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_alter_maske_anschluss_alter_maske_ausatemventil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maske',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='masken', to='patients.patient'),
        ),
    ]
