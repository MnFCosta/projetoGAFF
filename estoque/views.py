from django.shortcuts import render
from entregas.models import *
from .models import Movimentacao

# Create your views here.
def estoque(request):
    itens = Item.objects.order_by("id")
    
    return render(request, "estoque/pages/itens.html", context={
        "itens": itens,
    })

def movimentacoes(request):
    movimentacoes = Movimentacao.objects.order_by("-id")
    
    return render(request, "estoque/pages/movimentacoes.html", context={
        "movimentacoes": movimentacoes,
})