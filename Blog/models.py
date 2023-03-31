from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pagina(models.Model):
    titulo = models.CharField(max_length=40,null=True)
    subtitulo = models.CharField(max_length=40,null=True)
    cuerpo = models.TextField(null=True)
    autor = models.ForeignKey(User, models.CASCADE,null=True)
    fecha = models.DateTimeField(null=True)
    imagen = models.ImageField(upload_to="imagenes",null=True,blank=True)

    def __str__(self):
        return f'Titulo: {self.titulo}, Autor: {self.autor.username}'

class Comment(models.Model):
    page = models.ForeignKey(Pagina, models.CASCADE,null=True)
    autor = models.ForeignKey(User, models.CASCADE,null=True)
    cuerpo = models.TextField(null=True)
    fecha = models.DateTimeField(null=True)

    def __str__(self):
        return f'Pagina: {self.page.titulo}, Autor: {self.autor.username}'

class Message(models.Model):
    de = models.ForeignKey(User, models.CASCADE,null=True,related_name='de_messages')
    para = models.ForeignKey(User, models.CASCADE,null=True,related_name='para_messages')
    cuerpo = models.TextField(null=True)
    fecha = models.DateTimeField(null=True)

    def __str__(self):
        return f'Mensaje, De: {self.de.username}, Para: {self.para.username} '