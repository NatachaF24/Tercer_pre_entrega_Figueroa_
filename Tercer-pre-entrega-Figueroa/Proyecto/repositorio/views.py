from django.shortcuts import render
from .models import *

# Create your views here.
def inicio(request):
    return render (request, "repositorio/index.html")

def complejos(request):
    contexto = {"complejos": Complejo.objects.all()}
    return render(request, "repositorio/complejos.html", contexto)

def profesores(request):
    contexto = {"profesores": Profesor.objects.all()}
    return render(request, "repositorio/profesores.html", contexto)

def profesionales(request):
    contexto = {"profesionales": Profesional.objects.all()}
    return render(request, "repositorio/profesionales.html", contexto)

def acerca(request):
    return render(request, "repositorio/acerca.html")