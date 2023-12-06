from django.http import HttpResponse  #importamos la clase HttpResponse

from datetime import datetime

def saludo(request):
    return HttpResponse("Hola Comisión 50190-Coder!!") #creamos una respuesta http al usuario

def segunda_vista(request):
    return HttpResponse('<progress value="75" max="100"></progress><br></br>Esta es mi segunda vista!!') #usamos etiquetas HTML

def dia_de_hoy(request):
    dia = datetime.now()

    textoHtml = f'Hoy es: <br></br> {dia}' #incluimos un parámetro que varía según la información asignada a la variable dia

    return HttpResponse(textoHtml)