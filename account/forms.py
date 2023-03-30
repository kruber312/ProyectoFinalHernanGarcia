from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    imagen = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "imagen")

