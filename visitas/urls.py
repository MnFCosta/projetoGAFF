from django.contrib import admin
from django.urls import include, path
from visitas import views


app_name = 'visitas'

urlpatterns = [
    path('visita', views.visitas, name="visita"),
    path('visita/<int:id>/', views.visitaDetail, name="visita_detail"),
    path('visita_remove/<int:id_visita>/<int:id>', views.removeParticipante, name="visita_detail"),
    path('editar_visita/<int:id>/', views.visitaEdit, name="visita_editar"),
    path('cadastro_visita/<int:id>/', views.cadastroVisita, name="cadastro_visita"),
    path('cadastro_participantes/<int:id>/', views.participantesVisita, name="cadastro_participantes"),
    
]

