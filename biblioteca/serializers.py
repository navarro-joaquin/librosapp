from rest_framework import serializers
from .models import Autor, Genero, Libro, Resena

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'

class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = '__all__'
