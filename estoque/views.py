from django.shortcuts import render, redirect
from entregas.models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Movimentacao
from django.db.models import Q

# Create your views here.
def estoque(request):
    itens = Item.objects.order_by("-id")

    
    search_query = request.GET.get('search')
    if search_query:
        itens = Item.objects.filter(Q(nome__icontains=search_query))
        if len(itens) == 0:
            messages.error(request, "O item em questão não foi encontrado !")
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
        'list_page': True,
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

def detailItem(request,id):
    item = Item.objects.get(id=id)

    return render(request, "estoque/pages/item_detail.html", {'item': item, "is_detail_page": True,})

def movimentacoes(request):
    movimentacoes = Movimentacao.objects.order_by("-id")

    from django.db.models import Q
    search_query = request.GET.get('search')
    if search_query:
        movimentacoes = Movimentacao.objects.filter(Q(item__nome__icontains=search_query))
        if len(movimentacoes) == 0:
            messages.error(request, "A movimentação em questão não foi encontrada !")
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
        'list_page': True,
    } 
    
    return render(request, "estoque/pages/movimentacoes.html", context)