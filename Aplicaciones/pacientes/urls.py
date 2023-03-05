from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pacientes, name='lista_pacientes'),
    path('nuevo/', views.nuevo_paciente, name='nuevo_paciente'),
    path('editar_paciente/<id_paciente>', views.editar_paciente, name='editar_paciente'),
    path('edicion_paciente/', views.edicion_paciente),
    path('eliminar_paciente/<id_paciente>', views.eliminar_paciente, name='eliminar_paciente'),
    path('reporte/', views.reporte_pacientes, name='reporte_pacientes'),
    
    ]