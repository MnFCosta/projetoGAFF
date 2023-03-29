from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from estoque.models import Movimentacao
from .models import *
from .forms import *

# Create your views here.
def entregas(request):
    entregas = Entrega.objects.order_by("id")
    
    return render(request, "entregas/pages/entregas.html", context={
        "entregas": entregas,
    })

def cadastroEntrega(request):
    if request.method == 'POST':
        form = EntregaForm(request.POST)
        if form.is_valid():
            nova_entrega = Entrega(data_entrega=form.cleaned_data.get("data_entrega"),
                                 familia=form.cleaned_data.get("familia"),
                                                )
            nova_entrega.save()
            messages.success(request, "Entrega Criada, adicione items!")
            return redirect(f"/cadastro_itens_entrega/{nova_entrega.id}")
        else:   
            messages.error(request, "Dados inválidos!")
            return redirect("entregas:cadastro_entregas")
        
    else:
        form = EntregaForm()
    return render(request, "entregas/pages/cadastro_entregas.html", {'form': form})

def entregaDetail(request, id):
    entrega = get_object_or_404(Entrega,
        pk=id
    )
    itens = ItemEntrega.objects.filter(
        entrega=id
        ).order_by("-id")

    return render(request, 'entregas/pages/entregas_detail.html', context={
        "entrega": entrega,
        "itens": itens,
        "is_detail_page": True,
    })


def itensEntrega(request, id):
    entrega = Entrega.objects.get(id=id)
    itens = ItemEntrega.objects.filter(entrega_id=id)

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
                atualizar_valor = Item.objects.get(id=novos.id)
                if form.cleaned_data.get("quantidade") <= atualizar_valor.estoque_atual: 
                    novos_itens = ItemEntrega(entrega=entrega, item=novos, quantidade=form.cleaned_data.get("quantidade"))
                    novos_itens.save()
                    movimentacao = Movimentacao(item=novos, 
                                            data_movimento=timezone.now(),
                                            quantidade=form.cleaned_data.get("quantidade"),
                                            tipo = ContentType.objects.get_for_model(ItemEntrega),
                                            por = request.user,
                                            object_id = novos_itens.id)
                    movimentacao.save()
                    atualizar_valor.estoque_atual =  atualizar_valor.estoque_atual - form.cleaned_data.get("quantidade")
                    atualizar_valor.save()
                    messages.success(request, "Itens adicionados!")
                else:
                    qtd_solicitada = form.cleaned_data.get("quantidade")
                    qtd_estoque = atualizar_valor.estoque_atual
                    messages.error(request, f"A quantidade solicitada ({qtd_solicitada}g) é maior do que se há disponível em estoque ({qtd_estoque}g)")
            return redirect(f"/entregas/{entrega.id}")
        else:   
            messages.error(request, "Dados inválidos!")
            return redirect("entregas:entregas")
        
    else:
        form = ItensForm()
    return render(request, "entregas/pages/cadastro_itens_entrega.html", {'form': form, 'entrega': entrega})