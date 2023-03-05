from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente
from .forms import Pacienteform
from django.contrib import messages

# Create your views here.
def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'lista_pacientes.html', {'pacientes': pacientes})

def nuevo_paciente(request):
    if request.method == 'POST':
        form = Pacienteform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = Pacienteform()
    return render(request, 'nuevo_paciente.html', {'form': form})

def editar_paciente(request, id_paciente):
    paciente = Paciente.objects.get(id_paciente=id_paciente)
    return render(request, 'editar_paciente.html', {'paciente': paciente})

def edicion_paciente(request):
    id_paciente = request.POST['id_paciente']
    nombre = request.POST['nombre']
    apellido1 = request.POST['apellido1']
    apellido2 = request.POST['apellido2']
    fecha_nac = request.POST['fecha_nac']
    fecha_reg = request.POST['fecha_reg']

    pac = Paciente.objects.get(id_paciente=id_paciente)
    pac.nombre = nombre
    pac.apellido1 = apellido1
    pac.apellido2 = apellido2
    pac.fecha_nac = fecha_nac
    pac.fecha_reg = fecha_reg
    pac.save()

    messages.success(request,'Paciente Actualizado')

    return redirect('lista_pacientes')

def eliminar_paciente(request, id_paciente):
    paciente = Paciente.objects.get(id_paciente=id_paciente)
    paciente.delete()
    return redirect('lista_pacientes')

def reporte_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'reporte_pacientes.html', {'pacientes': pacientes})

