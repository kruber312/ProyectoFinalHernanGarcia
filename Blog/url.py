from django.urls import path
from Blog.views import crear_pagina, ver_paginas, vista_pagina

urlpatterns = [
    path('crear_pagina/',crear_pagina,name="crearPagina"),
    path('ver_pagina/',ver_paginas,name="verPagina"),
    path('pagina/<codigo>',vista_pagina,name="pagina"),
]
