
from tkinter import commondialog
from django.db import models

# Create your models here.
class Propietario(models.Model):
    nombre = models.CharField(max_length=50, null=True, blank=True)
    apellido_materno = models.CharField(max_length=50 , null=True, blank=True)
    apellido_paterno = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    codigo_postal = models.CharField(max_length=8)
    email = models.EmailField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)
    
    class Meta:
        verbose_name = 'Propietario'
        verbose_name_plural = 'Propietarios'
        db_table = 'propietario'
 
class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    edad = models.CharField(max_length=50)
    sexo = models.CharField(max_length=50)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    microchip = models.CharField(max_length=50, null=True, blank=True)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name='mascotas')
    caracteristicas = models.TextField()
    imagen1 = models.CharField(max_length=50, null=True, blank=True)
    imagen2 = models.CharField(max_length=50, null=True, blank=True)
    imagen3 = models.CharField(max_length=50, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '{}'.format(self.nombre)
    
    class Meta:
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'
        db_table = 'mascota'


class Expediente(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    alergias = models.TextField()
    enfermedades = models.TextField()
    medicamentos = models.TextField()
    observaciones = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    codigo = models.CharField(max_length=50)
 
    def __str__(self):
        return '{}'.format(self.mascota)
    
    class Meta:
        verbose_name = 'Expediente'
        verbose_name_plural = 'Expedientes'
        db_table = 'expediente'

class Vacuna(models.Model):
    expediente = models.ForeignKey(Expediente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    proxima_fecha = models.DateField()
    imagen = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '{}'.format(self.nombre)
    
    class Meta:
        verbose_name = 'Vacuna'
        verbose_name_plural = 'Vacunas'
        db_table = 'vacuna'

class Desparasitacion(models.Model):
    expediente = models.ForeignKey(Expediente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    proxima_fecha = models.DateField()
    imagen = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '{}'.format(self.nombre)
    
    class Meta:
        verbose_name = 'Desparasitacion'
        verbose_name_plural = 'Desparasitaciones'
        db_table = 'desparasitacion'

class Cita(models.Model):
    expediente = models.ForeignKey(Expediente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '{}'.format(self.mascota)
    
    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'
        db_table = 'cita'

class Consulta(models.Model):
    expediente = models.ForeignKey(Expediente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    temperatura = models.DecimalField(max_digits=5, decimal_places=2)
    frecuencia_cardiaca = models.DecimalField(max_digits=5, decimal_places=2)
    frecuencia_respiratoria = models.DecimalField(max_digits=5, decimal_places=2)
    diagnostico = models.TextField()
    tratamiento = models.TextField()
    observaciones = models.TextField()
    """ 
    imagen1 = models.CharField(max_length=50)
    imagen2 = models.CharField(max_length=50)
    imagen3 = models.CharField(max_length=50)
    """
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '{}'.format(self.mascota)
    
    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        db_table = 'consulta'

class Cirugia(models.Model):
    expediente = models.ForeignKey(Expediente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField()
    diagnostico = models.TextField()
    tratamiento = models.TextField()
    observaciones = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '{}'.format(self.mascota)
    
    class Meta:
        verbose_name = 'Cirugia'
        verbose_name_plural = 'Cirugias'
        db_table = 'cirugia'

class Hospitalizacion(models.Model):
    expediente = models.ForeignKey(Expediente, on_delete=models.CASCADE)
    fecha = models.DateField()
    ingreso = models.DateField()
    alta = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField()
    diagnostico = models.TextField()
    tratamiento = models.TextField()
    observaciones = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '{}'.format(self.mascota)
    
    class Meta:
        verbose_name = 'Hospitalizacion'
        verbose_name_plural = 'Hospitalizaciones'
        db_table = 'hospitalizacion'

class Eutanasia(models.Model):
    expediente = models.ForeignKey(Expediente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField()
    diagnostico = models.TextField()
    observaciones = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '{}'.format(self.mascota)
    
    class Meta:
        verbose_name = 'Eutanasia'
        verbose_name_plural = 'Eutanasias'
        db_table = 'eutanasia'

class Incineracion(models.Model):
    expediente = models.ForeignKey(Expediente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField()
    observaciones = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '{}'.format(self.mascota)
    
    class Meta:
        verbose_name = 'Incineracion'
        verbose_name_plural = 'Incineraciones'
        db_table = 'incineracion'

class Receta(models.Model):
    expediente = models.ForeignKey(Expediente, on_delete=models.CASCADE)
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    fecha = models.DateField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '{}'.format(self.mascota)
    
    class Meta:
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'
        db_table = 'receta'

class RecetaImagen(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    imagen = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '{}'.format(self.imagen)
    
    class Meta:
        verbose_name = 'RecetaImagen'
        verbose_name_plural = 'RecetaImagenes'
        db_table = 'receta_imagen'

class Medicamento(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    dosis = models.CharField(max_length=50)
    frecuencia = models.CharField(max_length=50)
    duracion = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '{}'.format(self.nombre)
    
    class Meta:
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'
        db_table = 'medicamento'


class Estudio(models.Model):
    expediente = models.ForeignKey(Expediente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    resultado = models.TextField()
    imagen = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '{}'.format(self.nombre)
    
    class Meta:
        verbose_name = 'Estudio'
        verbose_name_plural = 'Estudios'
        db_table = 'estudio'

class Medico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    cedula_profesional = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
    #imagen = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)
    
    class Meta:
        verbose_name = 'Medico'
        verbose_name_plural = 'Medicos'
        db_table = 'medico'