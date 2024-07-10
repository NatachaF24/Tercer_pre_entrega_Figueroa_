from django.urls import path, include
from .views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('complejos/', complejos, name="complejos"),
    path('profesores/', profesores, name="profesores"),
    path('profesionales/', profesionales, name="profesionales"),
    

    path('acerca/', acerca, name="acerca"),
    ]