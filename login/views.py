from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "login/pages/login.html")

def signin(request):
    return render(request, "login/pages/signin.html")

def register(request):
    return render(request, "login/pages/register.html")

def signout(request):
    pass
