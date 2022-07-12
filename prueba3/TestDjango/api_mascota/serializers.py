from dataclasses import fields
from rest_framework import serializers
from core.models import Producto, Categoria
from core.models import Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(queryset = Categoria.objects.all(), source="categoria")
    nombreProducto = serializers.CharField(required=True , min_length=3)
    """
    def validate_nombreProducto(self, value):
        existe = Producto.objects.filter(nombreProducto__iexact = value).exists()

        if existe:
            raise serializers.ValidationError("¡El nombre ya existe!")
        return value
    """   
    class Meta:
        model = Producto
        fields = '__all__'
     
    