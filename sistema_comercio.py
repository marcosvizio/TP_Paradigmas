class Producto():
    def __init__(self, nombre:str, precio:int, stock:int, id:str):
        self.nombre = nombre
        self.precio = precio
        self._stock = stock
        self._id = id

    @property
    def stock(self):
        return self._stock
    
    @property
    def id(self):
        return self._id
    
class Carrito():
    def __init__(self, productos:list):
        self.productos = productos
        self.total = 0

    def agregar_producto(self, producto):
        self.productos.append(producto)
        return print(f"El producto {producto.nombre} ha sido agregado al carrito.")
    
    def eliminar_producto(self, producto):
        self.productos.remove(producto)
        return print(f"El producto {producto.nombre} ha sido eliminado del carrito.")
    
    def calcular_total(self):
        for i in self.productos:
            self.total += i.precio
        return print(f"El precio total es de ${self.total}")
    
class Cliente():
    def __init__(self, productos, nombre, direccion):
        self.nombre = nombre
        self._direccion = direccion
        self.carrito = Carrito(productos)
        

    def agregar_producto(self,producto):
        return self.carrito.agregar_producto(producto)
        
    
    def eliminar_producto(self, producto):
        return self.carrito.eliminar_producto(producto)
    
    def calcular_total(self):
        return self.carrito.calcular_total()

    def consultar_carrito(self):
        print("Carrito:")
        for i in self.carrito.productos:
            print(f"""Producto: {i.nombre}. Precio: ${i.precio}.""")
            
    def comprar(self):
        self.carrito.productos.clear()
        print("Compra realizada.")

    @property
    def direccion(self):
        return self._direccion
    
producto1 = Producto("Yerba", 100, 5, "55xretsG")

producto2 = Producto("Dulce de leche", 50, 10, "njsnds231")

cliente = Cliente([],"Marcos","Avenida Falsa 1234")

cliente.agregar_producto(producto1)

cliente.agregar_producto(producto2)

cliente.calcular_total()

cliente.consultar_carrito()

cliente.eliminar_producto(producto2)

cliente.consultar_carrito()


