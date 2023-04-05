from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from .forms import *
from .models import *
from utils.utils import checar_repeticao

# Create your views here.

def visitas(request):
    visitas = Visita.objects.order_by("id")
    paginator = Paginator(visitas, 21)
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
    
    return render(request, "visitas/pages/visitas.html", context)



def visitaDetail(request, id):
    visita = get_object_or_404(Visita,
        pk=id
    )
    participantes = VisitaParticipantes.objects.filter(
        visita=id
        ).order_by("-id")

    return render(request, 'visitas/pages/visita_detail.html', context={
        "visita": visita,
        "colaboradores": participantes,
        "is_detail_page": True,
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

def participantesVisita(request, id):
    visita = Visita.objects.get(id=id)
    participantes = VisitaParticipantes.objects.filter(visita_id=id)

    participam = VisitaParticipantes.objects.none()
    for participante in participantes:
        var = participante.participantes.all()
        participam = participam | var
    if request.method == 'POST':
        form = ParticipantesForm(request.POST)
        if form.is_valid():
            
            novos=form.cleaned_data.get("participantes")    

            if checar_repeticao(participam,novos) == True:
                 messages.error(request, "Os mesmos participantes já foram adicionados anteriormente!")
            else:
                novos_participantes = VisitaParticipantes(visita=visita)
                novos_participantes.save()
                novos_participantes.participantes.set(novos)
                messages.success(request, "Participantes adicionados!")

            return redirect(f"/visita/{visita.id}/")
        else:   
            messages.error(request, "Dados inválidos!")
            return redirect("visitas:visita")
        
    else:
        form = ParticipantesForm()
    return render(request, "visitas/pages/cadastro_participantes.html", {'form': form, 'visita': visita})

