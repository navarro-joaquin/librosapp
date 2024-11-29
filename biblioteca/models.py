from django.db import models
from .validators import validar_anio, validar_calificacion

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    genero = models.ManyToManyField(Genero)
    publicacion = models.IntegerField(validators=[validar_anio])

    def __str__(self):
        return self.titulo

class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    texto = models.TextField()
    calificacion = models.PositiveIntegerField(validators=[validar_calificacion])

    def __str__(self):
        return f"Reseña de {self.libro.titulo}"