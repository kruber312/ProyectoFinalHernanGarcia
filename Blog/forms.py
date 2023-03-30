from django import forms
class paginaForm(forms.Form):
    titulo = forms.CharField(max_length=40)
    subtitulo = forms.CharField(max_length=40,required=False)
    cuerpo = forms.CharField(max_length=255)
    imagen = forms.ImageField(required=False)