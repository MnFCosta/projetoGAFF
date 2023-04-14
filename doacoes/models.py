from django.db import models
from django.db.models import CASCADE
from entregas.models import Item

# Create your models here.

class Doador(models.Model):
    nome = models.CharField(max_length=200, default=None)
    celular = models.CharField(max_length=45)
    bairro = models.CharField(max_length=200)
    rua = models.CharField(max_length=200)
    numero = models.CharField(max_length=30)
    cidade = models.CharField(max_length=200)
    unidade_federativa = models.CharField(max_length=2)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Doador"
        verbose_name_plural = "Doadores"

class Doacao(models.Model):
    doador = models.ForeignKey(Doador, verbose_name="Doador", on_delete=CASCADE)
    data_doacao = models.DateField(default=None)
    

    def __str__(self):
        return self.doador.nome
    
    class Meta:
        verbose_name = "Doações"
        verbose_name_plural = "Doações"

class ItemDoacao(models.Model):
    doacao = models.ForeignKey(Doacao, verbose_name="Doação", on_delete=CASCADE)
    item = models.ForeignKey(Item, verbose_name="Item da doação", on_delete=CASCADE)
    quantidade = models.DecimalField(max_digits=20, decimal_places=0)
    
    def __str__(self):
        return self.item.nome

    class Meta:
        verbose_name = "Item da doação"
        verbose_name_plural = "Itens de doações"

