# Farmacia API REST con Flask

Este proyecto es una API RESTful para gestionar una base de datos de una farmacia según las instrucciones del enunciado del examen. La API permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre diversas tablas en una base de datos PostgreSQL utilizando Flask y psycopg2.

## Autor

- Gerard Antony Caramazza Vilá (45983867J)
- alu0101229775@ull.edu.es
- Examen práctico de ADBD del 09/07/2024

## Requisitos

- Python 3.x
- PostgreSQL
- pip (gestor de paquetes de Python)

## Información Ejercicio 5
Se deben realizar estos pasos:
- Crear la base de datos llamada `farmacia` con el script `farmacia.sql`.
- Actualizar las credenciales de la base de datos en `database.py`.

```python
def get_db_connection():
    connection = psycopg2.connect(
        host="localhost",
        database="farmacia",
        user="alu0101229775",  # Se debe indicar el usuario para el acceso
        password="password"    # Se debe indicar la contraseña del usuario
    )
    return connection
```
