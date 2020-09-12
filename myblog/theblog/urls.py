from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('articulo/<pk>', ArticleDetailView.as_view(), name='detalle_articulo'),
    path('add_post/', AddPostView.as_view(), name='añadir_post')

]