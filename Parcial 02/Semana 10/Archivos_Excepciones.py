
# SISTEMA DE INVENTARIO MEJORADO


import os

ARCHIVO = "inventario.txt"  # Archivo donde se guardan los datos


# Clase Producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Formato para guardar en archivo
    def __str__(self):
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio}"


# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = []
        self.cargar_archivo()  # Cargar datos al iniciar

    # Cargar inventario desde archivo
    def cargar_archivo(self):
        try:
            if not os.path.exists(ARCHIVO):
                open(ARCHIVO, "w").close()  # Crear archivo si no existe

            with open(ARCHIVO, "r", encoding="utf-8") as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) == 4:
                        id, nombre, cantidad, precio = datos
                        self.productos.append(
                            Producto(id, nombre, int(cantidad), float(precio))
                        )

            print("Inventario cargado")

        except FileNotFoundError:
            print("Archivo no encontrado")
        except PermissionError:
            print("Sin permisos de lectura")
        except Exception as e:
            print("Error:", e)

    # Guardar inventario en archivo
    def guardar_archivo(self):
        try:
            with open(ARCHIVO, "w", encoding="utf-8") as f:
                for p in self.productos:
                    f.write(str(p) + "\n")  # Guardar cada producto

        except PermissionError:
            print("Sin permisos de escritura")
        except Exception as e:
            print("Error al guardar:", e)

    # Añadir producto
    def añadir(self, producto):
        for p in self.productos:
            if p.id == producto.id:
                print("ID repetido")
                return
        self.productos.append(producto)
        self.guardar_archivo()
        print("Producto añadido")

    # Eliminar producto
    def eliminar(self, id):
        for p in self.productos:
            if p.id == id:
                self.productos.remove(p)
                self.guardar_archivo()
                print("Eliminado")
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
                self.guardar_archivo()
                print("Actualizado")
                return
        print("No encontrado")

    # Buscar por nombre
    def buscar(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if encontrados:
            for p in encontrados:
                print(f"{p.id} | {p.nombre} | Cantidad: {p.cantidad} | Precio: ${p.precio}")
        else:
            print("Sin resultados")

    # Mostrar todos los productos
    def mostrar(self):
        if not self.productos:
            print("Inventario vacío")
        else:
            print("\nINVENTARIO:")
            for p in self.productos:
                print(f"{p.id} | {p.nombre} | Cantidad: {p.cantidad} | Precio: ${p.precio}")


# Menú principal
def menu():
    inv = Inventario()

    while True:
        print("\n1.Añadir  2.Eliminar  3.Actualizar  4.Buscar  5.Mostrar  6.Salir")
        op = input("Opción: ")

        try:
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

        except ValueError:
            print("Ingresa valores numéricos válidos")


# Ejecutar programa
if __name__ == "__main__":
    menu()