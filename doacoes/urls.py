from django.contrib import admin
from django.urls import include, path
from doacoes import views


app_name = 'doacoes'

urlpatterns = [
    path('doacoes', views.doacoes, name="doacoes"), 
    path('doacoes/<int:id>/', views.doacaoDetail, name="doacao_detail"),
    path('cadastro_doacao', views.cadastroDoacao, name="cadastro_doacao"),
    path('cadastro_itens/<int:id>', views.itensDoacao, name="cadastro_itens")
    

]

