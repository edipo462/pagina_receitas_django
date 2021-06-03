from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    receitas = {
        1: 'Sorvete',
        2: 'Bolo de cenoura',
        3: 'Torta de limão'
    }

    dados = {
        'nome_das_receitas' : receitas
    }

    return render(request, 'index.html', dados)

def receita(request):
    return render(request, 'receita.html')
