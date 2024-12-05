from rest_framework import viewsets
from .models import programmer
from .serializer import programmerSerializer
from .models import student
from .serializer import studentSerializer

# Create your views here.

class programmerViewSet(viewsets.ModelViewSet):
    queryset = programmer.objects.all()
    serializer_class = programmerSerializer
    
class studentViewSet(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = studentSerializer