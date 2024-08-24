from django.shortcuts import render
from gest_usuario.forms.formularioUsuarios import FormularioUsuarios, Sign_up, Login
from django.http import HttpResponse

# Create your views here.

def usuario(request):
	form = FormularioUsuarios(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			return HttpResponse('Usuario creado')
	return render(request, 'usuario.html', {"form":form})

def logIn(request):
    return render(request, 'login.html')

def signUp(request):
	form = Sign_up(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponse('Gracias por registrarte')
	else:
		form = Sign_up()
                  
	return render(request, 'signup.html', {'form': form})
    
def gracias(request):
    return render(request, 'gracias.html')

