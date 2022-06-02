from django import views
from django.urls import path
from .views import index, registro, contacto, agregar_producto


urlpatterns = [
    path('', index,name="index"),
    path('registro/', registro, name="registro"),
    path('contacto/', contacto, name="contacto"),
     path('agregar-producto/', agregar_producto, name="agregar_producto"),
]