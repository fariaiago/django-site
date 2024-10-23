from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from veiculo.models import *
from veiculo.forms import *

class TestesModelVeiculo(TestCase):
	def setUp(self):
		self.instancia = Veiculo(marca=1, modelo='ABCDE', ano=datetime.now().year, cor=2, combustivel=3)
	
	def test_anos_uso(self):
		self.instancia.ano = datetime.now().year - 10
		self.assertEqual(self.instancia.anos_de_uso(), 10)
	
	def test_eh_novo(self):
		self.assertTrue(self.instancia.veiculo_novo)
		self.instancia.ano = datetime.now().year - 5
		self.assertFalse(self.instancia.veiculo_novo)

class TestesViewListarVeiculos(TestCase):
	def setUp(self):
		self.user = User.objects.create(username='teste', password='12345@teste')
		self.client.force_login(self.user)
		self.url = reverse('listar-veiculos')
		Veiculo(marca=1, modelo='ABCDE', ano=2, cor=3, combustivel=4).save()
	
	def test_get(self):
		response = self.client.get(self.url)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.context.get('veiculos')), 1)

class TestesViewCriarVeiculos(TestCase):
	def setUp(self):
		self.user = User.objects.create(username='teste', password='12345@teste')
		self.client.force_login(self.user)
		self.url = reverse('criar-veiculos')
	
	def test_get(self):
		response = self.client.get(self.url)
		self.assertEqual(response.status_code, 200)
		self.assertIsInstance(response.context.get('form'), FormularioVeiculo)
	
	def test_post(self):
		data = {'marca': 1, 'modelo': 'ABCDE', 'ano': 2, 'cor': 3, 'combustivel': 4}
		response = self.client.post(self.url, data)

		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, reverse('listar-veiculos'))

		self.assertEqual(Veiculo.objects.count(), 1)
		self.assertEqual(Veiculo.objects.first().modelo, 'ABCDE')

class TestesViewEditarVeiculos(TestCase):
	def setUp(self):
		self.user = User.objects.create(username='teste', password='12345@teste')
		self.client.force_login(self.user)
		self.instancia = Veiculo.objects.create(marca=1, modelo='ABCDE', ano=2, cor=3, combustivel=4)
		self.url = reverse('editar-veiculos', kwargs={'pk': self.instancia.pk})
	
	def test_get(self):
		response = self.client.get(self.url)
		self.assertEqual(response.status_code, 200)
		self.assertIsInstance(response.context.get('object'), Veiculo)
		self.assertIsInstance(response.context.get('form'), FormularioVeiculo)
		self.assertEqual(response.context.get('object').pk, self.instancia.pk)
		self.assertEqual(response.context.get('object').marca, self.instancia.marca)
	
	def test_post(self):
		data = {'marca': 5, 'modelo': 'FGHIJ', 'ano': 4, 'cor': 2, 'combustivel': 1}
		response = self.client.post(self.url, data)

		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, reverse('listar-veiculos'))

		self.assertEqual(Veiculo.objects.count(), 1)
		self.assertEqual(Veiculo.objects.first().marca, 5)
		self.assertEqual(Veiculo.objects.first().pk, self.instancia.pk)
