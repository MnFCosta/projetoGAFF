from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *

# Create your views here.

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
        else:   
            messages.error(request, "Dados inválidos!")
            return redirect("familias:cadastro_familia") 
        
    else:
        form = FamiliaForm()
    return render(request, "familias/pages/cadastro_familia.html", {'form': form})
