from django.shortcuts import render,render_to_response,redirect,get_object_or_404
from django.views.generic.base import TemplateView
from .forms import *

def index(request):
	return render(request,'gturnos/plantilla-dash.html', {})

def organizacion_new(request):
	if request.method == "POST":
		form = OrganizacionForm(request.POST)
		if form.is_valid():
			oganizacion = form.save()
			return redirect('gturnos.views.organizacion_detail',pk=oganizacion.pk)
	else:		
		form = OrganizacionForm()
		return render(request, 'gturnos/organizacion/new.html', {'form':form})


def organizacion_edit(request, pk):
	organizacion = get_object_or_404(Organizacion, pk=pk)
	if request.method == "POST":
		form = OrganizacionForm(request.POST, instance=organizacion)
		if form.is_valid():			
			organizacion = form.save()
			return redirect('gturnos.views.organizacion_detail',pk=organizacion.pk)
	else:		
		form = OrganizacionForm(instance=organizacion)
		return render(request, 'gturnos/organizacion/edit.html', {'form':form})


def organizacion_detail(request, pk):
	org = get_object_or_404(Organizacion, pk=pk)	
	return render(request, 'gturnos/organizacion/detail.html', {'org':org})


def organizacion_all(request):
	orgTodas = Organizacion.objects.all()
	return render(request, 'gturnos/organizacion/orgList.html', {'orgTodas':orgTodas})


#Para arriba hizo walter tengo que editar 

# MEDICOS
def medico_new(request):
	if request.method == "POST":
		form = MedicoForm(request.POST)
		if form.is_valid():
			medico = form.save()			#Aca Guardo
			return redirect('gturnos.views.medico_detail',pk=medico.pk)
		else:
			return redirect('gturnos.views.medico_all')
	else:		
		form = MedicoForm()
		return render(request, 'gturnos/medico/new.html', {'form':form})

def medico_all(request):
	medTodos = Medico.objects.all()
	return render(request, 'gturnos/medico/medList.html', {'medTodos':medTodos})

def medico_edit(request, pk):
	medico = get_object_or_404(Medico, pk=pk)
	if request.method == "POST":
		form = MedicoForm(request.POST, instance=medico)
		if form.is_valid():			
			medico = form.save()
			return redirect('gturnos.views.medico_detail',pk=medico.pk)
	else:		
		form = MedicoForm(instance=medico)
		return render(request, 'gturnos/medico/edit.html', {'form':form})

def medico_detail(request, pk):
	med = get_object_or_404(Medico, pk=pk)	
	return render(request, 'gturnos/medico/detail.html', {'med':med})

#PACIENTES

def paciente_new(request):
	if request.method == "POST":
		form = PacienteForm(request.POST)
		if form.is_valid():
			paciente = form.save()			#Aca Guardo
			return redirect('gturnos.views.paciente_detail',pk=paciente.pk)
		else:
			return redirect('gturnos.views.paciente_all')
	else:		
		form = PacienteForm()
		return render(request, 'gturnos/paciente/new.html', {'form':form})

def paciente_all(request):
	pacTodas = Paciente.objects.all()
	return render(request, 'gturnos/paciente/pacList.html', {'pacTodas':pacTodas})

def paciente_edit(request, pk):
	paciente = get_object_or_404(Paciente, pk=pk)
	if request.method == "POST":
		form = PacienteForm(request.POST, instance=paciente)
		if form.is_valid():			
			paciente = form.save()
			return redirect('gturnos.views.paciente_detail',pk=paciente.pk)
	else:		
		form = PacienteForm(instance=paciente)
		return render(request, 'gturnos/paciente/edit.html', {'form':form})

def paciente_detail(request, pk):
	pac = get_object_or_404(Paciente, pk=pk)	
	return render(request, 'gturnos/paciente/detail.html', {'pac':pac})