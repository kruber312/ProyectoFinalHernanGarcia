# Web estilo Blog

Se puede entrar a la web a partir de la pagina principal http://127.0.0.1:8000/
Al cargar esa direccion deberiamos poder ver los ultimos "blogs" que han creado los usuarios.


## Features

 - El usuario puede crear cuentas con el boton de "Registrarse" si ya tiene una cuenta puede utilizar "Iniciar Sesion"
 - Una vez logueado, si hace click dentro de su nombre de usuario en la barra de navegacion, podra ver su perfil. En esta vista podra editar su perfil y ver sus posts.
 - El usuario puede crear una publicacion con Titulo, Subtitulo y el texto. Tambien puede incluir una imagen si lo desea.
 - Los posts tienen la opcion de "Leer mas", donde se puede ver el post completo, quien lo hizo y cuando. Ademas de poder hacer comentarios en cada uno.
 - Tambien la app cuenta con una opcion de Mensajeria. Si entra al perfil de otro usuario puede enviarle un mensaje privado. 
 - El usuario puede ver sus mensajes dentro de la opcion de "Mensajes" en la barra de navegacion.

## Modelos

Se utilizan los modelos de Usuario de Django, en base a estos luego creamos los modelos del blog, donde cada "pagina" es asignada a un usuario mediante una "ForeignKey". 
Luego, creamos comentarios asignados a una pagina. Y tambien con un autor que se asignar a un usuario
Y de la misma manera con los mensajes.


## Paquetes

Django 4.1.7
Pillow 9.4.0