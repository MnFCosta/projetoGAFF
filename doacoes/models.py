from django.db import models

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