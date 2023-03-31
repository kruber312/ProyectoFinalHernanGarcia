from django.urls import path
from Blog.views import crear_pagina,mensajes,mensaje_nuevo, ver_paginas, vista_pagina,comentario, filter_paginas_usuario

urlpatterns = [
    path('crear_pagina/',crear_pagina,name="crearPagina"),
    path('ver_pagina/',ver_paginas,name="verPagina"),
    path('pagina/<codigo>',vista_pagina,name="pagina"),
    path('pagina/comment/<pag>',comentario,name="comentar"),
    path('ver_pagina/<usuario>',filter_paginas_usuario,name="verPaginasUsuario"),
    path('mensajes',mensajes,name="mensajes"),
    path('mensajes_nuevo',mensaje_nuevo,name="nuevoMensaje"),
]
