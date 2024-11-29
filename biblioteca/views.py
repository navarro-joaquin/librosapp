from django.http import JsonResponse
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from .models import Autor, Genero, Libro, Resena
from .serializers import AutorSerializer, GeneroSerializer, LibroSerializer, ResenaSerializer
from django.shortcuts import render

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class ResenaViewSet(viewsets.ModelViewSet):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer

class ResenaCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer

@api_view(['GET'])
def libros_count(request):
    try:
        cantidad = Libro.objects.count()
        return JsonResponse({
            "cantidad": cantidad,
        },
        safe=False,
        status=200
        )
    except Exception as e:
        return JsonResponse({
            "error": str(e)
        },
        safe=False,
        status=400
        )

@api_view(['GET'])
def libros_por_genero(request, genero_id):
    try:
        libros = Libro.objects.filter(genero__id=genero_id)
        if libros.exists():
            data = {
                "libros": [
                    {
                        "id": libro.id,
                        "titulo": libro.titulo,
                    }
                    for libro in libros
                ]
            }
        return JsonResponse(data,
        safe=False,
        status=200
        )
    except Exception as e:
        return JsonResponse({
            "error": str(e)
        },
        safe=False,
        status=400
        )