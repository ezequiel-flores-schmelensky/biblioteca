from django.db import models

class AutorManager(models.Manager):
    """ managers para el modelo autor """

    def buscar_autor(self, kword):
        resultado = self.filter(nombre__icontains=kword)
        return resultado