from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from account.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from account.models import Avatar

# Create your views here.
@login_required
def editar_usuario(request):
    user = request.user
    if request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            info = form.cleaned_data
            user.username = info["username"]
            user.email = info["email"]
            try:
                user.avatar.imagen = info["imagen"]
            except:
                avatar = Avatar(user=user, imagen=info["imagen"])
                avatar.save()
            user.save()
            return redirect("accountLogin")


    form = UserRegisterForm(initial={
        "username": user.username,
        "email": user.email
    })


    context= {
        "form": form,
        "titulo": "Editar Usuario",
        "boton": "Editar"
    }

    return render(request, "form.html", context=context)
def register_account(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("accountLogin")
    form = UserRegisterForm()
    context= {
        "form": form,
        "titulo": "Registrar Usuario",
        "boton": "Crear Usuario"
    }
    return render(request, "form.html", context=context)


def login_account(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            info = form.cleaned_data
            user = authenticate(username=info['username'],password=info['password'])
            if user is not None:
                login(request, user)
                return render(request, "base.html", context={"mensajes":["Logueado Correctamente"]})
            else:
                return render(request, "base.html", context={"mensajes":["Logueado No Correcto"]})

    form = AuthenticationForm()
    context= {
        "form": form,
        "titulo": "Loguear Usuario",
        "boton": "LogIn"
    }
    return render(request, "form.html", context=context)

