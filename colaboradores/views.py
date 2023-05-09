from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

from .forms import ColaboradorEditForm
from .models import User

# Create your views here.
def colaboradores(request):
    users = User.objects.order_by("-id")
    
    search_query = request.GET.get('search')
    if search_query:
        users = User.objects.filter(Q(nome__icontains=search_query) | Q(email__icontains=search_query))
        if len(users) == 0:
            messages.error(request, "O colaborador em questão não foi encontrado !")
            users = User.objects.order_by("-id")
    
    paginator = Paginator(users, 21)
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

    return render(request, "colaboradores/pages/colaboradores.html", context)

def colaboradorDetail(request, id):
    colaborador = get_object_or_404(User,
        pk=id
    )

    return render(request, 'colaboradores/pages/colaborador_detail.html', context={
        "colaboradores": colaborador,
        "is_detail_page": True,
    })

def colaboradorEdit(request, id):
    colaborador = get_object_or_404(User,
        pk=id
    )
 
    if request.method == "POST":
        form = ColaboradorEditForm(request.POST)
        if form.is_valid():
            colaborador.nome = form.cleaned_data['nome']
            colaborador.celular = form.cleaned_data['telefone']
            colaborador.rua = form.cleaned_data['rua']
            colaborador.bairro = form.cleaned_data['bairro']
            colaborador.numero = form.cleaned_data['numero_casa']
            colaborador.cidade = form.cleaned_data['cidade']
            colaborador.unidade_federativa = form.cleaned_data['unidade_federativa']
            colaborador.save()
            messages.success(request, "Dados atualizados com sucesso!")
            return redirect(f"/colaboradores/{id}")
        else:
            messages.error(request, "Dados inválidos, tente novamente!")
            return redirect(f"/colaboradores_editar/{id}") 
    else:
        form = ColaboradorEditForm(initial={
        'nome': colaborador.nome,
        'telefone': colaborador.celular,
        'rua': colaborador.rua,
        'bairro': colaborador.bairro,
        'numero_casa': colaborador.numero,
        'cidade': colaborador.cidade,
        'unidade_federativa': colaborador.unidade_federativa,
    })

    return render(request, 'colaboradores/pages/colaborador_edit.html', context={
        "form": form,
        "colaboradores": colaborador,
        "is_detail_page": True,
    })
