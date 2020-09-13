from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm, EditForm

class HomeView(ListView):
    model = Post
    template_name = 'index.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'detalle_articulo.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'añadir_post.html'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'actualizar_post.html'
    #fields = ['titulo', 'titulo_tag', 'articulo']