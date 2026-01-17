# Clase base Aparato
# Representa un aparato electrónico
class Aparato:
    def __init__(self, nombre, precio, estado):
        # Atributos públicos
        self.nombre = nombre
        self.estado = estado  # Estado del aparato: "Nuevo" o "Usado"

        # Atributo privado (encapsulación)
        self.__precio = precio

    # Método público para acceder al precio (getter)
    def get_precio(self):
        return self.__precio

    # Método que será sobrescrito por las clases hijas
    # (polimorfismo)
    def mostrar_info(self):
        return "Aparato electrónico"


# Clase hija Celular
# Hereda de la clase Aparato
class Celular(Aparato):

    # Sobrescribe el método mostrar_info
    def mostrar_info(self):
        return f"Celular: {self.nombre} | Estado: {self.estado}"


# Clase hija Tablet
# Hereda de la clase Aparato
class Tablet(Aparato):

    # Sobrescribe el método mostrar_info
    def mostrar_info(self):
        return f"Tablet: {self.nombre} | Estado: {self.estado}"


# Clase hija Laptop
# Herencia de la clase Aparato
class Laptop(Aparato):

    # Sobrescribe el método mostrar_info
    def mostrar_info(self):
        return f"Laptop: {self.nombre} | Estado: {self.estado}"


# Programa principal
# Creación de objetos
celular = Celular("Xiaomi", 550, "Nuevo")
tablet = Tablet("Honor", 150, "Usado")
laptop = Laptop("Alienware", 1500, "Nuevo")

# Lista de aparatos para demostrar polimorfismo
aparatos = [celular, tablet, laptop]

# Uso de métodos
for a in aparatos:
    print(a.mostrar_info())  # Polimorfismo
    print("Precio:", a.get_precio())  # Encapsulación


