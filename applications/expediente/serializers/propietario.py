from rest_framework import serializers

from applications.expediente.models import Propietario


class PropietarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propietario
        fields = ['id', 'nombre', 'apellido_materno','apellido_paterno', 'telefono', 'email', 'codigo_postal']