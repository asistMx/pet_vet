from django.urls import path
from .views.subjects import CrearPropietario,ObtenerPropietario, ActualizarPropietario

urlpatterns = [
    path('expediente/crear_propietario/', CrearPropietario.as_view(), name='crear_propietario'),   
    path('expediente/propietario/<pk>', ObtenerPropietario.as_view(), name='propietario'),
    path('expediente/actualizar_propietario/<pk>', ActualizarPropietario.as_view(), name='actualizar_propietario'),
    ]
