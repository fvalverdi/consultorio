from django.db import models
from django.utils import timezone

# # Create your models here.
# class ObraSocial(models.Model):
# 	"""docstring for ObraSocial"""

# 	nombre = models.CharField(max_length=50, null=False, blank=False)
# 	def __str__(self):
# 		#super(ObraSocial, self).__init__()
# 		return self.nombre
		
# class Paciente(models.Model):
# 	"""docstring for Paciente"""
# 	nombres = models.CharField(max_length=50, null=False, blank=False)
# 	apellidos = models.CharField(max_length=50, null=False, blank=False)
# 	dni = models.IntegerField(null=False, blank=False)
# 	fechaNac = models.DateField()
# 	domicilio = models.CharField(max_length=100, null=True, blank=True)
# 	telFijo = models.CharField(max_length=10, null=True, blank=True)
# 	celular = models.CharField(max_length=10, null=True, blank=True)
# 	email = models.EmailField()
# 	obraSocial = models.ForeignKey('ObraSocial')

# 	def __str__(self):		
# 		return self.nombres

# class Turno(models.Model):
# 	"""docstring for Turno"""
# 	paciente = models.ForeignKey('Paciente')
# 	observacion = models.CharField(max_length=100, null=True, blank=True)
# 	fechaHoraInicio = models.DateTimeField()
# 	fechaHoraFin = models.DateTimeField()
# 	concluido = models.BooleanField()


class Persona(models.Model):
	apellido = models.CharField(max_length=50)
	nombres = models.CharField(max_length=100)
	fecha_nac = models.DateField('Fecha de nacimiento')
	domicilio = models.CharField(max_length=200)
	telefono = models.CharField(max_length=15)
	dni = models.IntegerField()
	sexo = models.CharField(max_length=1)

	def __str__(self):
            return self.nombres

class Especialidad(models.Model):
	nombre = models.CharField(max_length=100)
	mat_especialidad = models.IntegerField()

	def __str__(self):
            return self.nombre
		
class Medico(Persona):
	mat_profesional = models.IntegerField()
	#persona = models.ForeignKey (Personas)
	especialidad = models.ForeignKey(Especialidad)

	#def __str__(self):
     #       return self.mat_profesional

class Paciente(Persona):
	#persona = models.ForeignKey(Personas)
	fecha_inicio = models.DateField('Fecha de Alta Como paciente')
	altura = models.IntegerField()
	peso = models.IntegerField()
	perimetro_enc = models.IntegerField()

	def __str__(self):
            return self.nombres
	
class Historia_medica(models.Model):
	paciente = models.ForeignKey(Paciente)
	medico = models.ForeignKey(Medico)
	fecha_historia = models.DateTimeField('Fecha de Creacion')
	diagnostico = models.CharField(max_length=500)
	tratamiento = models.CharField(max_length=500)

	def __str__(self):
            return self.paciente.nombres

class Organizacion(models.Model):
	nombre = models.CharField(max_length=100)
	domicilio = models.CharField(max_length=200)
	telefono = models.CharField(max_length=15)

	def __str__(self):
            return self.nombre

class Tipo_Usuario(models.Model):
	nombre = models.CharField(max_length=20)

	def __str__(self):
            return self.nombre

class Usuario(models.Model):
	persona = models.ForeignKey(Persona)
	tipo_usuario = models.ForeignKey (Tipo_Usuario)
	organizacion = models.ForeignKey(Organizacion)

	def __str__(self):
            return self.persona.nombres
		
class Turno(models.Model):
	medico = models.ForeignKey(Medico)
	paciente = models.ForeignKey(Paciente)
	usuario = models.ForeignKey(Usuario)
	fecha = models.DateTimeField('Fecha del Turno')
	organizacion = models.ForeignKey(Organizacion)

	def __str__(self):
            return self.paciente.nombres
		
		
		