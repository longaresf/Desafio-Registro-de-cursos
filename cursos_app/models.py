from django.db import models

# Create your models here.

class Estudiante(models.Model):
    rut = models.CharField(max_length=9, primary_key=True, null=False)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    fecha_nac = models.DateField(null=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50, null=False)

class Direccion(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    calle = models.CharField(max_length=50, null=False)
    numero = models.CharField(max_length=10, null=False)
    dpto = models.CharField(max_length=10, null=True)
    comuna = models.CharField(max_length=50, null=False)
    ciudad = models.CharField(max_length=50, null=False)
    region = models.CharField(max_length=50, null=False)
    estudiante_id = models.OneToOneField('Estudiante', blank=False, null=False, on_delete=models.CASCADE, max_length=9, unique=True)
    
class Curso(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True, null=False, unique=True)
    nombre = models.CharField(max_length=50, null=False)
    version = models.SmallIntegerField(null=False)
    profesor_id = models.CharField(max_length=9, unique=True)
    profesores = models.ManyToManyField('Profesor', related_name="profesores")
    estudiante_id = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    
class Profesor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True, null=False)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50, null=False)
