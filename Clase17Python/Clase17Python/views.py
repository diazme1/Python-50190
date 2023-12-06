from django.http import HttpResponse  #importamos la clase HttpResponse

def saludo(request):
    return HttpResponse("Hola Comisión 50190-Coder!!")