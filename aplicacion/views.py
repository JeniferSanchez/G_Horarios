from django.shortcuts import render
from rest_framework import generics
from .models import usuario
from .serializers import usuarioSerializer

class usuarioList(generics.ListCreateAPIView):
    queryset=usuario.objects.all()
    serializer_class=usuarioSerializer