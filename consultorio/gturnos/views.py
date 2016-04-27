from django.shortcuts import render,render_to_response,redirect
from django.views.generic.base import TemplateView
from .forms import *

def index(request):
	return render(request,'gturnos/plantilla-dash.html', {})

def organizacion_new(request):
	if request.method == "POST":
		form = OrganizacionForm(request.POST)
		if form.is_valid():
			oganizacion = form.save()
			return redirect('gturnos.views.oganizacion_detail',pk=oganizacion.pk)
	else:		
		form = OrganizacionForm()
		return render(request, 'gturnos/organizacion/new.html', {'form':form})


def organizacion_edit(request, pk):
	oganizacion = get_object_or_404(Oganizacion, pk=pk)
	if request.method == "POST":
		form = oganizacionForm(request.POST, instance=oganizacion)
		if form.is_valid():
			oganizacion = form.save()
			return redirect('gturnos.views.oganizacion_detail',pk=oganizacion.pk)
	else:		
		form = OrganizacionForm(instance=oganizacion)
		return render(request, 'gturnos/organizacion/edit.html', {'form':form})


def organizacion_detail(request, pk):
	oganizacion = get_object_or_404(Oganizacion, pk=pk)	
	return render(request, 'gturnos/organizacion/new.html', {'form':form})