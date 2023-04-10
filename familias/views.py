from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from .forms import *
from .models import *

# Create your views here.
def familias(request):
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
        if form.is_valid():
            instance = form.save(commit=False)
            instance.realizado_por = request.user  # Set the user field
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
            messages.error(request, "Dados inválidos!")
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