from django.shortcuts import render
from entregas.models import Item

# Create your views here.
def estoque(request):
    itens = Item.objects.order_by("id")
    
    return render(request, "estoque/pages/itens.html", context={
        "itens": itens,
    })