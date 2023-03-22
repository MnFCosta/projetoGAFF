from django.shortcuts import render
from .models import *

# Create your views here.
def doacoes(request):
    doacoes = Doacao.objects.order_by("id")
    
    return render(request, "doacoes/pages/doacoes.html", context={
        "doacoes": doacoes,
    })