from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
    """Faz um logout do usuário."""
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    """Faz o cadastro de um novo usuário."""
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index')) #se estiver autenticado, não vai entrar na tela de registrar usuário e vai voltar automaticamente para index
    
    if request.method != 'POST':
        #exibe o formulário de cadastro em branco
        form = UserCreationForm()

    else:
        # processa o formulário preenchido
        form = UserCreationForm(data= request.POST)

        if form.is_valid():
            #faz o login do usuário e o redireciona para a página inicial, salvando na variável new_user e salvando com save() 
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password = request.POST["password1"]) # o authenticate pega o usuário e procura no banco se ele realmente existe e se realmente pode ser autenticado
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse("index"))
        
    context = {'form': form}
    return render(request, 'users/register.html', context)
