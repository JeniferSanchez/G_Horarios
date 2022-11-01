from dataclasses import fields

from pyexpat import model
from rest_framework import serializers

from .models import coordinador, docente
from .models import usuario


class docenteSerializer(serializers.ModelSerializer):
    class Meta:
        model=docente
        fields='__all__'

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=usuario
        fields='__all__'

class coordinadorSerializer(serializers.ModelSerializer):

    class Meta:
        model=coordinador
        fields='__all__'
            
            