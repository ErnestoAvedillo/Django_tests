from django.http import HttpResponse
from django.template import Template, Context
from trans.classes.jugador import Jugador
from django.template.loader import get_template
from django.shortcuts import render

def Home(request):
    mijugador = Jugador(
        'Juan', 
        'Perez', 
        'Calle Mayor', 
        '1', 
        '2', 
        'A', 
        'Madrid', 
        'España', 
        '28080', 
        'juan.perez@yahoo.es',
        '123456789'
        )
    #file_saludo = open('/home/ernesto/Desktop/trans/trans/templates/saludo_inicial.hml')
    #plt = Template(file_saludo.read())
    #file_saludo.close()
    #ctx = Context({'Jugador': mijugador})
    file_saludo = get_template('home.html')
    dicc_datos_jugador = mijugador.get_dictionary()
    print(dicc_datos_jugador)
    #ctx = Context(dicc_datos_jugador)
    saludo = file_saludo.render(dicc_datos_jugador)
    return render(request, 'home.html', dicc_datos_jugador)
    #return HttpResponse(saludo)

def About(request):
    return render(request, 'about.html')

def Play(request):
    return render(request, 'play.html')


