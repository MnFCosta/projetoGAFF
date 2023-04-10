from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import User
# Create your views here.


def colaboradores(request):
    users = User.objects.order_by("id")
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