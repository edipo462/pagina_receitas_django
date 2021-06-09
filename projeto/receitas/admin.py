from django.contrib import admin
from .models import Receita, Categoria
# Register your models here.


class ListaDeReceitas (admin.ModelAdmin):

    list_display = ('id', 'nome_receita',  'publicar')
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_editable = ('publicar',)
    list_per_page = 2

admin.site.register(Receita, ListaDeReceitas)

class ListaCategoria(admin.ModelAdmin):

    list_display = ('id', 'categoria')
    

admin.site.register(Categoria, ListaCategoria)
