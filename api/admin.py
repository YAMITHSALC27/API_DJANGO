from django.contrib import admin
from .models import programmer
from .models import student

# Register your models here.

admin.site.register(programmer)#se registra el modelo programmer para poder verlo en el panel de administracion de django
admin.site.register(student)#se registra el modelo student para poder verlo en el panel de administracion de django