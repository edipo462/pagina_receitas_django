from django.contrib import admin
from .models import Pessoas
# Register your models here.


#registrando o modelo de pessoas criado em models.py
class Lista_Pessoas(admin.ModelAdmin):

    list_display = ('id', 'Nome', 'email')
    list_display_links = ('id', 'Nome')



admin.site.register(Pessoas, Lista_Pessoas)