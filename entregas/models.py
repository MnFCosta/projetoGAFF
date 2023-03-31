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

class Item(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    unidade = models.CharField(max_length=45)
    multiplicador = models.DecimalField(max_digits=20, decimal_places=2)
    codigo_barras = models.CharField(max_length=100)
    estoque_atual = models.DecimalField(max_digits=20, decimal_places=2)
    observacao = models.TextField()

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
