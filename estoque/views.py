from django.shortcuts import render, redirect
from entregas.models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Movimentacao

# Create your views here.
def estoque(request):
    itens = Item.objects.order_by("-id")
    paginator = Paginator(itens, 21)
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
    
    return render(request, "estoque/pages/itens.html", context)

def cadastroItem(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            novo_item = form.save(commit=False)
            novo_item.estoque_atual = 0
            novo_item.unidade = 0
            novo_item.save()
            messages.success(request, "Novo item cadastrado")
            return redirect("estoque:estoque")
        else:   
            messages.error(request, "Dados inválidos!")
            return redirect("estoque:cadastro_item")
        
    else:
        form = ItemForm()
    return render(request, "estoque/pages/cadastro_item.html", {'form': form})

def movimentacoes(request):
    movimentacoes = Movimentacao.objects.order_by("-id")
    paginator = Paginator(movimentacoes, 22)
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