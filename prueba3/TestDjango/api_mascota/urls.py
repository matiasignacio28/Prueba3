from django import views
from django.urls import path, include
from api_mascota.views import ProductoList, productoDetalle



urlpatterns = [
   path('producto/', ProductoList.as_view(), name = 'producto_list'),
   path('producto-detalle/<id>', productoDetalle, name="producto_detalle"),
   
]
