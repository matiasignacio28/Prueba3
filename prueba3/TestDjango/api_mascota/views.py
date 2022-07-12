from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from core.models import Producto
from .serializers import ProductoSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser





# Create your views here.
#lista de productos /api/producto/
class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)



#productos indivduales /api/producto-detalle/<id>
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated, ))
def productoDetalle(request, id):
    try:
        producto = Producto.objects.get(id=id)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(producto, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

