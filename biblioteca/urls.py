from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AutorViewSet, GeneroViewSet, LibroViewSet, ResenaViewSet, libros_count, libros_por_genero

router = DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'generos', GeneroViewSet)
router.register(r'libros', LibroViewSet)
router.register(r'resenas', ResenaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('libros/count', libros_count),
    path('libros/genero/<int:genero_id>/', libros_por_genero),
]