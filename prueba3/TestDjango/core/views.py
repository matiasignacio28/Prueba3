from importlib.metadata import files
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, ContactoForm, ProductoForm, ProfileForm
from .models import Producto
from django.core.paginator import Paginator
from django.http import Http404
from .Carrito import Carrito



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
@login_required
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

@permission_required('core.add_producto')
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


@permission_required('core.change_producto')
def modificar_producto(request, id):

    producto = get_object_or_404(Producto,  id=id)

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

@permission_required('core.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="listar_productos")


@permission_required('core.view_producto')
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

            data["form"] = formulario
        

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

    producto = get_object_or_404(Producto,  id=id)

    data = {
        'producto': producto
    }
    return render(request, 'core/producto/detalle.html', data)

@login_required
def detalle_producto_oferta(request, id):

    producto = get_object_or_404(Producto,  id=id)

    data = {
        'producto': producto
    }
    return render(request, 'core/producto/detalle_oferta.html', data)


#acciones carro
def carrito(request):  
    productos = Producto.objects.all()
    return render(request, "core/carrito/cart.html", {'productos':productos})

def agregar_producto_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("carrito")

def eliminar_producto_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("carrito")

def restar_producto_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")



def procesar_compra(request):
    if request.user.is_authenticated:
        messages.success(request, 'Gracias por su Compra!!')
        carrito = Carrito(request)
        carrito.limpiar()
        return redirect("index")
    else:
        messages.success(request, '¡Debes registrarte para realizar compras!')    
    return redirect("carrito")



# Edit Profile
@login_required
def edit_profile(request):
	
    if request.method=='POST':
        form=ProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Datos actualizados")
    form=ProfileForm(instance=request.user)
    return render(request, 'core/edit-profile.html',{'form':form})


def delete_user(self):
    self.user.is_active = False
    self.user.save()
    return redirect("index")
@login_required
def add_sus(self):
    self.user.suscripcion = True
    self.user.save()
    return redirect("nosotros")
@login_required
def sub_sus(self):
    self.user.suscripcion = False
    self.user.save()
    return redirect("nosotros")

def nosotros(request):
    return render(request, 'core/nosotros.html')




