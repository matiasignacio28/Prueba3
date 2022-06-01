from django.db import models

# Create your models here.
#modelo para categoria
class Categoria(models.Model):
    idCategoria =models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la Categoria')
    

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='Id de Producto')
    nombreProducto = models.CharField(max_length=80, verbose_name='Nombre del Producto')
    sku = models.IntegerField(verbose_name='sku del Producto')
    precio = models.IntegerField(verbose_name='precio del producto')
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombreProducto

