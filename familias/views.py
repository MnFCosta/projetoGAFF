from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from .forms import *
from .models import *

# Create your views here.
def familias(request):
    familias = Familia.objects.order_by("id")
    paginator = Paginator(familias, 19)
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
    
    return render(request, "familias/pages/familias.html", context)


def cadastroComponente(request):
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
            messages.success(request, "Componente Criado!")
        else:   
            messages.error(request, "Dados inválidos!")
            return redirect("familias:cadastro")
        
    else:
        form = ComponenteForm()
    return render(request, "familias/pages/cadastro.html", {'form': form})

def cadastroFamilia(request):
    if request.method == 'POST':
        form = FamiliaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Familia Criada!")
            return redirect("familias:familias") 
        else:   
            messages.error(request, "Dados inválidos!")
            return redirect("familias:cadastro_familia") 
        
    else:
        form = FamiliaForm()
    return render(request, "familias/pages/cadastro_familia.html", {'form': form})

def cadastroRenda(request):
    if request.method == 'POST':
        form = RendaForm(request.POST)
        if form.is_valid():
            nova_renda= RendaFamiliar(familia=form.cleaned_data.get("familia"),
                                                origem_renda=form.cleaned_data.get("origem_renda"),
                                                valor=form.cleaned_data.get("valor"),)

            nova_renda.save()
            messages.success(request, "Renda Cadastrada!")
        else:   
            messages.error(request, "Dados inválidos!")
            return redirect("familias:renda")
        
    else:
        form = RendaForm()
    return render(request, "familias/pages/cadastro_renda.html", {'form': form})


def familiaDetail(request, id):
    familia = get_object_or_404(Familia,
        pk=id
    )
    """ itens = ItemDoacao.objects.filter(
        doacao=id
        ).order_by("-id") """

    return render(request, 'familias/pages/familia_detail.html', context={
        "familia": familia,
        "is_detail_page": True,
    })