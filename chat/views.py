from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Sala


def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        
        sala = Sala.objects.filter(nome=nome).filter(senha=senha)
        
        if not sala:
            return HttpResponse('sala ou senha invalida')
        return render(request, 'chat.html', {'nome': nome})
