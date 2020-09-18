from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-fecha_publicacion']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'lista_categoria.html', {'cat_menu_list':cat_menu_list})

def CategoryView(request, cats):
    category_posts = Post.objects.filter(categoria__nombre=cats.replace('-', ' '))
    return render(request, 'categoria.html', {'cats':cats.title().replace('-', ' '), 'category_posts':category_posts })

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'detalle_articulo.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'añadir_post.html'

class AddCategoryView(CreateView):
    model = Category
    template_name = 'añadir_categoria.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'actualizar_post.html'
    #fields = ['titulo', 'titulo_tag', 'articulo']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'eliminar_post.html'
    success_url = reverse_lazy('home')