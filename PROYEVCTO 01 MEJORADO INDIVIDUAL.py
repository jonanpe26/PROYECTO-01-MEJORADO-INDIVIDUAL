from itertools import product


class Categoria:
    def __init__(self, id_categoria, nombre):
        self.id_categoria=id_categoria
        self.nombre=nombre

    def __str__(self):
        return{
            "id_categoria":self.id_categoria,
            "nombre":self.nombre
        }

class Producto:
    def __init__(self, id_producto, nombre, precio, categoria, stock, total_compras=0, total_ventas=0):
        self.id_producto=id_producto
        self.nombre=nombre
        self.precio = float(precio)
        self.categoria = categoria
        self.stock=stock
        self.total_compras=total_compras
        self.total_ventas=total_ventas


    def diccionario(self):
        return {
            "id":self.id_producto,
            "nombre":self.nombre,
            "precio":self.precio,
            "stock":self.stock,
            "compras":self.total_compras,
            "ventas":self.total_ventas,
            "categoria":self.categoria.nombre
        }

class Cliente:
    def __init__(self, nit, nombre, direccion, telefono, correo):
        self.nit=nit
        self.nombre=nombre
        self.direccion=direccion
        self.telefono=telefono
        self.correo=correo

    def diccionario(self):
        return {
            "nit":self.nit,
            "nombre":self.nombre,
            "direccion":self.direccion,
            "telefono":self.telefono,
            "correo":self.correo
        }

class proveedor:
    def __init__(self, nit, nombre, direccion, telefono, correo, empresa):
        self.nir=nit
        self.nombre=nombre
        self.direccion=direccion
        self.telefono=telefono
        self.correo=correo,
        self.empresa=empresa

    def diccionario(self):
        return {
            "nit": self.nit,
            "nombre": self.nombre,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "correo": self.correo,
            "empresa":self.empresa
        }
class empleado:
    def __init__(self, id_empleado, nombre, direccion,  telefono, correo, puesto):
        self.id_empleado=id_empleado
        self.nombre=nombre
        self.direccion=direccion
        self.telefono=telefono
        self.correo=correo
        self.puesto=puesto

    def diccioanrio(self):
        return {
            "id_empleado":self.id_empleado,
            "nombre": self.nombre,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "correo": self.correo,
            "puesto": self.puesto
        }

class detalles_ventas:
    def __init__(self, id_detalle, producto, cantidad):
        self.id_detalle=id_detalle
        self.producto=producto
        self.cantidad=cantidad

    def diccionario(self):
        return {
            "id_detalle_venta":self.id_detalle,
            "producto":self.producto,
            "cantidad":self.cantidad,
            "subtotal":self.cantidad*self.producto.precio
        }

class venta:
    def __init__(self, id_venta, empleado, cliente, fecha):
        self.id_venta=id_venta
        self.empleado=empleado
        self.cliente=cliente
        self.fecha=fecha
        self.detalles=[]

    def agrefar_detalles(self,detalle):
        self.detalles.append(detalle)

    def diccionario(self):
        return {
            "id_venta":self.id_venta,
            "empleado":self.empleado.nommbre,
            "fecha":self.fecha,
            "detalles": [d.diccionario()for d in self.detalles],
            "total":sum(d.cantidad*d.producto.precio for d in self.detalles)
        }

class detalle_compra:
    def __init__(self, id_detalle, producto, cantidad):
        self.id_detalle=id_detalle
        self.producto=producto
        self.cantidad=cantidad

    def diccionario(self):
        return {
            "id_detalle_compra":self.id_detalle,
            "producto":self.producto,
            ""
        }

class Venta:
    def __init__(self, id_venta, cliente, producto, cantidad):
        self.id_venta = id_venta
        self.cliente = cliente
        self.producto = producto
        self.cantidad = cantidad
        self.total = producto.precio * cantidad

    def a_diccionario(self):
        return {
            "ID_Venta": self.id_venta,
            "Cliente": self.cliente.nombre,
            "Producto": self.producto.nombre,
            "Cantidad": self.cantidad,
            "Total": self.total
        }
clientes =[]
proveedores=[]
productos=[]
ventas=[]

def registrar_cliente():
    id_cliente=len(clientes)+1
    nombre=input("ingrese el nombre del cliente: ")
    telefono=input("ingrese telefono: ")
    cliente = Cliente("id_cliente, nombre, telefono")
    clientes.append(cliente)
    print("cliente registrado")

def registrar_proveedor():
    id_proveedor=len(proveedores)+1
    nombre = input("ingrese el nombre del cliente: ")
    correo = input("ingrese correo: ")
    proveedor = input("ingrese el nombre del proveedor: ")
    proveedores.append(proveedor)
    print("proveedor registrado")

def registrar_producto():
    id_producto=len(productos)+1
    nombre = input("ingrese el nombre del producto: ")
    precio=input(float("ingrese el precio del producto: "))
    stock=int(input("ingrese stock: "))
    categoria=input("ingrese categoria: ")

    if len(proveedores)==0:
        print("debe ingresar un proveedor primero: ")
        return

    print("lista de proveedores: ")
    for p in proveedores:
        print(f"{p.id_proveedores}.{p.nombre}")

    id_proveedor=int(input("ingrese el id del proveedor: "))
    proveedor=

    if proveedor is None:
        print("proveedor no encontrado")
        return

    producto = Producto=(id_producto, nombre, precio, stock, categoria, proveedor)
    productos.append(producto)
    print("prodcuto registrado")

def registrar_venta():
    if len(clientes)==0;
        print("debe registrar un cliente primero")
        return
    if len(productos)==0;
        print("debeb registrar un producto primero")
        return

    print("lista de clientes: ")
    for c in clientes:
        print (f"{c.id_cliente}.{c.nombre}")

    id.cliente=int(input("ingrese el id del cliente: "))
    cliente=

    print("lista de productos: ")
    for p in productos:
        print(f"{p.id_productos}.{p.nombre}(stock{p.stock})")

    id_producto=int
