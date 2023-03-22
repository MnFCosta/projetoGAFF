from django.db import models
from familias.models import *

# Create your models here.
class Entrega(models.Model):
    data_entrega = models.DateField(default=None)
    familia = models.ForeignKey(Familia, verbose_name="Familia", on_delete=CASCADE)

    def __str__(self):
        return self.familia.nome
    
    class Meta:
        verbose_name = "Entrega"
        verbose_name_plural = "Entregas"