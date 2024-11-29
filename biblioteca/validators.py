from django.core.exceptions import ValidationError

def validar_anio(value):
    if value > 2024 or value < 1450:
        raise ValidationError("El año debe estar entre 1450 y 2024")

def validar_calificacion(value):
    if value < 0 or value > 10:
        raise ValidationError("La calificación debe ser entre 1 y 10")