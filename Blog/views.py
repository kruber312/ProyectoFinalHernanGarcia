from django.shortcuts import render, redirect
from Blog.forms import paginaForm
from django.contrib.auth.decorators import login_required
from Blog.models import pagina
from datetime import date

# Create your views here.
@login_required
def crear_pagina(request):
    if request.method == "POST":
        pag = paginaForm(request.POST)
        if pag.is_valid():
            info = pag.cleaned_data
            info_save = pagina(
                titulo=info["titulo"],
                subtitulo=info["subtitulo"],
                cuerpo=info["cuerpo"],
                autor=request.user,
                fecha=date.today(),
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
    pass