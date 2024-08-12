from django.shortcuts import render
from gest_usuario.forms.formularioUsuarios import FormularioUsuarios
from django.http import HttpResponse

# Create your views here.

def usuario(request):
	form = FormularioUsuarios(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			return HttpResponse('Usuario creado')
	return render(request, 'usuario.html', {"form":form})