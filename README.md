# Course Registration & Academic Management Platform

Este repositorio contiene una aplicación backend desarrollada en **Python** utilizando el framework **Django**. El proyecto implementa un sistema robusto para la administración y registro de cursos académicos, estudiantes y profesores, gestionando la consistencia y las reglas de negocio a través de relaciones complejas en el ORM de Django.

## 🚀 Características y Funcionalidades Principales

* **Operaciones CRUD Completas:** Control total para la creación, lectura, actualización y eliminación de registros de cursos y estudiantes.
* **Modelo Relacional Avanzado:** Uso eficiente de relaciones de base de datos a través del ORM de Django (relaciones *One-to-Many* para asignación de profesores y *Many-to-Many* para inscripciones de alumnos).
* **Validación de Datos en Servidor:** Implementación de lógica de negocio para evitar la duplicidad de inscripciones y validar la disponibilidad de cupos en los cursos.
* **Panel de Administración Dinámico:** Configuración personalizada del módulo `django.contrib.admin` para permitir una gestión de datos intuitiva por parte de roles administrativos.

## 🛠️ Stack Tecnológico

* **Lenguaje:** Python 3.x
* **Framework Backend:** Django 4.x / 5.x
* **Base de Datos:** PostgreSQL.
* **Lógica de Plantillas (UI):** Django Templates / Bootstrap / CSS para la interfaz.

## ⚙️ Arquitectura del Sistema y Solución de Problemas

El desarrollo se enfocó en resolver la consistencia en sistemas transaccionales escolares:

1. **Integridad Referencial:** Se diseñaron las migraciones asegurando que la eliminación de un curso o un estudiante maneje correctamente las restricciones (como el borrado lógico o en cascada `on_delete=models.CASCADE`).
2. **Optimización de Consultas (ORM):** Estructuración de consultas eficientes utilizando técnicas de filtrado nativas de Django para optimizar el rendimiento al listar estudiantes matriculados por curso.
3. **Modularidad MVT:** Separación limpia utilizando la arquitectura Modelo-Vista-Template de Django para facilitar el mantenimiento y escalabilidad del código.

## 🔧 Instalación y Ejecución Local

Para levantar este panel de gestión en tu entorno de desarrollo, sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/longaresf/course-registration-platform.git](https://github.com/longaresf/course-registration-platform.git)
   ```
2. Ingresar al directorio:
   Bash
   cd course-registration-platform

3. Configurar el entorno virtual e instalar dependencias:
   Bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate
   pip install -r requirements.txt

4. Ejecutar migraciones para estructurar la base de datos:
   Bash
   python manage.py makemigrations
   python manage.py migrate

5. Crear un superusuario para el panel administrativo:
   Bash
   python manage.py createsuperuser

6. Iniciar el servidor local:
   Bash
   python manage.py runserver

   Accede a http://127.0.0.1:8000/admin para gestionar el sistema con las credenciales del superusuario creado.

   ✒️ Autor

    Francisco Longares - Desarrollador Backend Python - longaresf

    Este proyecto fue construido para resolver las evaluaciones de lógica relacional dentro del programa de especialización Full Stack Python de Desafío Latam.
