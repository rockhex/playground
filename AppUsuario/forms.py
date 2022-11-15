from django import forms

class PosteoForm(forms.Form):
    
    titulo = forms.CharField(max_length=40)
    texto = forms.CharField(max_length=400)
    

class PostearForm(forms.Form):

    titulo = forms.CharField(max_length=40)
    texto = forms.CharField(max_length=400)  
    nombre = forms.CharField(max_length=40)
    fecha = forms.DateField() 


