from django.db import models


# Create your models here.
class Posteo(models.Model):
    titulo = models.CharField(max_length=90)
    texto = models.CharField(max_length=254)
    

class PostNoticias(models.Model):
    titulo = models.CharField(max_length=90)
    sub_titulo = models.CharField(max_length=90)
    fecha = models.DateField()
    texto = models.CharField(max_length=254)

class PostCriticas(models.Model):
    titulo = models.CharField(max_length=90)
    sub_titulo = models.CharField(max_length=90)
    fecha = models.DateField()
    texto = models.CharField(max_length=254)
