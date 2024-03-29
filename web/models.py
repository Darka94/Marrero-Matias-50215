from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nombre}"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.nombre} - ${self.precio} - ${self.categoria}"
    def imagen_url(self):
    # Verifica si el campo 'imagen' está definido para el objeto actual
        if self.imagen:
            # Si hay una imagen asociada al objeto, devuelve la URL de la imagen
            return self.imagen.url
        else:
            # Si no hay una imagen asociada al objeto, devuelve None
            return None



class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return f"{self.nombre} - ${self.email}"
    
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_pedido = models.DateField()
    def __str__(self):
        return f"{self.cliente} - ${self.fecha_pedido}"
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")   
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"