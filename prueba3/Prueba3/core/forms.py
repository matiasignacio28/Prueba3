from django import forms
from .models import Categoria, Producto, Contacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = '__all__'



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]
    
class ProductoForm(forms.ModelForm):

    imagen = forms.ImageField(required=False)

    class Meta:
        model = Producto
        #fields = ['idProducto','nombreProducto','sku','precio','Categoria','imagen' ]
        fields = '__all__'
