from django.contrib import admin
from familias.models import *
# Register your models here.

class ComponenteAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'cpf','rg','papel','nascimento')
    list_display_links = ('id','nome', 'cpf','rg','papel','nascimento')
    search_fields = ('id','nome', 'cpf','rg','papel','nascimento')

admin.site.register(componenteFamilia, ComponenteAdmin)

class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    filter_horizontal = ('componentes',)


admin.site.register(Familia, FamiliaAdmin)

class RendaAdmin(admin.ModelAdmin):
    list_display = ('id','familia', 'valor')
    list_display_links = ('id','familia', 'valor')
    search_fields = ('id','familia','valor')

admin.site.register(RendaFamiliar, RendaAdmin)

