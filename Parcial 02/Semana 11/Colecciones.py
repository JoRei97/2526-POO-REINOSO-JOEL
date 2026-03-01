
# SISTEMA DE INVENTARIO

import os

ARCHIVO = "inventario.txt"


# Clase Producto

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id              # ID
        self.nombre = nombre      # Nombre
        self.cantidad = cantidad  # Cantidad
        self.precio = precio      # Precio

    # Convertir a texto para guardar en archivo
    def __str__(self):
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio}"


# Clase Inventario

class Inventario:
    def __init__(self):
        # Diccionario: clave = ID, valor = objeto
        self.productos = {}
        self.cargar_archivo()


    # Cargar datos desde archivo

    def cargar_archivo(self):
        if not os.path.exists(ARCHIVO):
            open(ARCHIVO, "w").close()

        try:
            with open(ARCHIVO, "r", encoding="utf-8") as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) == 4:
                        id, nombre, cantidad, precio = datos
                        self.productos[id] = Producto(
                            id, nombre, int(cantidad), float(precio)
                        )
            print("Inventario cargado")

        except Exception as e:
            print("Error al cargar:", e)


    # Guardar datos en archivo

    def guardar_archivo(self):
        try:
            with open(ARCHIVO, "w", encoding="utf-8") as f:
                for p in self.productos.values():
                    f.write(str(p) + "\n")
        except Exception as e:
            print("Error al guardar:", e)


    # Añadir producto

    def añadir(self, producto):
        if producto.id in self.productos:
            print("ID repetido")
            return

        self.productos[producto.id] = producto
        self.guardar_archivo()
        print("Producto añadido")


    # Eliminar producto por ID

    def eliminar(self, id):
        if id in self.productos:
            del self.productos[id]
            self.guardar_archivo()
            print("Producto eliminado")
        else:
            print("No encontrado")


    # Actualizar producto

    def actualizar(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].cantidad = cantidad
            if precio is not None:
                self.productos[id].precio = precio

            self.guardar_archivo()
            print("Producto actualizado")
        else:
            print("No encontrado")


    # Buscar por nombre

    def buscar(self, nombre):
        encontrados = [
            p for p in self.productos.values()
            if nombre.lower() in p.nombre.lower()
        ]

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
            for p in self.productos.values():
                print(f"{p.id} | {p.nombre} | Cantidad: {p.cantidad} | Precio: ${p.precio}")



# Menú principal (interfaz)

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