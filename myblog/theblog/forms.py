from django import forms
from .models import Post, Category
from django.utils.functional import lazy

#cats = [('codigo', 'codigo'), ('deportes', 'deportes'), ('entretenimiento', 'entretenimiento'),]




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'titulo_tag', 'autor', 'categoria' ,'articulo', 'header_image')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'elder', 'type': 'hidden'}),
            #'autor': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select( attrs={'class': 'form-control'}),
            'articulo': forms.Textarea(attrs={'class': 'form-control'}),


        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'titulo_tag', 'articulo')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'articulo': forms.Textarea(attrs={'class': 'form-control'}),

        }