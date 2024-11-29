from django.contrib import admin

from .models import Autor, Genero, Libro, Resena

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'biografia')
    ordering = ('nombre',)
    search_fields = ('nombre',)

admin.site.register(Autor, AutorAdmin)

class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    ordering = ('nombre',)
    search_fields = ('nombre',)

admin.site.register(Genero, GeneroAdmin)

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'publicacion')
    ordering = ('titulo',)
    search_fields = ('titulo',)

admin.site.register(Libro, LibroAdmin)

class ResenaAdmin(admin.ModelAdmin):
    list_display = ('libro', 'calificacion')
    ordering = ('calificacion',)
    search_fields = ('libro',)

admin.site.register(Resena, ResenaAdmin)