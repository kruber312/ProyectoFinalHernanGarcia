from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from account.forms import UserRegisterForm,UserEditForm
from django.contrib.auth.decorators import login_required
from account.models import Avatar

# Vista para editar la información del usuario
@login_required
def editar_usuario(request):
    user = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST, request.FILES)
        if form.is_valid():
            info = form.cleaned_data
            # Actualizar el nombre de usuario y el correo electrónico del usuario
            #user.username = info["username"]
            user.email = info["email"]
            # Actualizar la imagen de perfil del usuario si se proporcionó una nueva
            try:
                user.avatar.imagen = info["imagen"]
            except:
                avatar = Avatar(user=user, imagen=info["imagen"])
                avatar.save()
            user.save()
            return redirect("accountLogin")

    # Mostrar el formulario para editar la información del usuario
    form = UserEditForm(initial={
        "username": user.username,
        "email": user.email
    })
    context= {
        "form": form,
        "titulo": "Editar Usuario",
        "boton": "Editar"
    }
    return render(request, "form.html", context=context)

# Vista para registrar una cuenta de usuario
def register_account(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accountLogin")
    # Mostrar el formulario para registrar una cuenta de usuario
    form = UserRegisterForm
    context= {
        "form": form,
        "titulo": "Registrar Usuario",
        "boton": "Crear Usuario"
    }
    return render(request, "form.html", context=context)

# Vista para iniciar sesión en una cuenta de usuario
def login_account(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            info = form.cleaned_data
            # Verificar que el nombre de usuario y la contraseña proporcionados son válidos
            user = authenticate(username=info['username'],password=info['password'])
            if user is not None:
                login(request, user)
                return render(request, "base.html", context={"mensajes":["Logueado Correctamente"]})
            else:
                return render(request, "base.html", context={"mensajes":["Logueado No Correcto"]})

    # Mostrar el formulario para iniciar sesión en una cuenta de usuario
    form = AuthenticationForm()
    context= {
        "form": form,
        "titulo": "Loguear Usuario",
        "boton": "LogIn"
    }
    return render(request, "form.html", context=context)
