from django import views
from django.urls import path
from .views import index, registro, contacto, agregar_producto, modificar_producto, listar_productos,eliminar_producto, detalle_producto, oferta, detalle_producto_oferta

urlpatterns = [
    path('', index,name="index"),
    path('registro/', registro, name="registro"),
    path('contacto/', contacto, name="contacto"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('listar-productos/', listar_productos, name="listar_productos"),
    path('detalle-producto/<id>/', detalle_producto, name="detalle_producto"),
    path('oferta/', oferta, name="oferta"),
    path('detalle-producto_oferta/<id>/', detalle_producto_oferta, name="detalle_producto_oferta"),

]