from django.db import models
from django.utils import timezone

# Create your models here.
class ObraSocial(models.Model):
	"""docstring for ObraSocial"""

	nombre = models.CharField(max_length=50, null=False, blank=False)
	def __str__(self):
		#super(ObraSocial, self).__init__()
		return self.nombre
		
class Paciente(models.Model):
	"""docstring for Paciente"""
	nombres = models.CharField(max_length=50, null=False, blank=False)
	apellidos = models.CharField(max_length=50, null=False, blank=False)
	dni = models.IntegerField(null=False, blank=False)
	fechaNac = models.DateField()
	domicilio = models.CharField(max_length=100, null=True, blank=True)
	telFijo = models.CharField(max_length=10, null=True, blank=True)
	celular = models.CharField(max_length=10, null=True, blank=True)
	email = models.EmailField()
	obraSocial = models.ForeignKey('ObraSocial')

	def __str__(self):		
		return self.nombres

class Turno(models.Model):
	"""docstring for Turno"""
	paciente = models.ForeignKey('Paciente')
	observacion = models.CharField(max_length=100, null=True, blank=True)
	fechaHoraInicio = models.DateTimeField()
	fechaHoraFin = models.DateTimeField()
	concluido = models.BooleanField()


		
		
		