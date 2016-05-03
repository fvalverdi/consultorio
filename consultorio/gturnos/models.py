from django.db import models
from django.utils import timezone
from datetime import datetime   

class Persona(models.Model):
	apellido = models.CharField(max_length=50)
	nombres = models.CharField(max_length=100)
	fecha_nac = models.DateField(default=datetime.now, blank=True)
	domicilio = models.CharField(max_length=200)
	telefono = models.CharField(max_length=15)
	dni = models.IntegerField()
	sexo = models.CharField(max_length=1)


class Especialidad(models.Model):
	nombre = models.CharField(max_length=100)
	# mat_especialidad = models.IntegerField()

		
class Medico(Persona):
	mat_profesional = models.IntegerField()


class Rel_Med_Esp(models.Model):
	mat_especialidad = models.IntegerField()
	medico = models.ForeignKey(Medico)
	especialidad = models.ForeignKey(Especialidad)

class Paciente(Persona):
	#persona = models.ForeignKey(Personas)
	fecha_inicio = models.DateField(default=datetime.now, blank=True)
	altura = models.IntegerField()
	peso = models.IntegerField()
	perimetro_enc = models.IntegerField()

	
class Historia_medica(models.Model):
	paciente = models.ForeignKey(Paciente)
	medico = models.ForeignKey(Medico)
	fecha_historia = models.DateTimeField(default=datetime.now, blank=True)
	diagnostico = models.CharField(max_length=500)
	tratamiento = models.CharField(max_length=500)


class Organizacion(models.Model):
	nombre = models.CharField(max_length=100)
	domicilio = models.CharField(max_length=200)
	telefono = models.CharField(max_length=15)

class Turno(models.Model):
	medico = models.ForeignKey(Medico)
	paciente = models.ForeignKey(Paciente)
	# usuario = models.ForeignKey(Usuario)
	fecha = models.DateTimeField(default=datetime.now, blank=True)
	organizacion = models.ForeignKey(Organizacion)

		
		
		