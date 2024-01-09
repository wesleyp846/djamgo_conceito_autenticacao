from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    # senaõ é POST não veio por formulario, é get
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        return HttpResponse(f'username: {username} password: {password}')