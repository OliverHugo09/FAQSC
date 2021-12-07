from django.db import models
from django.contrib.auth.models import Group
from ckeditor.fields import RichTextField


#Modelos FAQ
class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    categoria = models.CharField(max_length=50)
    departamento = models.ManyToManyField(Group)

    def __str__(self):
        return self.categoria

class FAQ(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length = 50)
    descripcion = RichTextField(blank=True, null=True)
    categorias = models.ForeignKey(Categoria, null=True, on_delete=models.SET_NULL,related_name='categoria_name')
    departamento = models.ManyToManyField(Group, related_name='grupo_departamento')

    def __str__(self):
        return self.titulo

#Generador de tokens

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)