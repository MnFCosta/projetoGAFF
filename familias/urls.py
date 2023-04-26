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

]

