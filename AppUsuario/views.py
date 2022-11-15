from django.shortcuts import render
from django.http import HttpResponse
from .models import Posteo
from .forms import PosteoForm

# Create your views here.

def mostrar_index(request):
    return render(request,'index.html')

def mostrar_gallery(request):
    return render(request,'gallery.html')
    
def mostrar_contact(request):
    
    return render(request,'contact.html')

def crear_posteo(request):

    if request.method == 'POST':

        posteo = PosteoForm(request.POST)
        
        print('posteo')

        if posteo.is_valid():

            data = posteo.cleaned_data


            posteo = Posteo (titulo=data['titulo'], texto=data['texto'])
    
            posteo.save()
            print('posteo jajaj XD')
            return render(request,'index.html')

    else :
        posteo = PosteoForm()
        print('posteo estamos en la B')





    return render(request,'crear_posteo.html', {'posteo':posteo})


def buscador (request):
    if request.GET.get ('posteo', False):
        posteo = request.GET ['posteo']
        posteo = posteo.objects.filter(posteo__icontains=posteo)

        return render (request, 'buscador.html',{'posteo':posteo})
        
    else:
        respuesta = 'no hay datos'


    return render (request, 'buscador.html',{'respuesta':respuesta})

