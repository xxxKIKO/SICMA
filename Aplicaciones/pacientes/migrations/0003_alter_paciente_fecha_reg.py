# Generated by Django 4.1.7 on 2023-02-28 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0002_alter_consulta_fecha_alter_historialmedico_fecha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='fecha_reg',
            field=models.DateField(),
        ),
    ]
