import datetime
from django.db import models
from django.db.models import Q, Count, Avg, Sum       

class PrestamoManager(models.Manager):
    
    def libros_promedio_edades(self):
        resultado = self.filter(
            libro__id = "2"
        ).aggregate(
            promedio_edad = Avg('lector__edad'),
            suma_edad = Sum('lector__edad'),
        )
        return resultado

    def num_libros_prestados(self):
        resultado = self.values(
            'libro'
        ).annotate(
            num_prestados = Count('libro')
        )

        for r in resultado:
            print('==========')
            #Con values ya no devuelve el query set sino un valor
            print(r, r['num_prestados'])

        return resultado