from cursos_app.models import Estudiante, Direccion, Curso, Profesor
from django.db import models

def crear_curso(codigo, nombre, version, rut_profesor, rut_estudiante):
    id_profesor_id = Profesor.objects.get(pk=rut_profesor)
    id_estudiante_id = Estudiante.objects.get(pk=rut_estudiante)
    nuevo_curso = Curso.objects.create(codigo=codigo, nombre=nombre, version=version, profesor_id=id_profesor_id, estudiante_id=id_estudiante_id)
    return nuevo_curso

def crear_profesor(rut, nombre, apellido, activo, creado_por):
    nuevo_profesor = Profesor.objects.create(rut=rut, nombre=nombre, apellido=apellido, activo=activo, creado_por=creado_por)
    return nuevo_profesor

def crear_estudiante(rut, nombre, apellido, fecha_nac, activo, creado_por):
    nuevo_estudiante = Estudiante.objects.create(rut=rut, nombre=nombre, apellido=apellido, fecha_nac=fecha_nac, activo=activo, creado_por=creado_por)
    return nuevo_estudiante

def crear_direccion(calle, numero, dpto, comuna, ciudad, region, rut):
    id_estudiante_id = Estudiante.objects.get(pk=rut)
    nueva_direccion = Direccion.objects.create(calle=calle, numero=numero, dpto=dpto, comuna=comuna, ciudad=ciudad, region=region, estudiante_id=id_estudiante_id)
    return nueva_direccion

def obtiene_estudiante(rut):
    estudiante = Estudiante.objects.filter(pk=rut)
    
    for e in estudiante:
        print(f"[Estudiante Nombre: {e.nombre}] => [Apellido: {e.apellido}] => [Fecha de Nacimiento: {e.fecha_nac}] => [Creado por: {e.creado_por}]")

def obtiene_profesor(rut):
    profesor = Profesor.objects.filter(pk=rut)
    
    for e in profesor:
        print(f"[Profesor Nombre: {e.nombre}] => [Apellido: {e.apellido}] => [Creado por: {e.creado_por}]")

def obtiene_curso(codigo):
    curso = Curso.objects.filter(pk=codigo).values()
    return curso

def agrega_profesor_a_curso(codigo, rut_profesor):
    id_profesor_id = Profesor.objects.get(pk=rut_profesor)
    add_profesor_curso = Curso.objects.filter(pk=codigo).update(profesor_id=id_profesor_id.rut)
    return add_profesor_curso

def agrega_cursos_a_estudiante(codigo, rut_estudiante):
    id_estudiante_id = Estudiante.objects.get(pk=rut_estudiante)
    add_estudiante_curso = Curso.objects.filter(pk=codigo).update(profesor_id=id_estudiante_id.rut)
    return add_estudiante_curso

def imprime_estudiante_cursos():
    curso = Curso.objects.all()
    
    for e in curso:
        print(f"[Curso Nombre: {e.nombre}] => [Version: {e.version}] => [Profesor: {e.profesor_id}] => [Estudiante: {e.estudiante_id.nombre} {e.estudiante_id.apellido}]")
    