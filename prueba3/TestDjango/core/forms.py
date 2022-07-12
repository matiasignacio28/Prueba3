from tkinter import Widget
from django import forms
from .models import Categoria, Producto, Contacto
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
#from django.contrib.auth.models import User
from django.forms import ModelForm,ValidationError
from django.contrib.auth import get_user_model
User = get_user_model()


class ContactoForm(forms.ModelForm):
    nombre = forms.CharField(min_length=3, max_length=50)

    def clean_nombre(self):
     
       
        return self.cleaned_data.get('nombre','').strip()

    class Meta:
        model = Contacto
        fields = '__all__'



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]
        #fields = '__all__'
    
class ProductoForm(forms.ModelForm):

    nombreProducto = forms.CharField(min_length=3, max_length=80)
    imagen = forms.ImageField(required=False)
    precio = forms.IntegerField(min_value=1, max_value=1500000)
    """
    def clean_nombreProducto(self):
        nombre = self.cleaned_data["nombreProducto"]
        existe = Producto.objects.filter(nombreProducto__iexact = nombre).exists()
        
        if existe:
            raise ValidationError("¡El nombre ya existe!")
        return nombre
    """   
    class Meta:
        model = Producto
        #fields = ['idProducto','nombreProducto','sku','precio','Categoria','imagen' ]
        fields = '__all__'


    


# ProfileEdit
class ProfileForm(UserChangeForm):
    password = None
    #password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User 
        fields=['first_name','last_name','email','direccion']
        widgets = {
            'username': forms.TextInput(attrs={'readonly': 'readonly'}),
            
        }
        


       
      
