from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from .models import *
from estoque.models import *
from .forms import *
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q

# Create your views here.
def doacoes(request):
    doacoes = Doacao.objects.order_by("-id")

    search_query = request.GET.get('search')
    if search_query:
        doacoes = Doacao.objects.filter(Q(doador__nome__icontains=search_query))
        if len(doacoes) == 0:
            messages.error(request, "A doação em questão não foi encontrada !")
            doacoes = Doacao.objects.order_by("-id")

    paginator = Paginator(doacoes, 21)
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
    
    return render(request, "doacoes/pages/doacoes.html", context)

def cadastroDoador(request):
    if request.method == 'POST':
        form = DoadorForm(request.POST)
        if form.is_valid():
            novo_doador = Doador(nome=form.cleaned_data.get("nome"),
                                 celular=form.cleaned_data.get("celular"),
                                 bairro=form.cleaned_data.get("bairro"),
                                 rua=form.cleaned_data.get("rua"),
                                 numero=form.cleaned_data.get("numero"),
                                 cidade=form.cleaned_data.get("cidade"),
                                 unidade_federativa=form.cleaned_data.get("unidade_federativa"),
                                                )
            novo_doador.save()
            messages.success(request, "Doador criado!")
            return redirect("doacoes:doadores") 
        else:   
            messages.error(request, "Dados inválidos!")

            return redirect("doacoes:cadastro_doador")
        
    else:
        form = DoadorForm()
    return render(request, "doacoes/pages/cadastro_doador.html", {'form': form})

def doadores(request):
    doadores = Doador.objects.order_by("-id")
    search_query = request.GET.get('search')
    if search_query:
        doadores = Doador.objects.filter(Q(nome__icontains=search_query))
        if len(doadores) == 0:
            messages.error(request, "O doador em questão não foi encontrado !")
            doadores = Doador.objects.order_by("-id")

    paginator = Paginator(doadores, 21)
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
    
    return render(request, "doacoes/pages/doadores.html", context)

def cadastroDoacao(request, id):
    doador = Doador.objects.get(id=id)
    nova_doacao = Doacao(doador=doador,
                                 data_doacao=timezone.now(),
                                                )
    nova_doacao.save()
    messages.success(request, "Doação Criada, adicione items!")
    return redirect(f"/cadastro_itens/{nova_doacao.id}")
        
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

def doadoresDetail(request, id):
    doador = get_object_or_404(Doador,
        pk=id
    )

    doacoes = Doacao.objects.filter(doador=id).order_by("-id")

    paginator = Paginator(doacoes, 15)
    page_number = request.GET.get('page')

    try:
        current_page = paginator.get_page(page_number)
    except PageNotAnInteger:
        current_page = paginator.get_page(1)
    except EmptyPage:
        current_page = paginator.get_page(paginator.num_pages)
    

    return render(request, 'doacoes/pages/doador_detail.html', context={
        "doador": doador,
        "is_detail_page": True,
        'pagination': current_page,
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
            print(novos.id) 
            print(items_adicionados)
            if (f'{novos}' in items_adicionados):
                atualizar_valor = Item.objects.get(id=novos.id)
                atualizar_valor_item = ItemDoacao.objects.get(doacao_id=id, item=novos)
                atualizar_valor_item.quantidade += form.cleaned_data.get("quantidade") * atualizar_valor.multiplicador
                atualizar_valor_item.save()
                movimentacao = Movimentacao(item=novos, 
                                            data_movimento=timezone.now(),
                                            quantidade=form.cleaned_data.get("quantidade") * atualizar_valor.multiplicador,
                                            tipo = ContentType.objects.get_for_model(ItemDoacao),
                                            por = request.user,
                                            object_id = atualizar_valor_item.id)
                movimentacao.save()
                atualizar_valor.estoque_atual += form.cleaned_data.get("quantidade") * atualizar_valor.multiplicador
                atualizar_valor.save()
                messages.success(request, "Itens atualizados com sucesso!")
            else:
                atualizar_valor = Item.objects.get(id=novos.id)
                novos_itens = ItemDoacao(doacao=doacao, item=novos, quantidade=form.cleaned_data.get("quantidade") * atualizar_valor.multiplicador)
                novos_itens.save()
                movimentacao = Movimentacao(item=novos, 
                                            data_movimento=timezone.now(),
                                            quantidade=form.cleaned_data.get("quantidade") * atualizar_valor.multiplicador,
                                            tipo = ContentType.objects.get_for_model(ItemDoacao),
                                            por = request.user,
                                            object_id = novos_itens.id)
                movimentacao.save()
                atualizar_valor.estoque_atual += form.cleaned_data.get("quantidade") * atualizar_valor.multiplicador
                atualizar_valor.save() 
                messages.success(request, "Itens adicionados!")

            return redirect(f"/doacoes/{doacao.id}/")
        else:   
            messages.error(request, "Dados inválidos, itens não foram adicionados!")
            return redirect(f"/doacoes/{doacao.id}/")
        
    else:
        form = ItensForm()
    return render(request, "doacoes/pages/cadastro_itens.html", {'form': form, 'doacao': doacao})

def doadorEdit(request, id):
    doador = get_object_or_404(Doador,
        pk=id
    )
 
    if request.method == "POST":
        form = DoadorEditForm(request.POST)
        print(form.errors)
        if form.is_valid():
            doador.celular = form.cleaned_data['celular']
            doador.rua = form.cleaned_data['rua']
            doador.bairro = form.cleaned_data['bairro']
            doador.numero = form.cleaned_data['numero']
            doador.cidade = form.cleaned_data['cidade']
            doador.unidade_federativa = form.cleaned_data['unidade_federativa']
            doador.save()
            messages.success(request, "Dados atualizados com sucesso!")
            return redirect(f"/doadores/{id}")
        else:
            messages.error(request, "Dados inválidos, tente novamente!")
            return redirect(f"/editar_doador/{id}") 
    else:
        form = DoadorEditForm(initial={
        'celular': doador.celular,
        'rua': doador.rua,
        'bairro': doador.bairro,
        'numero': doador.numero,
        'cidade': doador.cidade,
        'unidade_federativa': doador.unidade_federativa,
    })

    return render(request, 'doacoes/pages/doador_edit.html', context={
        "form": form,
        "doador": doador,
        "is_detail_page": True,
    })
