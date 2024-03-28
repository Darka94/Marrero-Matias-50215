
from django.shortcuts import render, redirect
from .models import *
from .forms import ProductoForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms

#Menu Principal
def home(request):
    return render(request, "web/home.html") 
def productos(request):
    productos = Producto.objects.all()
    return render(request, 'web/productos.html', {'producto': productos})
def categoria(request):
    categoria = Categoria.objects.all()
    return render(request, 'web/categoria.html', {'categoria':categoria})
def cliente(request):
    cliente = Cliente.objects.all()
    return render(request, 'web/cliente.html', {'cliente':cliente})
#__________________________________________________________________________
#CRUD Producto

class ListarProducto(ListView): 
    model = Producto
    

class CrearProducto(SuccessMessageMixin, CreateView): 
    model = Producto # Llamamos a la clase 'Producto' que se encuentra en nuestro archivo 'models.py'
    form = Producto # Definimos nuestro formulario con el nombre de la clase o modelo 'Producto'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Producto' de nuestra Base de Datos 
    success_message = 'Producto Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Producto
 
    # Redireccionamos a la página principal luego de crear un registro o jugo
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class DetalleProducto(DetailView): 
    model = Producto

    
class ActualizarProducto(SuccessMessageMixin, UpdateView): 
    model = Producto # Llamamos a la clase 'Producto' que se encuentra en nuestro archivo 'models.py' 
    form = Producto # Definimos nuestro formulario con el nombre de la clase o modelo 'Producto' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Producto' de nuestra Base de Datos 
    success_message = 'Producto Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Producto 
 
    # Redireccionamos a la página principal luego de actualizar un registro o Producto 
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
    
class EliminarProducto(SuccessMessageMixin, DeleteView): 
    model = Producto
    form = Producto
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o producto
    def get_success_url(self): 
        success_message = 'Producto Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Producto
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
    
#CRUD Cliente

class ListarCliente(ListView): 
    model = Cliente
    


class CrearCliente(SuccessMessageMixin, CreateView): 
    model = Cliente # Llamamos a la clase 'Producto' que se encuentra en nuestro archivo 'models.py'
    form = Cliente # Definimos nuestro formulario con el nombre de la clase o modelo 'Producto'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Producto' de nuestra Base de Datos 
    success_message = 'Cliente Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Producto
 
    # Redireccionamos a la página principal luego de crear un registro o jugo
    def get_success_url(self):        
        return reverse('leer-cliente') # Redireccionamos a la vista principal 'leer'
 

class DetalleCliente(DetailView): 
    model = Cliente

    
class ActualizarCliente(SuccessMessageMixin, UpdateView): 
    model = Cliente 
    form = Cliente  
    fields = "__all__" 
    success_message = 'Cliente Actualizado Correctamente !' 
 
  
    def get_success_url(self):               
        return reverse('leer-cliente') #
    
class EliminarCliente(SuccessMessageMixin, DeleteView): 
    model = Cliente
    form = Cliente
    fields = "__all__"     
 
    
    def get_success_url(self): 
        success_message = 'Cliente Eliminada Correctamente !' 
        messages.success (self.request, (success_message))       
        return reverse('leer-cliente') #
    
    
#CRUD Categoria

class ListarCategoria(ListView): 
    model = Categoria
    


class CrearCategoria(SuccessMessageMixin, CreateView): 
    model = Categoria 
    form = Categoria 
    fields = "__all__" 
    success_message = 'Categoria Creada Correctamente !' 
 
    # Redireccionamos a la página principal luego de crear un registro o jugo
    def get_success_url(self):        
        return reverse('leer-categorias') # Redireccionamos a la vista principal 'leer'
 

class DetalleCategoria(DetailView): 
    model = Categoria

    
class ActualizarCategoria(SuccessMessageMixin, UpdateView): 
    model = Categoria 
    form = Categoria  
    fields = "__all__" 
    success_message = 'Categoria Actualizada Correctamente !' 
 
  
    def get_success_url(self):               
        return reverse('leer-categorias') 
    
class EliminarCategoria(SuccessMessageMixin, DeleteView): 
    model = Categoria
    form = Categoria
    fields = "__all__"     
 
    
    def get_success_url(self): 
        success_message = 'Categoria Eliminada Correctamente !' 
        messages.success (self.request, (success_message))       
        return reverse('leer-categorias') 
    
#CRUD Pedidos

class ListarPedido(ListView): 
    model = Pedido
    


class CrearPedido(SuccessMessageMixin, CreateView): 
    model = Pedido 
    form = Pedido 
    fields = "__all__" 
    success_message = 'Pedido Creado Correctamente !' 
 
    # Redireccionamos a la página principal luego de crear un registro o jugo
    def get_success_url(self):        
        return reverse('leer-pedidos') # Redireccionamos a la vista principal 'leer'
 

class DetallePedido(DetailView): 
    model = Pedido

    
class ActualizarPedido(SuccessMessageMixin, UpdateView): 
    model = Pedido 
    form = Pedido  
    fields = "__all__" 
    success_message = 'Pedido Actualizado Correctamente !' 
 
  
    def get_success_url(self):               
        return reverse('leer-pedidos') 
    
class EliminarPedido(SuccessMessageMixin, DeleteView): 
    model = Pedido
    form = Pedido
    fields = "__all__"     
 
    
    def get_success_url(self): 
        success_message = 'Pedido Eliminado Correctamente !' 
        messages.success (self.request, (success_message))       
        return reverse('leer-pedidos') 