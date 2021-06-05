from django.db import models
from datetime import datetime

from django.db.models.deletion import CASCADE
from pessoas.models import Pessoas
# Create your models here.

class Receita(models.Model):
    nome_pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    date_receita = models.DateTimeField(default=datetime.now, blank=True)