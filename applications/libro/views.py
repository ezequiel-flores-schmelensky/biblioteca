from django.shortcuts import render
from django.views.generic import ListView
from .models import Libro


class ListLibros(ListView):
    template_name = "libro/lista.html"
    context_object_name = "lista_libros"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword","")
        return Libro.objects.listar_libros(palabra_clave)
