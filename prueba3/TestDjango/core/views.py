from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import Producto

# Create your views here.
#@login_required
def index(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'core/index.html', data)
    


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