from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Post, PostCategory
from django.utils.text import Truncator

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
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Iterate through each post and extract the first sentence
        for post in context['posts']:
            # Use Truncator to truncate the content to the first sentence
            first_sentence = Truncator(post.content).chars(
                150, html=True, truncate='...'
            )
            # Add the first sentence to the post object
            post.first_sentence = first_sentence
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_details.html'
    slug_field = 'path'  # Specify the field containing the slug
    slug_url_kwarg = 'title'  # Specify the URL keyword argument for the slug


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def CategoryView(request, category_name):
    try:
        category = PostCategory.objects.get(category=category_name.upper())
        category_posts = Post.objects.filter(category=category)
        return render(request, 'blog/categories.html', {'category_posts': category_posts, 'category_name': category_name})
    except PostCategory.DoesNotExist:
        return render(request, 'category_not_found.html', {'category_name': category_name})
