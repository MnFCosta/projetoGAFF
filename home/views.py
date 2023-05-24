from django.shortcuts import render
from visitas.models import Visita, VisitaParticipantes
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def view(request):
    visitas = []
    colaborador = request.user.id
    participantes = VisitaParticipantes.objects.filter(Q(participantes=colaborador))
    for participantes in participantes:
            visitas.append(participantes.visita)

    search_query = request.GET.get('search')
    if search_query:
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
    return render(request, 'home/pages/home.html', context )