from django.contrib import admin
from .models import Categoria, FAQ

#FAQ admin

admin.site.site_header = 'FAQ'
admin.site.site_title = 'Sistemas FAQ'

class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('id','categoria')
    ordering = ['id']
    list_per_page = 20
    search_fields = ['id','categoria']

admin.site.register(Categoria,CategoriasAdmin)

class FAQAdmin(admin.ModelAdmin):
    list_display = ('id','titulo')
    ordering = ['id']
    list_per_page = 20
    search_fields = ['id']


admin.site.register(FAQ,FAQAdmin)