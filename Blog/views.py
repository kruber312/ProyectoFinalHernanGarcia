from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from Blog.forms import paginaForm, commentForm, messageForm
from django.contrib.auth.decorators import login_required
from Blog.models import Pagina, Comment, Message
from datetime import datetime

# Create your views here.
@login_required
def crear_pagina(request):
    if request.method == "POST":
        pag = paginaForm(request.POST, request.FILES)
        if pag.is_valid():
            info = pag.cleaned_data
            info_save = Pagina(
                titulo=info["titulo"],
                subtitulo=info["subtitulo"],
                cuerpo=info["cuerpo"],
                autor=request.user,
                fecha=datetime.now(),
                imagen=info["imagen"]
            )
            info_save.save()
            return redirect("crearPagina")

    form = paginaForm()
    context = {
        "form": form,
        "titulo": "Crear Pagina",
        "boton": "Crear",
    }
    return render(request, "form.html", context=context)


def ver_paginas(request):
    paginas = Pagina.objects.order_by('-fecha')[:9]
    context = {
        "paginas" : paginas
    }
    return render(request, "blog/ver_paginas.html", context=context)

def filter_paginas_usuario(request, usuario):
    paginas = Pagina.objects.filter(autor__username__iexact=usuario)
    context = {
        "paginas" : paginas,
        "titulo": f"Posts de {usuario}"
    }
    return render(request, "blog/ver_paginas.html", context=context)

def vista_pagina(request,codigo):
    if request.user.is_authenticated:
        pag = Pagina.objects.get(id=codigo)
        form = commentForm()
        if request.method == "POST":
            com = commentForm(request.POST)
            if com.is_valid():
                info = com.cleaned_data
                info_save = Comment(
                    cuerpo=info["cuerpo"],
                    autor=request.user,
                    fecha=datetime.now(),
                    page=pag,
                )
                info_save.save()
        comentarios = Comment.objects.filter(page_id=pag.id)
        comentarios = comentarios.order_by('-fecha')

        context = {
            "pagina": pag,
            "form": form,
            "titulo": "Escribir Comentario",
            "boton": "Comentar",
            "comentarios": comentarios
        }
        return render(request, "blog/pagina.html", context=context)
    else:
        context = {"mensajes": ["Por favor Logueate para ver las paginas"]}
        return render(request, "error.html",context=context)
def comentario(request,pag):
    if request.method == "POST":
        com = commentForm(request.POST)
        if com.is_valid():
            info = com.cleaned_data
            info_save = Comment(
                cuerpo=info["cuerpo"],
                autor=request.user,
                fecha=datetime.now(),
                page=pag,
            )
            info_save.save()
            return redirect("crearPagina")

    form = commentForm()
    context = {
        "form": form,
        "titulo": "Escribir Comentario",
        "boton": "Comentar",
        "pagina": pag
    }
    return render(request, "form.html", context=context)

def mensajes(request):
    mensajes_para = Message.objects.filter(para=request.user)
    print(mensajes_para)
    context = {
        "msg" : mensajes_para,
        "titulo": f"Mensajes de {request.user.username}"
    }
    return render(request, "blog/mensajes.html", context=context)

def mensaje_nuevo(request):
    if request.method == "POST":
        msg = messageForm(request.POST)
        if msg.is_valid():
            info = msg.cleaned_data
            try:
                info_save = Message(
                    cuerpo=info["cuerpo"],
                    de=request.user,
                    fecha=datetime.now(),
                    para=User.objects.get(username__iexact=info["para"]),
                )
                info_save.save()
                return redirect("mensajes")
            except User.DoesNotExist:
                context = {
                    "mensajes": ["El usuario no existe"],
                }
            return render(request, "error.html", context=context)
    form = messageForm()
    context = {
        "form": form,
        "titulo":"Escribir Mensaje",
        "boton": "Enviar",
    }
    return render(request, "form.html", context=context)