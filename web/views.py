
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from search_views.search import SearchListView
from search_views.filters import BaseFilter
# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#Menu Principal
def home(request):
    return render(request, "web/home.html") 
def contacto(request):
    return render(request, "web/contacto.html") 
def sobre_mi(request):
    return render(request, "web/sobre_mi.html") 


#__________________________________________________________________________

#Buscar Producto
class ProductosFilter(BaseFilter):
    search_fields = {
        'search_text': ['nombre'],
        'search_precio_exact': {'operator': '__exact', 'fields': ['precio']},
        'search_precio_min': {'operator': '__gte', 'fields': ['precio']},
        'search_precio_max': {'operator': '__lte', 'fields': ['precio']},
    }
#CRUD Producto
class ListarProducto(SearchListView):
    model = Producto
    paginate_by = 30
    template_name = "web/productos.html"
    form_class = ProductoSearchForm
    filter_class = ProductosFilter
    
class CrearProducto(LoginRequiredMixin,SuccessMessageMixin, CreateView): 
    model = Producto # Llamamos a la clase 'Producto' que se encuentra en nuestro archivo 'models.py'
    form = Producto # Definimos nuestro formulario con el nombre de la clase o modelo 'Producto'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Producto' de nuestra Base de Datos 
    success_message = 'Producto Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Producto
 
    # Redireccionamos a la página principal luego de crear un registro o jugo
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class DetalleProducto(LoginRequiredMixin,DetailView): 
    model = Producto

    
class ActualizarProducto(LoginRequiredMixin,SuccessMessageMixin, UpdateView): 
    model = Producto # Llamamos a la clase 'Producto' que se encuentra en nuestro archivo 'models.py' 
    form = Producto # Definimos nuestro formulario con el nombre de la clase o modelo 'Producto' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Producto' de nuestra Base de Datos 
    success_message = 'Producto Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Producto 
 
    # Redireccionamos a la página principal luego de actualizar un registro o Producto 
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
    
class EliminarProducto(LoginRequiredMixin,SuccessMessageMixin, DeleteView): 
    model = Producto
    form = Producto
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o producto
    def get_success_url(self): 
        success_message = 'Producto Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Producto
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'




#CRUD Cliente

class ListarCliente(LoginRequiredMixin,ListView): 
    model = Cliente
    


class CrearCliente(LoginRequiredMixin,SuccessMessageMixin, CreateView): 
    model = Cliente # Llamamos a la clase 'Producto' que se encuentra en nuestro archivo 'models.py'
    form = Cliente # Definimos nuestro formulario con el nombre de la clase o modelo 'Producto'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Producto' de nuestra Base de Datos 
    success_message = 'Cliente Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Producto
 
    # Redireccionamos a la página principal luego de crear un registro o jugo
    def get_success_url(self):        
        return reverse('leer-cliente') # Redireccionamos a la vista principal 'leer'
 

class DetalleCliente(LoginRequiredMixin,DetailView): 
    model = Cliente

    
class ActualizarCliente(LoginRequiredMixin,SuccessMessageMixin, UpdateView): 
    model = Cliente 
    form = Cliente  
    fields = "__all__" 
    success_message = 'Cliente Actualizado Correctamente !' 
 
  
    def get_success_url(self):               
        return reverse('leer-cliente') #
    
class EliminarCliente(LoginRequiredMixin,SuccessMessageMixin, DeleteView): 
    model = Cliente
    form = Cliente
    fields = "__all__"     
 
    
    def get_success_url(self): 
        success_message = 'Cliente Eliminada Correctamente !' 
        messages.success (self.request, (success_message))       
        return reverse('leer-cliente') #
    
    
#CRUD Categoria

class ListarCategoria(LoginRequiredMixin,ListView): 
    model = Categoria
    


class CrearCategoria(LoginRequiredMixin,SuccessMessageMixin, CreateView): 
    model = Categoria 
    form = Categoria 
    fields = "__all__" 
    success_message = 'Categoria Creada Correctamente !' 
 
    # Redireccionamos a la página principal luego de crear un registro o jugo
    def get_success_url(self):        
        return reverse('leer-categorias') # Redireccionamos a la vista principal 'leer'
 

class DetalleCategoria(LoginRequiredMixin,DetailView): 
    model = Categoria

    
class ActualizarCategoria(LoginRequiredMixin,SuccessMessageMixin, UpdateView): 
    model = Categoria 
    form = Categoria  
    fields = "__all__" 
    success_message = 'Categoria Actualizada Correctamente !' 
 
  
    def get_success_url(self):               
        return reverse('leer-categorias') 
    
class EliminarCategoria(LoginRequiredMixin,SuccessMessageMixin, DeleteView): 
    model = Categoria
    form = Categoria
    fields = "__all__"     
 
    
    def get_success_url(self): 
        success_message = 'Categoria Eliminada Correctamente !' 
        messages.success (self.request, (success_message))       
        return reverse('leer-categorias') 
    
#CRUD Pedidos

class ListarPedido(LoginRequiredMixin,ListView): 
    model = Pedido
    


class CrearPedido(LoginRequiredMixin,SuccessMessageMixin, CreateView): 
    model = Pedido 
    form = Pedido 
    fields = "__all__" 
    success_message = 'Pedido Creado Correctamente !' 
 
    # Redireccionamos a la página principal luego de crear un registro o jugo
    def get_success_url(self):        
        return reverse('leer-pedidos') # Redireccionamos a la vista principal 'leer'
 

class DetallePedido(LoginRequiredMixin,DetailView): 
    model = Pedido

    
class ActualizarPedido(LoginRequiredMixin,SuccessMessageMixin, UpdateView): 
    model = Pedido 
    form = Pedido  
    fields = "__all__" 
    success_message = 'Pedido Actualizado Correctamente !' 
 
  
    def get_success_url(self):               
        return reverse('leer-pedidos') 
    
class EliminarPedido(LoginRequiredMixin,SuccessMessageMixin, DeleteView): 
    model = Pedido
    form = Pedido
    fields = "__all__"     
 
    
    def get_success_url(self): 
        success_message = 'Pedido Eliminado Correctamente !' 
        messages.success (self.request, (success_message))       
        return reverse('leer-pedidos') 
    
#------------Login, Logout, Authentication, Registration--------------------#
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            try:
                avatar_url = Avatar.objects.get(user=request.user).imagen.url
            except Avatar.DoesNotExist:
                avatar_url = "/media/avatares/default.png"

            return render(request, "web/home.html", {"avatar_url": avatar_url})
        else:
            return redirect(reverse_lazy('login'))
    else:
        form = AuthenticationForm()
    return render(request, "web/login.html", {"form": form})


def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)

        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
    #Si ingresa en el else es la primera vez 
        miForm = RegistroForm()

    return render(request, "web/registro.html", {"form": miForm} )  

#Edición de Perfil, Cambio Clave, Avatar

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy('home'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = UserEditForm(instance=usuario)

    return render(request, "web/editarPerfil.html", {"form": miForm} )    
   
class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "web/cambiar_clave.html"
    success_url = reverse_lazy("home")

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)

        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            #___ Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #____________________________________________________
            avatar = Avatar(user=usuario,
                            imagen=miForm.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy('home'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = AvatarForm()

    return render(request, "web/agregarAvatar.html", {"form": miForm} ) 