# Generated by Django 4.1.7 on 2023-02-28 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='fecha',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='historialmedico',
            name='fecha',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='fecha_nac',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='fecha_reg',
            field=models.CharField(max_length=30),
        ),
    ]
