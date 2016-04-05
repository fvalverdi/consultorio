from django.shortcuts import render,render_to_response
from django.views.generic.base import TemplateView

def post_list(request):
	return render(request,'gturnos/hola.html', {})