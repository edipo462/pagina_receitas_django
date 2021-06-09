from django.db import models
from datetime import datetime

from django.db.models.deletion import CASCADE
from pessoas.models import Pessoas

# Create your models here.
# Criei um modelo para categoria, assim teremos categorias cadastradas e nao que o usuário coloque
class Categoria(models.Model):

    categoria = models.CharField(max_length=100)

    def __str__ (self):

        return self.categoria
#Aqui criei um modelo de receitas onde relaciono com o Modelo Pessoas e Categoria
class Receita(models.Model):
    nome_pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    date_receita = models.DateTimeField(default=datetime.now, blank=True)
    publicar = models.BooleanField(default=False)
    foto_receita = models.ImageField()