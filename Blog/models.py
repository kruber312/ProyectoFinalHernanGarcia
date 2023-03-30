from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class pagina(models.Model):
    titulo = models.CharField(max_length=40,null=True)
    subtitulo = models.CharField(max_length=40,null=True)
    cuerpo = models.TextField(null=True)
    autor = models.ForeignKey(User, models.CASCADE,null=True)
    fecha = models.DateTimeField(null=True)
    imagen = models.ImageField(upload_to="imagenes",null=True,blank=True)
