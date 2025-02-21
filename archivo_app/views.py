from django import forms
from django.shortcuts import render
import csv
import re
from io import TextIOWrapper

# Formulario para la carga del archivo
class FileUploadForm(forms.Form):
    file = forms.FileField()

# Función para validar los datos
def validate_row(row, row_num):
    errors = []
    
    # Validar número de columnas
    if len(row) != 5:
        return [f"Error en fila {row_num}: número de columnas incorrecto"]
    
    # Validar Columna 1: Números enteros entre 3 y 10 dígitos
    if not re.fullmatch(r"\d{3,10}", row[0]):
        errors.append(f"Error en fila {row_num}, columna 1: debe ser un número de 3 a 10 dígitos")
    
    # Validar Columna 2: Correo electrónico válido
    if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", row[1]):
        errors.append(f"Error en fila {row_num}, columna 2: debe ser un correo válido")
    
    # Validar Columna 3: Solo "CC" o "TI"
    if row[2] not in ["CC", "TI"]:
        errors.append(f"Error en fila {row_num}, columna 3: debe ser 'CC' o 'TI'")
    
    # Validar Columna 4: Número entre 500000 y 1500000
    try:
        if not (500000 <= int(row[3]) <= 1500000):
            errors.append(f"Error en fila {row_num}, columna 4: debe estar entre 500000 y 1500000")
    except ValueError:
        errors.append(f"Error en fila {row_num}, columna 4: debe ser un número entero")
    
    return errors

# Vista para manejar la carga y validación del archivo
def upload_file(request):
    errors = []
    success_message = ""
    
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES["file"]
            decoded_file = TextIOWrapper(file, encoding="utf-8")
            reader = csv.reader(decoded_file)
            
            for i, row in enumerate(reader, start=1):
                errors.extend(validate_row(row, i))
            
            if not errors:
                success_message = "Archivo validado correctamente"
        else:
            errors.append("Error en la subida del archivo")
    else:
        form = FileUploadForm()
    
    return render(request, "upload.html", {"form": form, "errors": errors, "success_message": success_message})
