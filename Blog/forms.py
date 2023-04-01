from django import forms
class paginaForm(forms.Form):
    titulo = forms.CharField(label="Titulo",max_length=40)
    subtitulo = forms.CharField(label="Subtitulo",max_length=40,required=False)
    cuerpo = forms.CharField(label="",widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))
    imagen = forms.ImageField(label="Incluir una imagen:",required=False)

class commentForm(forms.Form):
    cuerpo = forms.CharField(label="",widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}))

class messageForm(forms.Form):
    para = forms.CharField(label="Para:",max_length=40)
    cuerpo = forms.CharField(label="",widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}))
