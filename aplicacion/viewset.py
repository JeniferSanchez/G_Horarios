from rest_framework import viewsets

from . import models
from . import serializers

class docenteViewset(viewsets.ModelViewSet):
    queryset=models.docente.objects.all()
    serializer_class=serializers.docenteSerializer

class usuarioViewset(viewsets.ModelViewSet):
    queryset=models.usuario.objects.all()
    serializer_class=serializers.usuarioSerializer

class coordinadorViewset(viewsets.ModelViewSet):
    queryset=models.coordinador.objects.all()
    serializer_class=serializers.coordinadorSerializer