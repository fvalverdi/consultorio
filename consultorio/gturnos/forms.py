from django import forms
from .models import *
from django.forms import  TextInput

class OrganizacionForm(forms.ModelForm):
	"""docstring for OrganizacionForm"""
	class Meta:
		model = Organizacion
		fields = ('nombre','domicilio','telefono')
		widgets = {
		'nombre': TextInput(attrs={'class':'form-control'}),
		'domicilio': TextInput(attrs={'class':'form-control'}),
		'telefono': TextInput(attrs={'class':'form-control'}),
		}
		
class PacienteForm(forms.ModelForm):
	"""docstring for PacienteForm"""
	class Meta:
		model = Paciente
		fields = ('apellido','nombres','dni','fecha_nac','altura','peso','perimetro_enc','domicilio','telefono','sexo','fecha_inicio')
		widgets = {
		'apellido': TextInput(attrs={'class':'form-control'}),
		'nombres': TextInput(attrs={'class':'form-control'}),
		# 'fecha_nac': TextInput(attrs={'class':'form-control'}),
		'domicilio': TextInput(attrs={'class':'form-control'}),
		'telefono': TextInput(attrs={'class':'form-control'}),
		'dni': TextInput(attrs={'class':'form-control'}),
		'sexo': TextInput(attrs={'class':'form-control'}),
		# 'fecha_inicio': TextInput(attrs={'class':'form-control'}),
		'altura': TextInput(attrs={'class':'form-control'}),
		'peso': TextInput(attrs={'class':'form-control'}),
		'perimetro_enc': TextInput(attrs={'class':'form-control'}),
		}
		
class MedicoForm(forms.ModelForm):
	"""docstring for OrganizacionForm"""
	class Meta:
		model = Medico
		fields = ('apellido','nombres','dni','fecha_nac','domicilio','telefono','sexo','mat_profesional')
		widgets = {
		'apellido': TextInput(attrs={'class':'form-control'}),
		'nombres': TextInput(attrs={'class':'form-control'}),
		# 'fecha_nac': TextInput(attrs={'class':'form-control'}),
		'domicilio': TextInput(attrs={'class':'form-control'}),
		'telefono': TextInput(attrs={'class':'form-control'}),
		'dni': TextInput(attrs={'class':'form-control'}),
		'sexo': TextInput(attrs={'class':'form-control'}),
		# 'fecha_inicio': TextInput(attrs={'class':'form-control'}),
		'mat_profesional': TextInput(attrs={'class':'form-control'}),
		}
# class PersonaForm(forms.ModelForm):
# 	"""docstring for PersonaForm"""
# 	class Meta:
# 		model = Persona
# 		fields = ('apellido','nombres','fecha_nac','domicilio','telefono','dni','sexo')
# 		widgets = {
# 		'apellido': TextInput(attrs={'class':'form-control'}),
# 		'nombres': TextInput(attrs={'class':'form-control'}),
# 		'fecha_nac': TextInput(attrs={'class':'form-control'}),
# 		'domicilio': TextInput(attrs={'class':'form-control'}),
# 		'telefono': TextInput(attrs={'class':'form-control'}),
# 		'dni': TextInput(attrs={'class':'form-control'}),
# 		'sexo': TextInput(attrs={'class':'form-control'}),
# 		}	