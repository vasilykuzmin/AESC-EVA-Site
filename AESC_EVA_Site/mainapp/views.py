from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/index.html', context={})


def rickroll(request):
    return render(request, 'mainapp/rickroll.html', context={})


def posters(request):
    return render(request, 'mainapp/posters.html', context={})

def wiki(request):
    return render(request, 'mainapp/wiki.html', context={})

def rock(request):
    return render(request, 'mainapp/rock.html', context={})

def authors(request):
    return render(request, 'mainapp/authors.html', context={})