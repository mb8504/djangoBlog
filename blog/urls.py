from django.urls import path
from .views import PostListView, PostDetailView, CategoryView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<slug:title>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='blog-contact'),
    path('category/<str:category_name>/', CategoryView, name='category'),
]