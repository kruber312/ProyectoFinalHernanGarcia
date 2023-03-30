from django.urls import path
from Blog.views import crear_pagina

urlpatterns = [
    path('crear_pagina',crear_pagina,name="crearPagina"),
]
