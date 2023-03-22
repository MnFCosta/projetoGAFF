from django.shortcuts import render
from .models import *

# Create your views here.
def entregas(request):
    entregas = Entrega.objects.order_by("id")
    
    return render(request, "entregas/pages/entregas.html", context={
        "entregas": entregas,
    })