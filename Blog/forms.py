from django import forms
class paginaForm(forms.Form):
    titulo = forms.CharField(max_length=40)
    subtitulo = forms.CharField(max_length=40,required=False)
    cuerpo = forms.CharField()
    imagen = forms.ImageField(required=False)

class commentForm(forms.Form):
    cuerpo = forms.CharField()

class messageForm(forms.Form):
    para = forms.CharField(max_length=40)
    cuerpo = forms.CharField()
