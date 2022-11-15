
from django.contrib import admin
from django.urls import path

from .views import mostrar_contact, mostrar_gallery, mostrar_index, crear_posteo, buscador

urlpatterns = [
    

    path('',mostrar_index),
    path('mostrar_gallery/', mostrar_gallery, name='galeria'),
    path('mostrar_contact', mostrar_contact, name='contacto'),
    path('crear_posteo/', crear_posteo, name = 'crear_posteo'),
    path('buscador/', buscador, name = 'buscador'),
]
