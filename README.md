
# Matias Marrero 50215

Proyecto Final CoderHouse Python



## Apendice

A continuación se describira el funcionamiento de una aplicación web creada por mi como proyecto final del curso de Python, la misma es una representación de una aplicación de tienda virtual de articulos deportivos orientados a CrossFit

## Autor

- [@darka94](https://github.com/Darka94)


## FAQ

#### Modelos:

Cliente, Producto, Pedido, Categoria, Avatar

### Usuario administrador para validar el panel:

user: admin

pass: admin

#### ¿Cómo esta integrada la página?:

Consta de un menu principal itegrado por la página de bienvenida Home, Contacto, Sobre mi y Productos (Solo Verlos). Tambien cuenta con la opción de buscar productos en la base de datos. Para este recorrido no es necesario estar logueado.

#### Autenticación: 

El sitio cuenta con opción de registro y Autenticación de usarios.

#### Funciones administrativas:

Los usuarios habilitados, tendrán la capacidad de realizar las funciones CRUD en los cuatro modelos de la aplicación (Productos, Categorías, Clientes, Pedidos). 

#### Perfil, Avatares:

El usuario puede autenticado puede ingresar en el botón "Perfil" y editar sus datos, cambiar su contraseña, así como la imagen de su avatar.




## Deployment
### Pre requisitos deseables:
- git-clone
- Pip
- Python  Python 3.12.2
Para realizar el Deployment de manera local el usuario deberá ejecutar los siguientes comandos:

#### Paso 1
```bash
  - git-clone https://github.com/Darka94/Marrero-Matias-50215/tree/master
  - pip install -r requeriment.txt
```
#### Paso 2

acceder a la carpeta del proyecto (donde se encuentra el archivo migrate.py) desde la consola y ejecutar:
```bash
  - python manage.py runserver
```
#### Paso 3
- Ingresar a localhost:8000 y explorar las funcionalidades

## Demo

- Video "Demo-Coder-Matias.rar"
- Casos de test.xlsx
## Used By

Este proyecto fue creado con fines educativos para:

- CoderHouse (https://www.coderhouse.com/)

