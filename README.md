# PROJETO PYTHON E DJANGO -- REGISTROS DE APRENDIZAGEM

Este é o meu primeiro projeto desenvolvido com Django. O trabalho foi
realizado acompanhando as aulas do Jefferson Lobato:
https://www.youtube.com/@JeffersonLobato

A estrutura geral segue o projeto apresentado no curso, porém fiz
algumas melhorias visuais básicas e implementei a funcionalidade de
exclusão de entradas.

## Funcionalidades

-   Cadastro de tópicos.
-   Adição de entradas dentro de cada tópico.
-   Edição e exclusão de entradas.
-   Sistema de autenticação com registro e login.
-   Cada usuário só pode visualizar, editar ou excluir seus próprios
    tópicos e entradas.

## Tecnologias Utilizadas

-   Python 3.13.5
-   Django 4.2
-   Bootstrap 3

## Como rodar o projeto

Clone o repositório: git clone
https://github.com/seu-usuario/seu-repositorio.git cd seu-repositorio

Crie o ambiente virtual: python -m venv venv

Ative o ambiente virtual: Windows: venv`\Scripts`{=tex}`\activate`{=tex}
Linux/Mac: source venv/bin/activate

Instale as dependências: pip install -r requirements.txt

Execute as migrações: python manage.py migrate

Inicie o servidor: python manage.py runserver

Acesse no navegador: http://127.0.0.1:8000
