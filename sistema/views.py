from django.conf import settings
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

class Login(View):
    """
    """
    def get(self, request):
        contexto = {'mensagem': ''}
        if request.user.is_authenticated:
            return redirect('/veiculo')
        else:
            return render(request, 'autenticacao.html', contexto)

    def post(self, request):
        nome = request.POST.get('nome', None)
        senha = request.POST.get('senha', None)
        
        usuario = authenticate(request, username=nome, password=senha)
        if usuario is not None:
            if usuario.is_active:
                login(request, usuario)
                return redirect("/veiculo")
            return render(request, 'autenticacao.html', {'mensagem': 'Usuário inativo.'})
        return render(request, 'autenticacao.html', {'mensagem': 'Usuário ou senha inválidos.'})

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(settings.LOGIN_URL)