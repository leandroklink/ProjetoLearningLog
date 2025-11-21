from django.shortcuts import render, get_object_or_404, redirect
from .models import Topic, Entry 
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect, Http404 #http404 é uma página padrão do django quando o caminho não é encontrado
from django.urls import reverse
from django.contrib.auth.decorators import login_required # isso é um decorator, é uma forma simples de alterar um comportamento de uma função sem a necessidade de modificar seu código

def index(request):
    """página principal do learning_logs"""
    return render(request, 'learning_logs/index.html')


@login_required # leva a página de login se não estiver com o usuário logado, conforme a importação logo acima chamada login_required
def topics(request):
    """Mostra todos os assuntos"""
    topics = Topic.objects.filter(owner=request.user).order_by("date_added") # o filter está filtrando apenas os topics com o ID do user
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Mostra um único assunto e todas as suas entradas"""
    topic = Topic.objects.get(id = topic_id)

    #Garante que o assunto pertence ao usuário atual
    if topic.owner != request.user:
        raise Http404 #leva o usuário a página 404 se ele tentar acessar um tópico que ele não é dono

    entries = topic.entry_set.order_by("-date_added") #ordem do mais recente pro mais antigo
    context = {'topic': topic, "entries": entries}
    return render (request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Adiciona um novo assunto"""
    if request.method != 'POST':
        #nenhum dado submetido, cria um formulario em branco
        form = TopicForm()
    else:
        #Dados de post submetidos, processa os dados.
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse("topics"))#reverse usa o nome da url, em urls.py, pra enviar onde quer mandar
    
    context = {'form': form}
    return render(request, "learning_logs/new_topic.html", context)

@login_required
def new_entry(request, topic_id):
    """Acrescenta uma nova entrada para um assunto particular"""
    topic = Topic.objects.get(id=topic_id)

    #Garante que o assunto pertence ao usuário atual
    if topic.owner != request.user:
        raise Http404 #leva o usuário a página 404 se ele tentar acessar um tópico que ele não é dono
    
    if request.method != 'POST':
        #nenhum dado submetido, cria um formulário em branco
        form = EntryForm()
    else:
        #Dados de POST submetidos, processa os dados
        form = EntryForm(data = request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic 
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
        
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edita uma entrada existente"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

        #Garante que o assunto pertence ao usuário atual
    if topic.owner != request.user:
        raise Http404 #leva o usuário a página 404 se ele tentar acessar um tópico que ele não é dono

    if request.method != 'POST':
        #requesição inicial, preenche previamento o formulário
        form = EntryForm(instance=entry)
    else:
        #dados de post submetidos, processa os dados.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid(): #valida se o formulário está ok
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))
        # redirecionamento para topic
        
    context = {"entry": entry, "topic": topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

@login_required
def delete_entry(request, entry_id):
    """Excluir entry existente"""

    entry_del = get_object_or_404(Entry, id=entry_id)
    topic = entry_del.topic

    if topic.owner != request.user:
        raise Http404

    if request.method == 'POST':
        entry_del.delete()
        return HttpResponseRedirect(reverse('topic', args=[topic.id]))
    
    context = {"entry": entry_del, "topic": topic}
    return render(request, 'learning_logs/delete_entry.html', context)