from django.contrib import admin
from .models import *
import math

# Register your models here.
class DoadorAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'celular', 'bairro', 'rua', 'numero', 'cidade', 'unidade_federativa')
    list_display_links = ('id','nome', 'celular', 'bairro', 'rua', 'numero', 'cidade', 'unidade_federativa')
    search_fields = ('id','nome', 'celular', 'bairro', 'rua', 'numero', 'cidade', 'unidade_federativa')
    
admin.site.register(Doador, DoadorAdmin)

class DoacoesAdmin(admin.ModelAdmin):
    list_display = ('id','doador', 'data_doacao')
    list_display_links = ('id','doador', 'data_doacao')
    search_fields =('id','doador', 'data_doacao')
    
admin.site.register(Doacao, DoacoesAdmin)

class DoacaoItensAdmin(admin.ModelAdmin):
    list_display = ('id','item', 'doacao', 'quantidade_display')
    list_display_links = ('id','item', 'doacao', 'quantidade_display')
    search_fields = ('id','item', 'doacao', 'quantidade_display')

    def quantidade_display(self, obj):
        return f"{math.trunc(obj.quantidade)}g"
    
    quantidade_display.short_description = 'Quantidade' # type: ignore

admin.site.register(ItemDoacao, DoacaoItensAdmin)