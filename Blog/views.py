# Importar las librerías necesarias
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from Blog.forms import paginaForm, commentForm, messageForm
from django.contrib.auth.decorators import login_required
from Blog.models import Pagina, Comment, Message
from datetime import datetime

# Vista para crear una página
@login_required
def crear_pagina(request):
    # Si se recibe un POST en el request
    if request.method == "POST":
        # Se crea un objeto formulario de página con los datos recibidos en el request
        pag = paginaForm(request.POST, request.FILES)
        # Si el formulario es válido
        if pag.is_valid():
            # Se guarda la información del formulario en un objeto Pagina
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
            # Se redirige a la página recién creada
            return redirect("pagina",info_save.id)

    # Si el request no es un POST, se muestra el formulario vacío
    form = paginaForm()
    context = {
        "form": form,
        "titulo": "Crear Pagina",
        "boton": "Crear",
    }
    return render(request, "form.html", context=context)


# Vista para ver las últimas páginas creadas
def ver_paginas(request):
    paginas = Pagina.objects.order_by('-fecha')[:9]
    context = {
        "paginas" : paginas,
        "titulo":"Ultimas paginas"
    }
    return render(request, "blog/ver_paginas.html", context=context)


# Vista para filtrar las páginas creadas por un usuario específico
def filter_paginas_usuario(request, usuario):
    paginas = Pagina.objects.filter(autor__username__iexact=usuario)
    if paginas:
        context = {
            "paginas" : paginas,
            "titulo": f"Posts de {usuario}"
        }
        return render(request, "blog/ver_paginas.html", context=context)
    else:
        context = {"mensajes": ["Esa pagina no existe"]}
        return render(request, "error.html",context=context)

def vista_pagina(request,codigo):
    if request.user.is_authenticated:
        # Si el usuario está autenticado, se busca la página con el id proporcionado.
        try:
            pag = Pagina.objects.get(id=codigo)
        except:
            # Si la página no existe, se muestra un mensaje de error.
            context = {"mensajes": ["Esa pagina no existe"]}
            return render(request, "error.html", context=context)
        # Se crea un formulario para añadir comentarios a la página.
        form = commentForm()
        # Si se envió un comentario por POST, se procesa y se guarda en la base de datos.
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
        # Se obtienen los comentarios de la página y se ordenan por fecha descendente.
        comentarios = Comment.objects.filter(page_id=pag.id)
        comentarios = comentarios.order_by('-fecha')
        # Se crea un contexto con la página, el formulario de comentarios y los comentarios obtenidos.
        context = {
            "pagina": pag,
            "form": form,
            "titulo": "Escribir Comentario",
            "boton": "Comentar",
            "comentarios": comentarios
        }
        # Se muestra la página con los comentarios y el formulario.
        return render(request, "blog/pagina.html", context=context)
    else:
        # Si el usuario no está autenticado, se muestra un mensaje de error.
        context = {"mensajes": ["Por favor Logueate para ver las paginas"]}
        return render(request, "error.html",context=context)

def comentario(request,pag):
    # Si se envió un comentario por POST, se procesa y se guarda en la base de datos.
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
            # Se redirige a la página de creación de páginas una vez que se ha guardado el comentario.
            return redirect("crearPagina")
    # Se crea un formulario para añadir comentarios a la página.
    form = commentForm()
    # Se crea un contexto con el formulario y la página a la que se quiere añadir el comentario.
    context = {
        "form": form,
        "titulo": "Escribir Comentario",
        "boton": "Comentar",
        "pagina": pag
    }
    # Se muestra el formulario para añadir el comentario.
    return render(request, "form.html", context=context)

def mensajes(request):
    # Se obtienen los mensajes que se han enviado al usuario logueado.
    mensajes_para = Message.objects.filter(para=request.user)
    # Se crea un contexto con los mensajes obtenidos.
    context = {
        "msg" : mensajes_para,
        "titulo": f"Mensajes de {request.user.username}"
    }
    # Se muestra la página con los mensajes recibidos.
    return render(request, "blog/mensajes.html", context=context)

# Vista para crear un nuevo mensaje
def mensaje_nuevo(request, para = ""):
    if request.method == "POST":
        msg = messageForm(request.POST)  # Se crea un formulario con los datos recibidos en el POST
        if msg.is_valid():  # Se comprueba si el formulario es válido
            info = msg.cleaned_data  # Se obtienen los datos limpios del formulario
            try:
                # Se crea un nuevo mensaje a partir de los datos del formulario y se guarda en la BD
                info_save = Message(
                    cuerpo=info["cuerpo"],
                    de=request.user,
                    fecha=datetime.now(),
                    para=User.objects.get(username__iexact=info["para"]),
                )
                info_save.save()
                return redirect("mensajes")  # Si se ha creado el mensaje correctamente se redirige al usuario a su bandeja de entrada
            except User.DoesNotExist:  # Si el usuario al que se intenta enviar el mensaje no existe, se muestra un mensaje de error
                context = {
                    "mensajes": ["El usuario no existe"],
                }
            return render(request, "error.html", context=context)  # Se renderiza la plantilla de error con el mensaje correspondiente
    form = messageForm(initial={  # Se crea un nuevo formulario con el nombre del destinatario ya relleno (si se ha pasado como parámetro)
        "para":para
    })
    context = {  # Se crea el contexto con el formulario y los datos necesarios para renderizar la plantilla de creación de mensajes
        "form": form,
        "titulo":"Escribir Mensaje",
        "boton": "Enviar",
    }
    return render(request, "form.html", context=context)  # Se renderiza la plantilla de creación de mensajes
