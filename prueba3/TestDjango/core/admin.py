from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Categoria, Producto, Contacto
from user.models import User


# Register your models here.
#Permite administrar  el modelo completo
class UserAdmin(BaseUserAdmin):
    model = User
    fieldsets= BaseUserAdmin.fieldsets + (
        ("Datos adicionales",{'fields': ('direccion','suscripcion')}),
    )

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Contacto)
admin.site.register(User, UserAdmin)

