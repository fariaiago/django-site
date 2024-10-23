from django.db import models
from veiculo.consts import *
from datetime import datetime

class Veiculo(models.Model):
	marca = models.SmallIntegerField(choices=OPCOES_MARCAS)
	modelo = models.CharField(max_length=100)
	ano = models.IntegerField()
	cor = models.SmallIntegerField(choices=OPCOES_CORES)
	foto = models.ImageField(blank=True, null=True, upload_to='veiculo/fotos')
	combustivel = models.SmallIntegerField(choices=OPCOES_COMBUSTIVEIS)

	def anos_de_uso(self):
		return datetime.now().year - self.ano
	
	@property
	def veiculo_novo(self) -> bool:
		return self.ano == datetime.now().year