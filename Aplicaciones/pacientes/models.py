from django.db import models

# Create your models here.
class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido1 = models.CharField(max_length=30)
    apellido2 = models.CharField(max_length=30)
    fecha_nac = models.CharField(max_length=30)
    fecha_reg = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre} {self.apellido1} {self.apellido2}'

class HistorialMedico(models.Model):
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.CharField(max_length=30)
    diagnostico = models.TextField()
    tratamiento = models.TextField()

    def __str__(self):
        return f'{self.id_paciente} {self.fecha}'

class Consulta(models.Model):
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.CharField(max_length=30)
    sintomas = models.TextField()
    diagnostico = models.TextField()
    tratamiento = models.TextField()

    def __str__(self):
        return f'{self.id_paciente} {self.fecha}'

