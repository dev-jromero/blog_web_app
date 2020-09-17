from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        #return reverse('detalle_articulo', args=(str(self.id)))
        return reverse('home')

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    titulo_tag = models.CharField(max_length=255, default="")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    articulo = RichTextField(blank=True, null=True)
    #articulo = models.TextField()
    fecha_publicacion = models.DateField(auto_now_add=True)
    categoria = models.CharField(max_length=255, default='codigo')
    snippet = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)

    def get_absolute_url(self):
        #return reverse('detalle_articulo', args=(str(self.id)))
        return reverse('home')
