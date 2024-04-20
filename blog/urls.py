from django.urls import path
from .views import PostListView, PostDetailView, CategoryView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='blog-about'),
    path('category/<str:category_name>/', CategoryView, name='category'),
]