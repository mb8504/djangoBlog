from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

posts = [
    {
        'author': 'MikeyB',
        'title': 'Blog post 1',
        'content': 'March 25, 2024',
    },
    {
        'author': 'TraveyB',
        'title': 'My Blog Post',
        'content': 'March 25, 2024',
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})





