from django.shortcuts import render
from .models import Post

posts = [
    {
        'autor': 'SzymonL',
        'tytul': 'pierwszy',
        'tresc': 'Pierwsza tresc',
        'data': 'Wrzesien 12'
    },
    {
        'autor': 'Jakub',
        'tytul': 'drugi',
        'tresc': 'Druga tresc',
        'data': 'Grudzien 12'

    }
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})

def kontakt(request):
    return render(request, 'blog/kontakt.html', {'title' : 'Kontakt'})