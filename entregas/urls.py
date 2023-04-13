from django.contrib import admin
from django.urls import include, path
from entregas import views


app_name = 'entregas'

urlpatterns = [
    path('entregas', views.entregas, name="entregas"),
    path('entregas/<int:id>', views.entregaDetail, name="entregas_detail"),
    path('cadastro_entregas', views.cadastroEntrega, name="cadastro_entregas"), 
    path('cadastro_itens_entrega/<int:id>', views.itensEntrega, name="cadastro_itens_entrega"),
    path('get_data/', views.get_data, name='get_data'),
    path('get_unidades/', views.get_unidades, name='get_unidades'),

]