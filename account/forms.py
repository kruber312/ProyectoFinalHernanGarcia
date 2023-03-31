from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    imagen = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ("username", "email")

class UserEditForm(UserChangeForm):
    email = forms.EmailField(required=False)
    imagen = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ("email", "imagen")
