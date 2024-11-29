# Catálogo de Libros - Proyecto en Django

Este proyecto es un sistema de catálogo de libros desarrollado en Django, que incluye funcionalidades como la gestión de autores, géneros, libros y reseñas. Además, se proporciona una API RESTful utilizando Django Rest Framework para interactuar con los datos de manera programática.

---

## **Comandos para Configurar y Ejecutar el Proyecto**


### 1. **Instalar las Dependencias**

```bash
pip install -r requirements.txt
```

### 2. **Realizar las Migraciones**

```bash
python manage.py migrate
```

### 2. **Cargar los datos de prueba en la base de datos (opcional)**

```bash
paython manage.py loaddata dump.json
```

### 3. **Crear un Superusuario** (opcional para acceder al administrador de Django)

```bash
python manage.py createsuperuser
```

### 4. **Ejecutar el Servidor de Desarrollo**

```bash
python manage.py runserver
```

El servidor estará disponible en `http://127.0.0.1:8000/`.

---

## **Endpoints de la API RESTful**

### **Modelos Disponibles**
1. Autores
2. Géneros
3. Libros
4. Reseñas

---

## **Archivos Importantes**

1. `requirements.txt`: Contiene las dependencias necesarias para ejecutar el proyecto.
2. `biblioteca/`: Carpeta principal donde se encuentran los modelos, vistas y configuraciones.
3. `manage.py`: Script principal para gestionar el proyecto.

---
