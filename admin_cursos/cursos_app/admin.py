from django.contrib import admin
from cursos_app.models import Estudiante, Direccion, Curso, Profesor

# Register your models here.

admin.site.register(Estudiante)
admin.site.register(Direccion)
admin.site.register(Curso)
admin.site.register(Profesor)