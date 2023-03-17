from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *

# Create your views here.

def visitas(request):
    visitas = Visita.objects.order_by("id")
    
    return render(request, "visitas/pages/visitas.html", context={
        "visitas": visitas,
    })


def cadastroVisita(request):
    if request.method == 'POST':
        form = VisitaForm(request.POST)
        if form.is_valid():
            nova_visita = Visita(familia=form.cleaned_data.get("familia"),
                                            data=form.cleaned_data.get("data"),
                                            pedidos=form.cleaned_data.get("pedidos"),
                                            observacao=form.cleaned_data.get("observacao"),
                                                )

            nova_visita.save()
            messages.success(request, "Visita Criada!")
            return redirect("visitas:visita")
        else:   
            messages.error(request, "Dados inválidos!")
            return redirect("visitas:cadastro_visita")
        
    else:
        form = VisitaForm()
    return render(request, "visitas/pages/cadastro_visita.html", {'form': form})