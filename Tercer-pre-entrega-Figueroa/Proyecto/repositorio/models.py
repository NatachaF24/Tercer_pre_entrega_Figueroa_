from django.db import models

# Create your models here.
class Complejo(models.Model):
    complejo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=80)
    telefono = models.IntegerField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    complejo = models.CharField(max_length=50)

class Profesional(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    profesion = models.CharField(max_length=50)
