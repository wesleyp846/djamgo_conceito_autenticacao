# Documentação da Aplicação Django Conceito de Autenticação

video https://www.youtube.com/watch?v=gdhiA6wObw0&list=PLCxYb_kl1FLaVvULMOXthDa9DP5-anT7A&index=2

docunemtação = https://docs.djangoproject.com/en/5.0/topics/auth/default/#user-objects

Introdução
Bem-vindo à documentação da aplicação Django Auth, desenvolvida por Wesley Pereira. Esta aplicação é um sistema web para cadastro de usuários, implementando autenticação e registro de usuários de forma segura e profissional utilizando o framework Django.

Versão Atual: v1.0
Na versão v1.0, a aplicação concentra-se na implementação do backend, proporcionando um sistema de autenticação e registro de usuários básico e seguro.

Pré-requisitos
Python 3.9 ou superior.
Bibliotecas Utilizadas
Django: Framework web utilizado para o desenvolvimento da aplicação.
SQLite: Sistema de gerenciamento de banco de dados utilizado para armazenar os dados da aplicação.
Funcionalidades
Cadastro de novos usuários com nome e senha.
Armazenamento dos dados em um banco de dados SQLite.
Pré-configuração
Ambiente Virtual
Execute os seguintes comandos via terminal para criar e ativar um ambiente virtual:

bash
Copy code
python -m venv env
.\env\Scripts\activate
Instalação de Bibliotecas
bash
Copy code
python -m pip install --upgrade pip
pip install django
Configuração do Projeto
Criação do Projeto atenticacao
bash
Copy code
django-admin startproject atenticacao .
Configuração de settings.py
Em django_auth/settings.py, configure o projeto:

python
Copy code

# Aplicações instaladas
INSTALLED_APPS = [
    'usuarios'
]

Adicione a rota do Allauth em urls.py:

python
Copy code
# Em urls.py
path('accounts/', include('usuarios.urls')),
Execute migrações e crie um superusuário:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
Inicie o servidor:

bash
Copy code
python manage.py runserver
Acesse http://127.0.0.1:8000/accounts/login/ para verificar a instalação bem-sucedida.


Implementação
O projeto utiliza o framework Django. O código inicial foi baseado no canal Paythonando, com documentação e melhorias adicionadas por Wesley Pereira.

Créditos
Código inicial baseado no canal Paythonando.
Documentação e melhorias por Wesley Pereira.
Licença
MIT

Esperamos que esta documentação ajude você a compreender a aplicação. Fique à vontade para contribuir e melhorar. Para mais informações, visite o LinkedIn de Wesley Pereira.

para a versão 1.5V
Personalização do Frontend
Personalizar as páginas HTML e um modelo BASE.HTML, siga estas etapas:

Em settings.py, adicione o diretório de templates:

python
Copy code
import os

'DIRS' = [os.path.join(BASE_DIR, 'templates')]
Crie uma pasta chamada templates na raiz do projeto.

Copie os diretórios account e openid de env/lib/allauth/templates/ para templates.

Personalize os arquivos HTML conforme necessário.
