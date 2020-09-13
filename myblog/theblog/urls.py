from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('articulo/<pk>', ArticleDetailView.as_view(), name='detalle_articulo'),
    path('add_post/', AddPostView.as_view(), name='añadir_post'),
    path('articulo/editar/<int:pk>', UpdatePostView.as_view(), name='actualizar_post'),
    path('articulo/<int:pk>/eliminar', DeletePostView.as_view(), name='eliminar_post'),

]