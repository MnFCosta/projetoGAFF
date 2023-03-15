from django.contrib import admin
from django.urls import include, path
from familias import views


app_name = 'familias'

urlpatterns = [
    path('cadastro', views.cadastroComponente, name="cadastro"),
]

