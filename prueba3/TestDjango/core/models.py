from django.db import models
from user.models import User

# Create your models here.
#modelo para categoria
class Categoria(models.Model):
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la Categoria')
    

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    nombreProducto = models.CharField(max_length=80, unique=True, verbose_name='nombre')
    sku = models.IntegerField(verbose_name='sku del Producto')
    precio = models.IntegerField(verbose_name='precio del producto')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)
    oferta = models.BooleanField(default=False)
    

    def __str__(self):
        return self.nombreProducto

opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_cosulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    
    def __str__(self):
        return self.nombre



    
    
    
