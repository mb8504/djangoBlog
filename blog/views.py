from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Post
# Create your views here.

# posts = [
#     {
#         'author': 'MikeyB',
#         'title': 'Blog post 1',
#         'content': 'March 25, 2024',
#     },
#     {
#         'author': 'TraveyB',
#         'title': 'My Blog Post',
#         'content': 'March 25, 2024',
#     }
# ]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})












def my_view(request):
    # Get the username of the logged-in user
    username = request.user.username if request.user.is_authenticated else None
    # Pass the username to the template context
    return render(request, 'base.html', {'username': username})



