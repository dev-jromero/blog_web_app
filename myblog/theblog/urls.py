from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, AddCategoryView, UpdatePostView, DeletePostView, CategoryView, CategoryListView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('articulo/<pk>', ArticleDetailView.as_view(), name='detalle_articulo'),
    path('add_post/', AddPostView.as_view(), name='añadir_post'),
    path('add_category/', AddCategoryView.as_view(), name='añadir_categoria'),
    path('articulo/editar/<int:pk>', UpdatePostView.as_view(), name='actualizar_post'),
    path('articulo/<int:pk>/eliminar', DeletePostView.as_view(), name='eliminar_post'),
    path('category/<str:cats>/', CategoryView, name='categoria'),
    path('category-list/', CategoryListView, name='lista-categoria'),
]