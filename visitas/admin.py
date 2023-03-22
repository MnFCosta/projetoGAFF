from django.contrib import admin
from visitas.models import *
# Register your models here.

class VisitasAdmin(admin.ModelAdmin):
    list_display = ('id','familia', 'data')
    list_display_links = ('id','familia', 'data')
    search_fields = ('id','familia', 'data')

admin.site.register(Visita, VisitasAdmin)

class ParticipantesAdmin(admin.ModelAdmin):
    list_display = ('id','visita')
    list_display_links = ('id','visita')
    search_fields = ('id','visita')

admin.site.register(VisitaParticipantes, ParticipantesAdmin)