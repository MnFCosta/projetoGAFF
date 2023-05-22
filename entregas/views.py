
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from estoque.models import Movimentacao
from django.http import JsonResponse
from django.db.models import Q
from .models import *
from .forms import *

# Create your views here.
def entregas(request):
    entregas = Entrega.objects.order_by("-id")
    
    search_query = request.GET.get('search')
    if search_query:
        entregas = Entrega.objects.filter(Q(familia__nome__icontains=search_query))
        if len(entregas) == 0:
            messages.error(request, "A entrega em questão não foi encontrada !")
            entregas = Entrega.objects.order_by("-id")
    
    paginator = Paginator(entregas, 21)
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
    
    return render(request, "entregas/pages/entregas.html", context)


def cadastroEntrega(request, id):
    familia = Familia.objects.get(id=id)
    if request.method == 'POST':
        form = EntregaForm(request.POST)
        if form.is_valid():
            nova_entrega = Entrega(data_entrega=form.cleaned_data.get("data_entrega"),
                                 familia=familia,
                                                )
            nova_entrega.save()
            messages.success(request, "Entrega Criada, adicione items!")
            return redirect(f"/cadastro_itens_entrega/{nova_entrega.id}") 
        else:   
            messages.error(request, "Dados inválidos!")
            return redirect("entregas:entregas")
        
    else:
        form = EntregaForm()
    return render(request, "entregas/pages/cadastro_entregas.html", {'form': form, 'familia': familia})

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
            if (f'{novos}' in items_adicionados):
                 atualizar_valor = Item.objects.get(id=novos.id)
                 atualizar_valor_item = ItemEntrega.objects.get(entrega_id=id, item=novos)
                 atualizar_valor_item.quantidade += form.cleaned_data.get("quantidade") * atualizar_valor.multiplicador
                 atualizar_valor_item.save()
                 movimentacao = Movimentacao(item=novos, 
                                            data_movimento=timezone.now(),
                                            quantidade=form.cleaned_data.get("quantidade") * atualizar_valor.multiplicador,
                                            tipo = ContentType.objects.get_for_model(ItemEntrega),
                                            por = request.user,
                                            object_id = atualizar_valor_item.id)
                 movimentacao.save()
                 atualizar_valor.estoque_atual =  atualizar_valor.estoque_atual - form.cleaned_data.get("quantidade") * atualizar_valor.multiplicador
                 atualizar_valor.save()
                 messages.success(request, "Itens atualizados com sucesso!")
            else:
                atualizar_valor = Item.objects.get(id=novos.id)
                if form.cleaned_data.get("quantidade") * atualizar_valor.multiplicador <= atualizar_valor.estoque_atual: 
                    novos_itens = ItemEntrega(entrega=entrega, item=novos, quantidade=form.cleaned_data.get("quantidade") * atualizar_valor.multiplicador)
                    novos_itens.save()
                    movimentacao = Movimentacao(item=novos, 
                                            data_movimento=timezone.now(),
                                            quantidade=form.cleaned_data.get("quantidade") * atualizar_valor.multiplicador,
                                            tipo = ContentType.objects.get_for_model(ItemEntrega),
                                            por = request.user,
                                            object_id = novos_itens.id)
                    movimentacao.save()
                    atualizar_valor.estoque_atual =  atualizar_valor.estoque_atual - form.cleaned_data.get("quantidade") * atualizar_valor.multiplicador
                    atualizar_valor.save()
                    messages.success(request, "Itens adicionados!")
                else:
                    qtd_solicitada = form.cleaned_data.get("quantidade")
                    qtd_estoque = atualizar_valor.estoque_atual
                    messages.error(request, f"A quantidade solicitada ({qtd_solicitada}g) é maior do que se há disponível em estoque ({qtd_estoque}g)")
            return redirect(f"/entregas/{entrega.id}")
        else:   
            messages.error(request, "Dados inválidos, itens não foram adicionados!")
            return redirect(f"/entregas/{entrega.id}")
        
    else:
        form = ItensForm()
    return render(request, "entregas/pages/cadastro_itens_entrega.html", {'form': form, 'entrega': entrega})



def get_data(request):
    data = Item.objects.all().values('nome','unidade') 
    return JsonResponse(list(data), safe=False)

def get_unidades(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == 'GET':
        item_id = request.GET.get('item_id')
        item = Item.objects.get(id=item_id)
        unidade = item.unidade
        return JsonResponse({'unidades': unidade})
    
