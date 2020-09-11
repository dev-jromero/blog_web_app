from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    titulo_tag = models.CharField(max_length=255, default="")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    articulo = models.TextField()

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)