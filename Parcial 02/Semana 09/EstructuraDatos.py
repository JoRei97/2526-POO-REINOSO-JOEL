# ===============================
# SISTEMA DE INVENTARIO (SIMPLE)
# ===============================

# Clase Producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.id} | {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio}"


# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = []

    # Añadir producto (ID único)
    def añadir(self, producto):
        for p in self.productos:
            if p.id == producto.id:
                print("ID repetido")
                return
        self.productos.append(producto)
        print("Producto añadido")

    # Eliminar producto
    def eliminar(self, id):
        for p in self.productos:
            if p.id == id:
                self.productos.remove(p)
                print("🗑 Eliminado")
                return
        print("No encontrado")

    # Actualizar producto
    def actualizar(self, id, cantidad=None, precio=None):
        for p in self.productos:
            if p.id == id:
                if cantidad is not None:
                    p.cantidad = cantidad
                if precio is not None:
                    p.precio = precio
                print("Actualizado")
                return
        print("No encontrado")

    # Buscar por nombre
    def buscar(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("No hay resultados")

    # Mostrar todos
    def mostrar(self):
        if not self.productos:
            print("Inventario vacío")
        else:
            for p in self.productos:
                print(p)


# ===============================
# MENÚ
# ===============================
def menu():
    inv = Inventario()

    while True:
        print("\n1.Añadir  2.Eliminar  3.Actualizar  4.Buscar  5.Mostrar  6.Salir")
        op = input("Opción: ")

        if op == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inv.añadir(Producto(id, nombre, cantidad, precio))

        elif op == "2":
            inv.eliminar(input("ID: "))

        elif op == "3":
            id = input("ID: ")
            c = input("Cantidad (Enter = no cambiar): ")
            p = input("Precio (Enter = no cambiar): ")
            inv.actualizar(id, int(c) if c else None, float(p) if p else None)

        elif op == "4":
            inv.buscar(input("Nombre: "))

        elif op == "5":
            inv.mostrar()

        elif op == "6":
            print("Fin del programa")
            break

        else:
            print("Opción inválida")


# Ejecutar
menu()