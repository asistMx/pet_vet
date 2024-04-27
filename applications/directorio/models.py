from django.db import models

# Create your models here.
""" class Directorio(models.Model):
    razonsocial = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    telefono2 = models.CharField(max_length=10)
    telefono3 = models.CharField(max_length=10)
    email = models.EmailField()
    email2 = models.EmailField()
    whataapp = models.CharField(max_length=10)
    facebook = models.URLField()
    web = models.URLField()
    descripcion = models.TextField()
    calle = models.CharField(max_length=50)
    colonia = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cp = models.CharField(max_length=5)
    pais = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='directorio', null=True, blank=True)
    imagen2 = models.ImageField(upload_to='directorio', null=True, blank=True)
    imagen3 = models.ImageField(upload_to='directorio', null=True, blank=True)
    imagen4 = models.ImageField(upload_to='directorio', null=True, blank=True)
    imagen5 = models.ImageField(upload_to='directorio', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nombre
    
    class Meta: """

