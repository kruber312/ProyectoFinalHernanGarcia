from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #Tendra una relacion uno a uno con nuestro usuario

    imagen = models.ImageField(upload_to="avatares", null=True, blank=True,default="media/avatares/avat.jpg")