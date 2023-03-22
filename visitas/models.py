from django.db import models
from familias.models import *
from colaboradores.models import User

# Create your models here.
class Visita(models.Model):
    familia = models.ForeignKey(Familia, verbose_name="Visita para a Familia", on_delete=CASCADE)
    data = models.DateField(default=None)
    pedidos = models.TextField()
    observacao = models.TextField()

    class Meta:
        verbose_name = "Visita"
        verbose_name_plural = "Visitas"

    def __str__(self):
        data_formatada = self.data.strftime("%d-%m-%Y")
        return f"Visita a {self.familia} no dia {data_formatada}"

class VisitaParticipantes(models.Model):
    visita = models.ForeignKey(Visita, verbose_name="Visita", on_delete=CASCADE)
    participantes = models.ManyToManyField(User, verbose_name="Participantes da Visita")
    

    class Meta:
        verbose_name = "Participantes Visita"
        verbose_name_plural = "Participantes visita"