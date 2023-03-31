from django.shortcuts import get_object_or_404, render
from .models import User
# Create your views here.


def colaboradores(request):
    users = User.objects.order_by("id")
    
    return render(request, "colaboradores/pages/colaboradores.html", context={
        "usuarios": users,
    })

def colaboradorDetail(request, id):
    colaborador = get_object_or_404(User,
        pk=id
    )
    """ itens = ItemDoacao.objects.filter(
        doacao=id
        ).order_by("-id") """

    return render(request, 'colaboradores/pages/colaborador_detail.html', context={
        "colaboradores": colaborador,
        "is_detail_page": True,
    })