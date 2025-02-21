# Aplicación Django para Subida y Validación de Archivos CSV

## Descripción

Esta aplicación permite subir un archivo CSV y validar su estructura conforme a las siguientes reglas:

### Reglas de Validación

- **Número de columnas**: Debe contener exactamente 5 columnas. Si hay más o menos, se generará un error.
- **Columna 1 (ID numérico)**: Debe ser un número entero de entre 3 y 10 caracteres.
- **Columna 2 (Correo electrónico)**: Debe ser una dirección de correo válida.
- **Columna 3 (Tipo de documento)**: Solo se permiten los valores `CC` o `TI`.
- **Columna 4 (Valor numérico)**: Debe estar en el rango de `500000` a `1500000`.
- **Columna 5 (Cualquier valor)**: Se permite cualquier contenido en esta columna.

## Instalación y Configuración

### Requisitos Previos

- Python 3.x
- Django instalado:  
  ```sh
  pip install django
  ```

### Pasos de Instalación

1. Clona el repositorio o descarga los archivos:
   ```sh
   git clone https://github.com/FredyAlexHoyosAriza/adresfirst.git
   cd adresfirst
   ```

2. Aplica migraciones de base de datos:
   ```sh
   python manage.py migrate
   ```

3. Inicia el servidor de desarrollo:
   ```sh
   python manage.py runserver
   ```

## Uso de la Aplicación

La aplicación solo funciona en la ruta:  
[http://127.0.0.1:8000/archivo/upload/](http://127.0.0.1:8000/archivo/upload/)

- Desde esta página puedes cargar un archivo CSV.
- Si el archivo cumple las reglas, se mostrará un mensaje de **"Archivo validado"**.
- Si hay errores, se listará la fila y la columna con el problema.

## Estructura del Proyecto

```
mi_proyecto/
│── mi_proyecto/
│   │── settings.py
│   │── urls.py
│   │── wsgi.py
│── archivo_app/
│   │── migrations/
│   │── templates/
│   │   ├── upload.html
│   │── forms.py
│   │── views.py
│   │── urls.py
│── manage.py
│── README.md
```

## Posibles Errores y Soluciones

- **Error 500 al subir un archivo**: Verifica que el archivo sea un CSV válido.
- **Error de validación de columnas**: Asegúrate de que el archivo tiene exactamente 5 columnas.
- **Errores de tipos de datos**: Verifica que los datos cumplen con las restricciones mencionadas.

## Licencia

Este proyecto es de código abierto y puedes modificarlo según tus necesidades.
