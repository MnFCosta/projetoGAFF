from django.contrib import admin
from entregas.models import *
import math
# Register your models here.

class EntregaAdmin(admin.ModelAdmin):
    list_display = ('id','familia', 'data_entrega')
    list_display_links = ('id','familia', 'data_entrega')
    search_fields = ('id','familia', 'data_entrega')

admin.site.register(Entrega, EntregaAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'codigo_barras', 'estoque_display')
    list_display_links = ('id','nome', 'codigo_barras', 'estoque_display')
    search_fields = ('id','nome', 'codigo_barras', 'estoque_display')

    def estoque_display(self, obj):
        return f"{math.trunc(obj.estoque_atual)}g" 
    
    estoque_display.short_description = 'Em estoque' # type: ignore

admin.site.register(Item, ItemAdmin)

class EntregaItensAdmin(admin.ModelAdmin):
    list_display = ('id','item', 'entrega', 'quantidade_display')
    list_display_links = ('id','item', 'entrega', 'quantidade_display')
    search_fields = ('id','item', 'entrega', 'quantidade_display')

    def quantidade_display(self, obj):
        return f"{math.trunc(obj.quantidade)}g"
    
    quantidade_display.short_description = 'Quantidade' # type: ignore

admin.site.register(ItemEntrega, EntregaItensAdmin)