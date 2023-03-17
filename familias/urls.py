from django.contrib import admin
from django.urls import include, path
from familias import views


app_name = 'familias'

urlpatterns = [
    path('familias', views.familias, name="familias"),
    path('cadastro', views.cadastroComponente, name="cadastro"),
    path('cadastro_familia', views.cadastroFamilia, name="cadastro_familia"),
    path('renda', views.cadastroRenda, name="renda"),
]

