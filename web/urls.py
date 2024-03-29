from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView


urlpatterns = [
# Menu Principal
    path('', home, name="home"),

    
#CRUD Producto
    path('productos/', ListarProducto.as_view(template_name = "web/productos.html"), name='leer'),
    path('productos/detalle/<int:pk>/', DetalleProducto.as_view(template_name = "web/detalle.html"), name='detalle_producto'),
    path('productos/crear', CrearProducto.as_view(template_name = "web/crear.html"), name='crear'),
    path('productos/editar/<int:pk>', ActualizarProducto.as_view(template_name = "web/actualizar.html"), name='actualizar'), 
    path('productos/eliminar/<int:pk>', EliminarProducto.as_view(), name='eliminar'),
    
#CRUD Cliente
    path('clientes/', ListarCliente.as_view(template_name = "web/clientes.html"), name='leer-cliente'),
    path('clientes/detalle/<int:pk>/', DetalleCliente.as_view(template_name = "web/detalle-cliente.html"), name='detalle_cliente'),
    path('clientes/crear', CrearCliente.as_view(template_name = "web/crear-cliente.html"), name='crear-cliente'),
    path('clientes/editar/<int:pk>', ActualizarCliente.as_view(template_name = "web/actualizar-cliente.html"), name='actualizar-cliente'), 
    path('clientes/eliminar/<int:pk>', EliminarCliente.as_view(), name='eliminar-cliente'),
    
#CRUD Categoria
    path('categorias/', ListarCategoria.as_view(template_name = "web/categorias.html"), name='leer-categorias'),
    path('categorias/detalle/<int:pk>/', DetalleCategoria.as_view(template_name = "web/detalle-categorias.html"), name='detalle-categorias'),
    path('categorias/crear', CrearCategoria.as_view(template_name = "web/crear-categoria.html"), name='crear-categoria'),
    path('categorias/editar/<int:pk>', ActualizarCategoria.as_view(template_name = "web/actualizar-categoria.html"), name='actualizar-categoria'), 
    path('categorias/eliminar/<int:pk>', EliminarCategoria.as_view(), name='eliminar-categoria'),
    
    #CRUD Pedidos
    path('pedidos/', ListarPedido.as_view(template_name = "web/pedidos.html"), name='leer-pedidos'),
    path('pedidos/detalle/<int:pk>/', DetallePedido.as_view(template_name = "web/detalle-pedidos.html"), name='detalle-pedidos'),
    path('pedidos/crear', CrearPedido.as_view(template_name = "web/crear-pedidos.html"), name='crear-pedidos'),
    path('pedidos/editar/<int:pk>', ActualizarPedido.as_view(template_name = "web/actualizar-pedidos.html"), name='actualizar-pedidos'), 
    path('pedidos/eliminar/<int:pk>', EliminarPedido.as_view(), name='eliminar-pedidos'),
    
     #____________________ Login, Logout, Registration
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="web/logout.html") , name="logout"),
    path('registrar/', register, name="registrar"),

    #____________________ Edicion Perfil, Cambio de Clave, Avatar
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiar_clave"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
]



# Configuración para archivos multimedia
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)