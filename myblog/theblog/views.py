from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

class HomeView(ListView):
    model = Post
    template_name = 'index.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'detalle_articulo.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'añadir_post.html'
    fields = '__all__'