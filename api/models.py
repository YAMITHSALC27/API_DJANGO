from django.db import models

# Create your models here.
#aquí se crean los modelos (las tablas o colecciones)

class programmer(models.Model):
    fullname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=30)
    age = models.PositiveBigIntegerField(default=True)
    phone = models.CharField(max_length=10, null=True, default=None)
    is_active = models.BooleanField(default=True)

class student(models.Model):#se crean la clase estudiante
    Nombre = models.CharField(max_length=20)
    Apellido = models.CharField(max_length=20)
    Sexo = models.CharField(max_length=1)
    Num_ficha = models.IntegerField(default=None)
    
    Formacion = models.BooleanField(default=True)
    Fecha_ingreso = models.DateField(default=None)
    is_active = models.BooleanField(default=True)