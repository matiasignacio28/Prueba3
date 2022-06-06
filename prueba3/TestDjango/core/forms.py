from django import forms
from .models import Categoria, Producto, Contacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError


class ContactoForm(forms.ModelForm):
    nombre = forms.CharField(min_length=3, max_length=50)
    class Meta:
        model = Contacto
        fields = '__all__'



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]
    
class ProductoForm(forms.ModelForm):

    nombreProducto = forms.CharField(min_length=3, max_length=80)
    imagen = forms.ImageField(required=False)
    precio = forms.IntegerField(min_value=1, max_value=1500000)



    class Meta:
        model = Producto
        #fields = ['idProducto','nombreProducto','sku','precio','Categoria','imagen' ]
        fields = '__all__'
