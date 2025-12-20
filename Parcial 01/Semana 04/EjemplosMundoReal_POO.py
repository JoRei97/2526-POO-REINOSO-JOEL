# ============================================
# Sistema de Gestión de una Mecánica Automotriz
# Programación Orientada a Objetos (POO)
# ============================================

# Clase Cliente
class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
        return f"Cliente: {self.nombre} | Cédula: {self.cedula}"


# Clase Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, placa, cliente):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.cliente = cliente

    def __str__(self):
        return f"Vehículo: {self.marca} {self.modelo} | Placa: {self.placa}"


# Clase Servicio
class Servicio:
    def __init__(self, descripcion, costo):
        self.descripcion = descripcion
        self.costo = costo

    def __str__(self):
        return f"Servicio: {self.descripcion} | Costo: ${self.costo:.2f}"


# Clase Mecánica
class Mecanica:
    def __init__(self, nombre):
        self.nombre = nombre
        self.servicios_realizados = []

    def realizar_servicio(self, vehiculo, servicio):
        # Registra un servicio realizado a un vehículo
        self.servicios_realizados.append((vehiculo, servicio))
        print(f"Servicio realizado: {servicio.descripcion} al vehículo {vehiculo.placa}")

    def mostrar_servicios(self):
        print(f"\nServicios realizados en la mecánica '{self.nombre}':")
        for vehiculo, servicio in self.servicios_realizados:
            print(f"- {servicio.descripcion} | Vehículo: {vehiculo.placa} | Cliente: {vehiculo.cliente.nombre}")


# ======================
# Programa Principal
# ======================

# Crear un cliente
cliente1 = Cliente("Joel Reinoso", "0102030405")

# Crear un vehículo asociado al cliente
vehiculo1 = Vehiculo("Nissan", "Tiida", "PCO-1574", cliente1)

# Crear servicios
servicio1 = Servicio("Cambio de aceite", 30.00)
servicio2 = Servicio("Revisión de frenos", 50.00)

# Crear la mecánica
mecanica = Mecanica("Mecánica San José")

# Realizar servicios
mecanica.realizar_servicio(vehiculo1, servicio1)
mecanica.realizar_servicio(vehiculo1, servicio2)

# Mostrar resultados
print("\nInformación del cliente y vehículo:")
print(cliente1)
print(vehiculo1)

mecanica.mostrar_servicios()
