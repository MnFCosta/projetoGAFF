from django.contrib import admin
from django.urls import include, path
from visitas import views


app_name = 'visitas'

urlpatterns = [
    path('visita', views.visitas, name="visita"),
    path('visita/<int:id>/', views.visitaDetail, name="visita_detail"),
    path('cadastro_visita/<int:id>/', views.cadastroVisita, name="cadastro_visita"),
    path('cadastro_participantes/<int:id>/', views.participantesVisita, name="cadastro_participantes"),
    
]

