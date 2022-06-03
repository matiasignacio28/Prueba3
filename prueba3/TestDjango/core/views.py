from importlib.metadata import files
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, ContactoForm, ProductoForm
from .models import Producto
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.
#@login_required
def index(request):
    productos = Producto.objects.filter(oferta=False)
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 6)
        productos = paginator.page(page)
    except:
        raise Http404


    data = {
        'entity': productos,
        'paginator': paginator
    }
    return render(request, 'core/index.html', data)

def oferta(request):
    productos = Producto.objects.filter(oferta=True)
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 6)
        productos = paginator.page(page)
    except:
        raise Http404


    data = {
        'entity': productos,
        'paginator': paginator
    }
    return render(request, 'core/oferta.html', data)

def agregar_producto(request):

    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se agrego un nuevo producto")
        else:
            data["form"] = formulario

    return render(request, 'core/producto/agregar.html',data)

def modificar_producto(request, id):

    producto = get_object_or_404(Producto,  idProducto=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method =='POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto editado")
            return redirect(to="listar_productos")
        data['form'] = formulario

    return render(request, 'core/producto/modificar.html', data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, idProducto=id)
    producto.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="listar_productos")



def listar_productos(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(productos, 4)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': productos,
        'paginator': paginator
    }
    
    return render(request, 'core/producto/listar.html', data)




def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Mensaje enviado")
        else:
            messages.success(request, "Problemas al guardar")
        

    return render(request, 'core/contacto.html', data)


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            #redirigir al home
            return redirect(to="index")
        data["form"] = formulario
        
    return render(request, 'registration/registro.html', data)


def detalle_producto(request, id):

    producto = get_object_or_404(Producto,  idProducto=id)

    data = {
        'producto': producto
    }
    return render(request, 'core/producto/detalle.html', data)

def detalle_producto_oferta(request, id):

    producto = get_object_or_404(Producto,  idProducto=id)

    data = {
        'producto': producto
    }
    return render(request, 'core/producto/detalle_oferta.html', data)


