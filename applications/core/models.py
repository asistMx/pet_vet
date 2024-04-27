from django.db import models

class Empresa(models.Model):
    clave = models.CharField(max_length=100)
    razon_social = models.CharField(max_length=100)
    rfc = models.CharField(max_length=13)
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
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'empresa'
        verbose_name_plural = 'empresas'
        managed= True
        db_table = 'empresa'

    def __str__(self):
        return self.razon_social
    
class Sucursal(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='sucursales')
    clave = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
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
    latitud = models.DecimalField(max_digits=19, decimal_places=7, blank=True, null=True)
    longitud = models.DecimalField(max_digits=19, decimal_places=7, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'sucursal'
        verbose_name_plural = 'sucursales'
        managed= True
        db_table = 'sucursal'

    def __str__(self):
        return self.nombre