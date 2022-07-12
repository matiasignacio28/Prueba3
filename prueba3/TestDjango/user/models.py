from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    direccion = models.CharField(max_length=80, blank= True, null=True,verbose_name='dirección')
    suscripcion= models.BooleanField(default=False)





    
    
    