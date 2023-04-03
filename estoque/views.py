from django.shortcuts import render
from entregas.models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Movimentacao

# Create your views here.
def estoque(request):
    itens = Item.objects.order_by("id")
    
    return render(request, "estoque/pages/itens.html", context={
        "itens": itens,
    })

def movimentacoes(request):
    movimentacoes = Movimentacao.objects.order_by("-id")
    paginator = Paginator(movimentacoes, 21)
    page_number = request.GET.get('page')

    try:
        current_page = paginator.get_page(page_number)
    except PageNotAnInteger:
        current_page = paginator.get_page(1)
    except EmptyPage:
        current_page = paginator.get_page(paginator.num_pages)
    context = {
        'pagination': current_page,
    } 
    
    return render(request, "estoque/pages/movimentacoes.html", context)