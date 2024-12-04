from rest_framework import viewsets
from .models import programmer
from .serializer import programmerSerializer

# Create your views here.

class programmerViewSet(viewsets.ModelViewSet):
    queryset = programmer.objects.all()
    serializer_class = programmerSerializer