from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Receita

#A função index foi criada para renderizar os dados do 'index.html' e receber os dados do banco de dados
def index(request):

    receitas = Receita.objects.order_by('-date_receita').filter(publicar=True)

    dados = {
        'receitas' : receitas
    }

    return render(request, 'index.html', dados)

#A função receita foi criada para renderizar a pagina de receitas (a receita selecionada (ID))
def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita' : receita
    }
    return render(request, 'receita.html', receita_a_exibir)


