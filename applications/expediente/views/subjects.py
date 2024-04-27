from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from ..serializers import PropietarioSerializer
from ..models import Propietario, Mascota


class CrearPropietario(generics.CreateAPIView):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer

class ObtenerPropietario(generics.RetrieveAPIView):
    queryset = Propietario.objects.filter()
    serializer_class = PropietarioSerializer

class ActualizarPropietario(generics.UpdateAPIView):
    queryset = Propietario.objects.filter()
    serializer_class = PropietarioSerializer