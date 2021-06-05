from django.db import models


# Create your models here.

# Aqui estou criando um modelo de pessoas, onde vou vincular o cadastro de pessoas a minha receita
class Pessoas(models.Model):

     Nome = models.CharField(max_length=100)
     email = models.CharField(max_length=100)
     
     def __str__(self):

         return self.Nome

 

        