from django.contrib import admin
from .models import Familia, componenteFamilia
# Register your models here.

class ComponenteAdmin(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id','nome')
    search_fields = ('nome',)

admin.site.register(componenteFamilia, ComponenteAdmin)

class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id','nome')
    search_fields = ('nome',)


admin.site.register(Familia, FamiliaAdmin)

