# Generated by Django 4.2.4 on 2023-10-06 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_alter_patient_abdruck_ort_alter_patient_gesichtstyp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maske',
            name='anschluss',
            field=models.CharField(choices=[('1, 15', '1, 15'), ('2, 22', '2, 22')], max_length=5),
        ),
        migrations.AlterField(
            model_name='maske',
            name='ausatemventil',
            field=models.CharField(choices=[('8901, Respironics', '8901, Respironics'), ('8902, Weinmann Sf', '8902, Weinmann Sf'), ('8912, Schalldämpfer', '8912, Schalldämpfer'), ('8922, F&P', '8922, F&P'), ('8923, F&P Aclaim FF', '8923, F&P Aclaim FF'), ('1, sonstige', '1, sonstige')], max_length=19),
        ),
        migrations.AlterField(
            model_name='maske',
            name='gaensegurgeln',
            field=models.CharField(choices=[('8811 13cm, 15', '8811 13cm, 15'), ('8812 13cm, 22', '8812 13cm, 22'), ('8813 15cm, 15, PV', '8813 15cm, 15, PV'), ('8814 20cm, 15, PV', '8814 20cm, 15, PV'), ('8821 20cm, 15', '8821 20cm, 15'), ('8754 Silikonadapter', '8754 Silikonadapter'), ('1 sonstige', '1 sonstige')], max_length=19),
        ),
        migrations.AlterField(
            model_name='maske',
            name='konnektoren',
            field=models.CharField(choices=[('8721, 15 mm', '8721, 15 mm'), ('8722, 22 mm', '8722, 22 mm'), ('8723, Rückatemsperrung', '8723, Rückatemsperrung'), ('8752, Doppelnippel', '8752, Doppelnippel'), ('8702, Titrationsadapter', '8702, Titrationsadapter'), ('1, sonstige', '1, sonstige')], max_length=23),
        ),
        migrations.AlterField(
            model_name='maske',
            name='kopf_Mund_Baender',
            field=models.CharField(choices=[('8652S, Full-Face Band', '8652S, Full-Face Band'), ('8652, Full-Face Band', '8652, Full-Face Band'), ('8653, Full-Face Band', '8653, Full-Face Band'), ('8642, EasyFit, 5 P."M"', '8642, EasyFit, 5 P."M"'), ('8154, Kopfband', '8154, Kopfband'), ('8120, Endlosband', '8120, Endlosband'), ('8132, Kopfband (3P.)', '8132, Kopfband (3P.)'), ('8133, Kopfband (3P.)', '8133, Kopfband (3P.)'), ('8134, Kopfband (3P.)', '8134, Kopfband (3P.)'), ('8554, F&P Aclaim FF', '8554, F&P Aclaim FF'), ('2, Kopfhaube', '2, Kopfhaube'), ('1, sonstige', '1, sonstige')], max_length=22),
        ),
        migrations.AlterField(
            model_name='maske',
            name='tuben',
            field=models.CharField(choices=[('1, 6', '1, 6'), ('2, 6.5', '2, 6.5'), ('3, 8', '3, 8')], max_length=6),
        ),
    ]
