
from django.db import models

class Alimento(models.Model):
	nome = models.CharField(max_length=100)
	peso = models.FloatField()
	quantidade = models.IntegerField()
	preco_por_unidade = models.FloatField()

	def __str__(self):
		return self.nome
