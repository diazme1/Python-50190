from django.http import HttpResponse  #importamos la clase HttpResponse

from datetime import datetime

from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola Comisión 50190-Coder!!") #creamos una respuesta http al usuario

def segunda_vista(request):
    return HttpResponse('<progress value="75" max="100"></progress><br></br>Esta es mi segunda vista!!') #usamos etiquetas HTML

def dia_de_hoy(request):
    dia = datetime.now()

    textoHtml = f'Hoy es: <br></br> {dia}' #incluimos un parámetro que varía según la información asignada a la variable dia

    return HttpResponse(textoHtml)

def saludo_nombre(request, nombre):
    textoHtml = f'Hola, {nombre}!!'

    return HttpResponse(textoHtml)

def vista_template(request):
    miHtml = open(r'D:\Usuario\Documents\coder\Tutoria\Python-50190\Clase17Python\Clase17Python\templates\template1.html')

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)
    return HttpResponse(documento)