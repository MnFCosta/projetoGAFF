from django.contrib import admin
from entregas.models import *
# Register your models here.

class EntregaAdmin(admin.ModelAdmin):
    list_display = ('id','familia', 'data_entrega')
    list_display_links = ('id','familia', 'data_entrega')
    search_fields = ('id','familia', 'data_entrega')

admin.site.register(Entrega, EntregaAdmin)