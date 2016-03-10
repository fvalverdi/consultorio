from django.contrib import admin

# Register your models here.
from .models import ObraSocial,Paciente,Turno

admin.site.register(ObraSocial)
admin.site.register(Paciente)
admin.site.register(Turno)
