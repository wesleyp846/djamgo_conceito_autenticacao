from django.shortcuts import render
from django.http import HttpResponse
# Importação para poder usar o objeto User do Django
from django.contrib.auth.models import User
# Importação para poder usar o objeto authenticate do Django
from django.contrib.auth import authenticate
#importamos com o apelido porque temos uma função com o mesmo nome do importe
from django.contrib.auth import login as auth_login
# Importação para poder usar os decoradores login_required
from django.contrib.auth.decorators import login_required
#from django.shortcuts import redirect

def cadastro(request):
    # senaõ é POST não veio por formulario, é get
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        #dentro da variável estão todos os usuarios com o username informado
        user = User.objects.filter(username=username).first()

        # se o user existir, sinal de que ja tem algem cadastrado com este nome
        if user:
            return HttpResponse('Ja existe um usuario com este nome')
        
        # cria o novo user
        user=User.objects.create_user(username=username, password=password)
        user.save()

        return HttpResponse(f'username: {username}  cadastrado com sucesso')
    
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponse(f'Login efetuado com sucesso')
        else:
            return HttpResponse('Login falhou')

@login_required(login_url='/auth/login/')     
def plataforma(request):
    return HttpResponse('Plataforma')
    ### SE NÃO TIVESSE DECORADORES TERIA QUE DIGATITAR TUDO ISSO
    # # se o user estiver autenticado ele autorisa ver o conteudo
    # if request.user.is_authenticated:
    #     return HttpResponse('Plataforma')
    # else:
    #     return HttpResponse('você precisa estar logado para ver esta página')