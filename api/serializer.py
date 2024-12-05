from rest_framework import serializers
from .models import programmer
from .models import student

class programmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = programmer
        #fields = ('fullname', 'nickname', 'age', 'is_active')
        fields = '__all__'
        
class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        #fields = ('Nombre', 'Apellido', 'Sexo', 'Num_ficha', 'Formacion', 'Fecha_ingreso', 'is_active')
        fields = '__all__'