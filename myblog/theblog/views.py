from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class HomeView(ListView):
    model = Post
    template_name = 'index.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'detalle_articulo.html'