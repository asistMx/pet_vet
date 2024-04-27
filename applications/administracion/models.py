from django.db import models
from applications.core.models import Empresa, Sucursal


# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    calle = models.CharField(max_length=100)
    numero_exterior = models.CharField(max_length=100, null=True, blank=True)
    numero_interior = models.CharField(max_length=100, null=True, blank=True)
    colonia = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    cp = models.CharField(max_length=100)
    numero = models.IntegerField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'empleado'
        verbose_name_plural = 'empleados'
        managed= True
        db_table = 'empleado'

    def __str__(self):
        return self.nombre
