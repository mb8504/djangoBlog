from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Post, PostCategory

# Create your views here.
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
    template_name = 'blog/post_details.html'


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def CategoryView(request, category_name):
    try:
        category = PostCategory.objects.get(category=category_name.upper())
        category_posts = Post.objects.filter(category=category)
        return render(request, 'blog/categories.html', {'category_posts': category_posts, 'category_name': category_name})
    except PostCategory.DoesNotExist:
        return render(request, 'category_not_found.html', {'category_name': category_name})












# def my_view(request):
#     # Get the username of the logged-in user
#     username = request.user.username if request.user.is_authenticated else None
#     # Pass the username to the template context
#     return render(request, 'base.html', {'username': username})



