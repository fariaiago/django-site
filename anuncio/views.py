from django.shortcuts import render
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from anuncio.models import Anuncio
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import FileResponse, Http404
from django.urls import reverse_lazy
from anuncio.forms import FormularioAnuncio

class ListarAnuncios(LoginRequiredMixin, ListView):
	model = Anuncio
	context_object_name = 'anuncios'
	template_name = 'anuncio/listar.html'

class CriarAnuncios(LoginRequiredMixin, CreateView):
	model = Anuncio
	form_class = FormularioAnuncio
	template_name = 'anuncio/novo.html'
	success_url = reverse_lazy('listar-anuncios')

class EditarAnuncios(LoginRequiredMixin, UpdateView):
    model = Anuncio
    form_class = FormularioAnuncio
    template_name = 'anuncio/editar.html'
    success_url = reverse_lazy('listar-anuncios')

class DeletarAnuncios(LoginRequiredMixin, DeleteView):
    model = Anuncio
    template_name = 'anuncio/deletar.html'
    success_url = reverse_lazy('listar-anuncios')
