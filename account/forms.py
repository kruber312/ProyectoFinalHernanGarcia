from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Ingrese su nombre de usuario", max_length=100)
    email = forms.EmailField(label="Ingrese su Correo",required=False)

    class Meta:
        model = User
        fields = ("username", "email")


class UserEditForm(UserChangeForm):

    email = forms.EmailField(label="Ingrese su Correo",required=False)
    imagen = forms.ImageField(label="Subir una Imagen de Avatar",required=False)
    password = forms.PasswordInput(render_value=False)

    class Meta:
        model = User
        fields = ("email", "imagen")

