from django.contrib import admin
from django.urls import include, path
from doacoes import views


app_name = 'doacoes'

urlpatterns = [
    path('doacoes', views.doacoes, name="doacoes"), 
    path('doadores', views.doadores, name="doadores"), 
    path('doacoes/<int:id>/', views.doacaoDetail, name="doacao_detail"),
    path('doadores/<int:id>', views.doadoresDetail, name="doadores_detail"), 
    path('cadastro_doador/', views.cadastroDoador, name="cadastro_doador"),
    path('cadastro_doacao/<int:id>/', views.cadastroDoacao, name="cadastro_doacao"),
    path('cadastro_itens/<int:id>', views.itensDoacao, name="cadastro_itens")
]

