from django.shortcuts import render
from entregas.models import *
from .models import Movimentacao

# Create your views here.
def estoque(request):
    itens = Item.objects.order_by("id")
    movimentacoes = Movimentacao.objects.order_by("-id")
    tipo = movimentacoes[1].tipo
    print(tipo.model)
    
    return render(request, "estoque/pages/itens.html", context={
        "itens": itens,
        "movimentacoes": movimentacoes,
    })