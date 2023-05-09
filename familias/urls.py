from django.contrib import admin
from django.urls import include, path
from familias import views


app_name = 'familias'

urlpatterns = [
    path('familias', views.familias, name="familias"),
    path('cadastro/<int:id>', views.cadastroComponente, name="cadastro"),
    path('cadastro_familia', views.cadastroFamilia, name="cadastro_familia"),
    path('renda/<int:id>', views.cadastroRenda, name="renda"),
    path('familias/<int:id>', views.familiaDetail, name="familia_detail"),
    path('componente/<int:id>', views.componenteDetail, name="componente_detail"),
    path('familia_editar/<int:id>', views.familiaEdit, name="familias_editar"),
    path('componente_editar/<int:id>', views.componenteEdit, name="componente_editar"),
    path('remove_renda/<int:id>', views.removeRenda, name="remove_renda"),
    path('renda_editar/<int:id>', views.rendaEdit, name="renda_editar"),
    path('remove_componente/<int:id>', views.removeComponente, name="remove_componente"),

]

