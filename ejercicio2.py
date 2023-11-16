"""Imagina que estás desarrollando un sistema de gestión para una empresa de comercio electrónico. Tu tarea es diseñar un conjunto de clases orientadas a objetos para manejar productos, carritos de compra, usuarios y pedidos. Debes crear clases como 'Producto', 'Carrito', 'Usuario' y 'Pedido'. Aplica herencia para representar diferentes tipos de usuarios, como 'Cliente' y 'Administrador'. Utiliza la composición para gestionar la relación entre productos y carritos, y asegúrate de que el diseño sea escalable para futuras características del comercio electrónico."""

class Producto:
    def __init__(self, nombre, stock, precio):
        self.nombre = nombre
        self.stock = stock
        self.precio = precio

class Carrito:
    def __init__(self, id):
        self._id = id
        self.productos = []

    def agregar_producto(self, nombre, stock, precio):
        if nombre == "":
            return f"Ingresar el producto correctamente"
        producto = Producto(nombre, stock, precio)
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto.nombre)

    @property
    def total(self):
        precioTotal = 0
        for producto in self.productos:
            precioTotal += producto.precio
        return precioTotal
        

class Usuario:
    def __init__(self, nombre, direccion, edad, email):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad
        self.email = email

    def pagar(self):
        pass

    def mostrar_info(self):
        return f"La informacion del usuario es {self.nombre}, {self.edad}, {self.direccion} y {self.email}"

class Cliente(Usuario):
    def __init__(self, nombre, direccion, edad, email):
        super().__init__(nombre, direccion, edad, email)
        self.carrito = Carrito(243)

    def mostrar_info(self):
        return f"La informacion del usuario es {self.nombre}, {self.edad}, {self.direccion}, {self.email} y {self.carrito}"
    
    def pagar(self):
        return f"El cliente pago!"

class Administrador(Usuario):
    def __init__(self, nombre, direccion, edad, email):
        super().__init__(nombre, direccion, edad, email)

cliente1 = Cliente("Marcos", "Calle", 25, "marcos")

cliente1.carrito.agregar_producto("Yerba", 10, 5000)
cliente1.carrito.agregar_producto("Jabon", 25, 5000)
cliente1.carrito.agregar_producto("Carne", 5, 5000)

cliente1.carrito.mostrar_productos()

print(cliente1.carrito.total)

""" Adriel Viola
Camila Gonzalez
Alan Alexis Galvan
Orianna Herrera
Alejandra Peraza
Alejo Rodriguez
Gabriela Argañaraz 
Cristian Pallante
Marcos Vizio"""