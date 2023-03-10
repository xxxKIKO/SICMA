# Generated by Django 4.1.7 on 2023-02-27 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id_paciente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido1', models.CharField(max_length=30)),
                ('apellido2', models.CharField(max_length=30)),
                ('fecha_nac', models.DateField()),
                ('fecha_reg', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HistorialMedico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('diagnostico', models.TextField()),
                ('tratamiento', models.TextField()),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('sintomas', models.TextField()),
                ('diagnostico', models.TextField()),
                ('tratamiento', models.TextField()),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.paciente')),
            ],
        ),
    ]
