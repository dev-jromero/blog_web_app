from django.urls import path
from .views import HomeView, ArticleDetailView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('articulo/<pk>', ArticleDetailView.as_view(), name='detalle_articulo')
]