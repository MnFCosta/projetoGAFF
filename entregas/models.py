from django.db import models
from familias.models import *
from django.db.models import F, Func, IntegerField
import math


# Create your models here.
class Entrega(models.Model):
    data_entrega = models.DateField(default=None)
    familia = models.ForeignKey(Familia, verbose_name="Familia", on_delete=CASCADE)

    def __str__(self):
        return self.familia.nome
    
    class Meta:
        verbose_name = "Entrega"
        verbose_name_plural = "Entregas"

class Item(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    multiplicador = models.DecimalField(max_digits=20, decimal_places=2)
    codigo_barras = models.CharField(max_length=100)
    estoque_atual = models.DecimalField(max_digits=20, decimal_places=2)
    unidade = models.IntegerField(
        default=0,
        db_column='calculo_unidade',
        editable=False
    )
    observacao = models.TextField()

    class CalculaUnidade(Func):
        function = 'FLOOR'
        template = '%(function)s(%(expressions)s / %(multiplicador)s)'
        output_field = IntegerField()

    def save(self, *args, **kwargs):
        if self.pk is not None:
            self.unidade = self.CalculaUnidade(F('estoque_atual'), multiplicador=self.multiplicador)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Itens"


class ItemEntrega(models.Model):
    entrega = models.ForeignKey(Entrega, verbose_name="Entrega", on_delete=CASCADE)
    item = models.ForeignKey(Item, verbose_name="Item da entrega", on_delete=CASCADE)
    quantidade = models.DecimalField(max_digits=20, decimal_places=2)
    
    def __str__(self):
        return self.item.nome

    class Meta:
        verbose_name = "Item da entrega"
        verbose_name_plural = "Itens de entregas"
