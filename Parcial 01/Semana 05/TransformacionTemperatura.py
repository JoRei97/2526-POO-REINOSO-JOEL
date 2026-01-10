"""
Transformador de temperatura de Celsius a Fahrenheit
"""

class TransformarTemperatura:
    """
    Clase que representa un transformador de temperatura.
    """

    def __init__(self, temperatura_celsius):
        """
        Constructor de la clase.
        """
        self.temperatura_celsius = temperatura_celsius

    def temperatura_es_valida(self):
        """
        Verifica si la temperatura es válida el rango es >=-273
        """
        return self.temperatura_celsius >= -273

    def convertir_a_fahrenheit(self):
        """
        Convierte la temperatura de Celsius a Fahrenheit.
        """
        return (self.temperatura_celsius * 9 / 5) + 32


# Solicita la temperatura al usuario
temperatura_celsius = float(input("Ingrese la temperatura en grados Celcius: "))

# Crea un objeto de la clase TransformarTemperatura
conversor = TransformarTemperatura(temperatura_celsius)

# Valida y convierte la temperatura
if conversor.temperatura_es_valida():
    temperatura_fahrenheit = conversor.convertir_a_fahrenheit()
    print("La temperatura en Fahrenheit es:", temperatura_fahrenheit)
else:
    print("Error: la temperatura ingresada no es válida.")
