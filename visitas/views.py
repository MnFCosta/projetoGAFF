from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.contrib import messages
from .forms import *
from .models import *

# Create your views here.
def visitas(request):
    visitas = Visita.objects.order_by("-id")

    search_query = request.GET.get('search')
    if search_query:
        visitas = Visita.objects.filter(Q(familia__nome__icontains=search_query))
        if len(visitas) == 0:
            messages.error(request, "A visita em questão não foi encontrada !")
            visitas = Visita.objects.order_by("-id")

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
        'list_page': True,
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

def cadastroVisita(request, id):
    familia = Familia.objects.get(id=id
    )
    if request.method == 'POST':
        form = VisitaForm(request.POST)
        if form.is_valid():
            nova_visita = Visita(familia=familia,
                                            data=form.cleaned_data.get("data"),
                                            pedidos=form.cleaned_data.get("pedidos"),
                                            observacao=form.cleaned_data.get("observacao"),
                                                )
            nova_visita.save()
            messages.success(request, "Visita Criada!")
            return redirect("visitas:visita")
        else:   
            messages.error(request, "Dados inválidos!")
            return redirect(f"/familias/{id}")
        
    else:
        form = VisitaForm()
    return render(request, "visitas/pages/cadastro_visita.html", {'form': form, 'familia': familia})

def participantesVisita(request, id):
    visita = Visita.objects.get(id=id)
    participantes = VisitaParticipantes.objects.filter(visita_id=visita.id).values_list('participantes__id', flat=True)
    print(participantes)
    form = ParticipantesForm()
    form.fields['participantes'].queryset = User.objects.exclude(id__in=participantes)
    if participantes != None:
        if len(form.fields['participantes'].queryset) == 0:
                    messages.error(request, "Não há mais participantes para adicionar!")
                    return redirect(f"/visita/{visita.id}/")


    if request.method == 'POST':
        form = ParticipantesForm(request.POST)
        if form.is_valid():
            novos = form.cleaned_data.get("participantes")
            novos_participantes = VisitaParticipantes(visita=visita)
            novos_participantes.save()
            novos_participantes.participantes.set(novos)
            messages.success(request, "Participantes adicionados!")

            return redirect(f"/visita/{visita.id}/")
        else:
            messages.error(request, "Dados inválidos!")
            return redirect("visitas:visita")
        
    else:
        search_query = request.GET.get('search')
        if search_query:
            form.fields['participantes'].queryset = User.objects.filter(nome__icontains=search_query).exclude(id__in=participantes)
            if len(form.fields['participantes'].queryset) == 0:
                messages.error(request, "O participante em questão não foi encontrado ou já foi adicionado!")
                return redirect(f"/visita/{visita.id}/")
        return render(request, "visitas/pages/cadastro_participantes.html", {'form': form, 'visita': visita})

def visitaEdit(request, id):
    visita = get_object_or_404(Visita,
        pk=id
    )
 
    if request.method == "POST":
        form = VisitaEditForm(request.POST)
        print(form.errors)
        if form.is_valid():
            visita.data = form.cleaned_data['data']
            visita.pedidos = form.cleaned_data['pedidos']
            visita.observacao = form.cleaned_data['observacao']
            visita.save()
            messages.success(request, "Dados atualizados com sucesso!")
            return redirect(f"/visita/{id}")
        else:
            messages.error(request, "Dados inválidos, tente novamente!")
            return redirect(f"/editar_visita/{id}") 
    else:
        form = VisitaEditForm(initial={
        'data': visita.data,
        'pedidos': visita.pedidos,
        'observacao': visita.observacao,
        
    })

    return render(request, 'visitas/pages/visita_edit.html', context={
        "form": form,
        "visita": visita,
        "is_detail_page": True,
    })

def removeParticipante(request, id, id_visita):
    participante = get_object_or_404(User,
        id=id
    )
    remover = VisitaParticipantes.objects.filter(
    Q(visita_id=id_visita) & Q(participantes=participante))

    for visita_participante in remover:
            visita_participante.participantes.remove(participante)
            if visita_participante.participantes.count() == 0:
                visita_participante.delete()


    messages.success(request, "Participante removido com sucesso!")
    return redirect(f"/visita/{id_visita}")