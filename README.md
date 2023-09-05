# Microservicio REST API con Python y FastAPI

Este repositorio contiene el código fuente de un microservicio REST API desarrollado como parte de una prueba técnica para Reputación Digital. El microservicio se ha construido utilizando Python, el framework FastAPI y SQLite como base de datos.

## Descripción del Proyecto

El objetivo de este proyecto es crear un microservicio que ofrezca una API REST para gestionar entidades. El microservicio proporciona las siguientes funcionalidades:

- Recuperar una entidad por su ID.
- Crear una entidad con un campo de destino especificado y convertir el valor de ese campo a mayúsculas antes de insertarlo en la base de datos.

## Configuración

Antes de ejecutar el proyecto, asegúrate de configurar adecuadamente tu entorno de desarrollo y las dependencias necesarias. Puedes seguir estos pasos:

1. Clona este repositorio a tu máquina local utilizando el comando `git clone`.

2. Crea un entorno virtual: `python -m venv venv`

3. Activa el entorno virtual: 
    - `source venv/bin/activate` __En Linux/macOS__ 
    - `venv\Scripts\activate` __En Windows (cmd)__

4. Instala las dependencias: `pip install -r requirements.txt`

## Ejecución

Para ejecutar el microservicio, utiliza el siguiente comando:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
- El microservicio estará disponible en http://localhost:8000.

## Uso de la API

- __POST__ /input/{my_target_field}: Crea una entidad con un campo de destino especificado y lo convierte a mayúsculas.
 - __GET__ /get_data/{id}: Obtiene una entidad por su ID.
