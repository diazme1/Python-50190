from django.http import HttpResponse  #importamos la clase HttpResponse

def saludo(request):
    return HttpResponse("Hola Comisión 50190-Coder!!") #creamos una respuesta http al usuario

def segunda_vista(request):
    return HttpResponse('<progress value="75" max="100"></progress><br></br>Esta es mi segunda vista!!') #usamos etiquetas HTML