from django.db import models
from veiculo.models import Veiculo
from django.contrib.auth.models import User

class Anuncio(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=200)
    preco = models.DecimalField(decimal_places=2, max_digits=10)
    
    veiculo = models.ForeignKey(Veiculo, related_name='anuncios', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, related_name='anuncios_realizados', on_delete=models.CASCADE)