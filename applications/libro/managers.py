from django.db import models
from django.db.models import Q

class LibroManager(models.Manager):
    
    
    def listar_libros(self, kword):
        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=('2000-01-01', '2017-01-02')
        )
        return resultado