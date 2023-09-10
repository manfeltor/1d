from django.db import models

# Create your models here.

class Curso(models.Model):

    nombre = models.CharField(max_length=50)
    comision = models.IntegerField(max_length=4)

class Estudiante(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

class Profesor(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    
class Entregable(models.Model):

    nombre = models.CharField(max_length=50)
    fentrega = models.DateField()
    aprobado = models.BooleanField()

