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

class cliente:
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
