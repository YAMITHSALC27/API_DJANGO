from django.db import models

# Create your models here.
#aquí se crean los modelos (las tablas o colecciones)

class programmer(models.Model):
    fullname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=30)
    age = models.PositiveBigIntegerField(default=True)
    phone = models.CharField(max_length=10, null=True, default=None)
    is_active = models.BooleanField(default=True)