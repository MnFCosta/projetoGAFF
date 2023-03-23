from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from estoque.models import *
from .forms import *
from utils.utils import checar_repeticao
from django.contrib.contenttypes.models import ContentType

# Create your views here.
def doacoes(request):
    doacoes = Doacao.objects.order_by("id")
    
    return render(request, "doacoes/pages/doacoes.html", context={
        "doacoes": doacoes,
    })

def cadastroDoacao(request):
    if request.method == 'POST':
        form = DoacaoForm(request.POST)
        if form.is_valid():
            nova_doacao = Doacao(doador=form.cleaned_data.get("doador"),
                                 data_doacao=timezone.now(),
                                                )
            nova_doacao.save()
            messages.success(request, "Doação Criada, adicione items!")
            return redirect(f"/cadastro_itens/{nova_doacao.id}")
        else:   
            messages.error(request, "Dados inválidos!")
            return redirect("doacao:cadastro_items")
        
    else:
        form = DoacaoForm()
    return render(request, "doacoes/pages/cadastro_doacao.html", {'form': form})

def doacaoDetail(request, id):
    doacao = get_object_or_404(Doacao,
        pk=id
    )
    itens = ItemDoacao.objects.filter(
        doacao=id
        ).order_by("-id")

    return render(request, 'doacoes/pages/doacao_detail.html', context={
        "doacao": doacao,
        "itens": itens,
        "is_detail_page": True,
    })

def itensDoacao(request, id):
    doacao = Doacao.objects.get(id=id)
    itens = ItemDoacao.objects.filter(doacao_id=id)

    items_adicionados = []
    for item in itens:
        var = item.item.nome
        items_adicionados.append(var)
    if request.method == 'POST':
        form = ItensForm(request.POST)
        if form.is_valid():
            novos=form.cleaned_data.get("item") 
            print(novos) 
            print(items_adicionados)
            if (f'{novos}' in items_adicionados):
                 messages.error(request, "Os mesmos itens já foram adicionados anteriormente!")
            else:
                novos_itens = ItemDoacao(doacao=doacao, item=novos, quantidade=form.cleaned_data.get("quantidade"))
                novos_itens.save()
                movimentacao = Movimentacao(item=novos, 
                                            data_movimento=timezone.now(),
                                            quantidade=form.cleaned_data.get("quantidade"),
                                            tipo = ContentType.objects.get_for_model(ItemDoacao),
                                            por = request.user,
                                            object_id = novos_itens.id)
                movimentacao.save()
                messages.success(request, "Itens adicionados!")

            return redirect(f"/doacoes/{doacao.id}/")
        else:   
            messages.error(request, "Dados inválidos!")
            return redirect("doacao:doacao")
        
    else:
        form = ItensForm()
    return render(request, "doacoes/pages/cadastro_itens.html", {'form': form, 'doacao': doacao})