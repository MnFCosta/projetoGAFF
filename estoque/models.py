from django.db import models
from django.utils import timezone
from entregas.models import *
from colaboradores.models import User
from django.contrib.contenttypes.fields import ContentType, GenericForeignKey


# Create your models here.
class Movimentacao(models.Model):
    item = models.ForeignKey(Item, verbose_name="Item movido", on_delete=CASCADE)
    data_movimento = models.DateTimeField(default = timezone.now)
    quantidade = models.DecimalField(max_digits=20, decimal_places=2)
    tipo = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=None)
    por = models.ForeignKey(User, verbose_name="Técnico Movimentação", on_delete=CASCADE, default=None)
    object_id = models.PositiveIntegerField(default=None)
    content_object = GenericForeignKey('tipo', 'object_id')

    def __str__(self):
        return f"Movimentação de {self.item} em {self.data_movimento}"
    
    class Meta:
        verbose_name = "Movimentação"
        verbose_name_plural = "Movimentações"