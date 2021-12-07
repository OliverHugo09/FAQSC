from django.db import models
from django.contrib.auth.models import Group
from ckeditor.fields import RichTextField


#Modelos FAQ
'''Buscar el modelo de categorias y verificar si ya existe, si no crearlo'''
class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    categoria = models.CharField(max_length=50)
    departamento = models.ManyToManyField(Group)

    def __str__(self):
        return self.categoria

class FAQ(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length = 50)
    
    '''Verificar que libreria usan para las descripciones'''
    descripcion = RichTextField(blank=True, null=True)
    
    '''Buscar el modelo de las categorias si ya esta creado'''
    categorias = models.ForeignKey(Categoria, null=True, on_delete=models.SET_NULL,related_name='categoria_name')
    
    '''Buscar que modelo se relaciona al canal de venta con el usuario'''
    departamento = models.ManyToManyField(Group, related_name='grupo_departamento')

    def __str__(self):
        return self.titulo
