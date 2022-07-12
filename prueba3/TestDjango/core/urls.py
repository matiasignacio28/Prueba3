from django import views
from django.urls import path, include
from .views import agregar_producto_carrito, nosotros, restar_producto_carrito, limpiar_carrito, eliminar_producto_carrito,procesar_compra, index, registro, contacto, agregar_producto, modificar_producto, listar_productos,eliminar_producto, detalle_producto, oferta, detalle_producto_oferta, carrito, edit_profile, delete_user,add_sus,sub_sus





urlpatterns = [
    path('', index,name="index"),
    path('registro/', registro, name="registro"),
    path('contacto/', contacto, name="contacto"),
    path('nosotros/', nosotros, name="nosotros"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('listar-productos/', listar_productos, name="listar_productos"),
    path('detalle-producto/<id>/', detalle_producto, name="detalle_producto"),
    path('oferta/', oferta, name="oferta"),
    path('detalle-producto_oferta/<id>/', detalle_producto_oferta, name="detalle_producto_oferta"),
    path('edit-profile/', edit_profile, name="edit_profile"),  
    path('deleteprofile/', delete_user, name="deleteprofile"),
    path('add-sus/', add_sus, name="add_sus"), 
    path('sub-sus/', sub_sus, name="sub_sus"), 
    #carro
    path('carrito/', carrito, name="carrito"), 
    path('agregar/<int:producto_id>/', agregar_producto_carrito, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto_carrito, name="Del"),
    path('restar/<int:producto_id>/', restar_producto_carrito, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('pago/', procesar_compra, name="pago"),
  
]