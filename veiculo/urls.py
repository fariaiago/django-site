from django.urls import path
from veiculo.views import ListarVeiculos, FotoVeiculo, CriarVeiculos, EditarVeiculos

urlpatterns = [
	path('', ListarVeiculos.as_view(), name='listar-veiculos'),
	path('novo/', CriarVeiculos.as_view(), name='criar-veiculos'),
	path('<int:pk>/', EditarVeiculos.as_view(), name='editar-veiculos'),
	path('fotos/<str:arquivo>/', FotoVeiculo.as_view(), name="foto-veiculo"),
]
