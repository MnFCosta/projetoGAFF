from django.shortcuts import render
from .models import User
# Create your views here.


def colaboradores(request):
    users = User.objects.order_by("id")
    
    return render(request, "login/pages/login.html", context={
        "usuarios": users,
    })