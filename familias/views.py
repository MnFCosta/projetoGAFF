from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.contrib import messages
from .forms import *
from .models import *

# Create your views here.
def familias(request):
    familias = Familia.objects.order_by("-id")


    search_query = request.GET.get('search')
    if search_query:
        familias = Familia.objects.filter(Q(nome__icontains=search_query))
        if len(familias) == 0:
            messages.error(request, "A familia em questão não foi encontrada !")
            familias = Familia.objects.order_by("-id")

    paginator = Paginator(familias, 21)
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
    
    return render(request, "familias/pages/familias.html", context)


def cadastroComponente(request, id):
    familia = Familia.objects.get(id=id)
    if request.method == 'POST':
        form = ComponenteForm(request.POST)
        if form.is_valid():
            novo_componente = componenteFamilia(nome=form.cleaned_data.get("nome"),
                                                cpf=form.cleaned_data.get("cpf"),
                                                rg=form.cleaned_data.get("rg"),
                                                papel=form.cleaned_data.get("papel"),
                                                nascimento=form.cleaned_data.get("nascimento"),
                                                NR_calcado=form.cleaned_data.get("NR_calcado"),
                                                NR_roupa=form.cleaned_data.get("NR_roupa"))

            novo_componente.save()
            familia.componentes.add(novo_componente)
            familia.save()
            messages.success(request, "Componente Criado!")

            return redirect(f"/familias/{id}")
        else:   
            messages.error(request, "Dados inválidos!")
            return redirect(f"/familias/{id}")
        
    else:
        form = ComponenteForm()
    return render(request, "familias/pages/cadastro.html", {'form': form, 'id': id})
   

def cadastroFamilia(request):
    if request.method == 'POST':
        form = FamiliaForm(request.POST)
        print(form.errors)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.realizado_por = request.user  
            instance.save()
            form.save_m2m()
            messages.success(request, "Familia Criada!")
            return redirect("familias:familias") 
        else:   
            messages.error(request, "Dados inválidos!")
            return redirect("familias:cadastro_familia") 
        
    else:
        form = FamiliaForm()
    return render(request, "familias/pages/cadastro_familia.html", {'form': form})

def cadastroRenda(request,id):
    familia = Familia.objects.get(id=id)
    if request.method == 'POST':
        form = RendaForm(request.POST)
        if form.is_valid():
            nova_renda= RendaFamiliar(familia=familia,
                                                origem_renda=form.cleaned_data.get("origem_renda"),
                                                valor=form.cleaned_data.get("valor"),)

            nova_renda.save()
            messages.success(request, "Renda Cadastrada!")
            return redirect(f"/familias/{id}")
        else:   
            messages.error(request, "Dados inválidos, renda não cadastrada!")
            return redirect(f"/familias/{id}")
        
    else:
        form = RendaForm()
    return render(request, "familias/pages/cadastro_renda.html", {'form': form, 'id': id})


def familiaDetail(request, id):
    familia = get_object_or_404(Familia,
        pk=id
    )
    renda = RendaFamiliar.objects.filter(familia_id=id)

    if not renda:
        messages.warning(request, 'Esta família não possui nenhuma renda!')

    return render(request, 'familias/pages/familia_detail.html', context={
        "familia": familia,
        "renda": renda,
        "is_detail_page": True,

    })

def componenteDetail(request, id):
    componente = get_object_or_404(componenteFamilia,
        pk=id
    )

    return render(request, 'familias/pages/componente_detail.html', context={
        "componente": componente,
        "is_detail_page": True,

    })


def familiaEdit(request, id):
    familia = get_object_or_404(Familia,
        pk=id
    )
    if request.method == "POST":
        form = FamiliaEditForm(request.POST)
        if form.is_valid():
            familia.celular = form.cleaned_data['celular']
            familia.moradia = form.cleaned_data['moradia']
            familia.casa_de = form.cleaned_data['casa_de']
            familia.condicoes_casa = form.cleaned_data['condicoes_casa']
            familia.aluguel = form.cleaned_data['aluguel']
            familia.rua = form.cleaned_data['rua']
            familia.bairro = form.cleaned_data['bairro']
            familia.numero = form.cleaned_data['numero']
            familia.cidade = form.cleaned_data['cidade']
            familia.unidade_federativa = form.cleaned_data['unidade_federativa']
            familia.latitude = form.cleaned_data['latitude']
            familia.longitude = form.cleaned_data['longitude']
            familia.cep = form.cleaned_data['cep']
            familia.observacao = form.cleaned_data['observacao']
            familia.save()
            messages.success(request, "Dados atualizados com sucesso!")
            return redirect(f"/familias/{id}")
        else:
            messages.error(request, "Dados inválidos, tente novamente!")
            return redirect(f"/familia_editar/{id}") 
    else:
        form = FamiliaEditForm(initial={
        'celular': familia.celular,
        'moradia': familia.moradia,
        'casa_de': familia.casa_de,
        'condicoes_casa': familia.condicoes_casa,
        'aluguel': familia.aluguel,
        'rua': familia.rua,
        'bairro': familia.bairro,
        'numero': familia.numero,
        'cidade': familia.cidade,
        'unidade_federativa': familia.unidade_federativa,
        'latitude': familia.latitude,
        'longitude': familia.longitude,
        'cep': familia.cep,
        'observacao': familia.observacao,
    })

    return render(request, 'familias/pages/familia_edit.html', context={
        "form": form,
        "familia": familia,
        "is_detail_page": True,
    })


def componenteEdit(request, id):
    componente = get_object_or_404(componenteFamilia,
        pk=id
    )

    familia = get_object_or_404(Familia, componentes=id)

    if request.method == "POST":
        form = ComponenteEditForm(request.POST)
        if form.is_valid():
            componente.nome = form.cleaned_data['nome']
            componente.cpf = form.cleaned_data['cpf']
            componente.rg = form.cleaned_data['rg']
            componente.papel = form.cleaned_data['papel']
            componente.nascimento = form.cleaned_data['nascimento']
            componente.NR_calcado = form.cleaned_data['NR_calcado']
            componente.NR_roupa = form.cleaned_data['NR_roupa']
            componente.save()
            messages.success(request, "Dados atualizados com sucesso!")
            return redirect(f"/familias/{familia.id}")
        else:
            messages.error(request, "Dados inválidos, tente novamente!")
            return redirect(f"/componente_editar/{id}") 
    else:
        form = ComponenteEditForm(initial={
        'nome': componente.nome,
        'cpf': componente.cpf,
        'rg': componente.rg,
        'papel': componente.papel,
        'nascimento': componente.nascimento,
        'NR_calcado': componente.NR_calcado,
        'NR_roupa': componente.NR_roupa,
    })

    return render(request, 'familias/pages/componente_edit.html', context={
        "form": form,
        "componente": componente,
        "is_detail_page": True,
    })

def rendaEdit(request, id):
    renda = get_object_or_404(RendaFamiliar,
        pk=id
    )

    id_familia=renda.familia.id

    if request.method == "POST":
        form = RendaEditForm(request.POST)
        if form.is_valid():
            renda.origem_renda = form.cleaned_data['origem_renda']
            renda.valor = form.cleaned_data['valor']
            renda.save()
            messages.success(request, "Dados atualizados com sucesso!")
            return redirect(f"/familias/{id_familia}")
        else:
            messages.error(request, "Dados inválidos, tente novamente!")
            return redirect(f"/renda_editar/{id}") 
    else:
        form = RendaEditForm(initial={
        'origem_renda': renda.origem_renda,
        'valor': renda.valor,
    })

    return render(request, 'familias/pages/renda_edit.html', context={
        "form": form,
        "renda": renda,
        "is_detail_page": True,
    })


def removeRenda(request, id):
    renda = get_object_or_404(RendaFamiliar,
        pk=id
    )
    id_familia=renda.familia.id

    renda.delete()
    messages.success(request, "Renda apagada com sucesso!")
    return redirect(f"/familias/{id_familia}")

def removeComponente(request, id):
    componente = get_object_or_404(componenteFamilia,
        pk=id
    )
    familia = get_object_or_404(Familia, componentes=id)

    componente.delete()
    messages.success(request, "Componente apagado com sucesso!")
    return redirect(f"/familias/{familia.id}")
  
    


    
