# Programa para calcular el promedio semanal del clima usando POO

class ClimaDiario:
    def __init__(self, temperatura=0.0):
        # Encapsulamiento: atributo privado
        self.__temperatura = temperatura

    def set_temperatura(self, temperatura):
        self.__temperatura = temperatura

    def get_temperatura(self):
        return self.__temperatura


class ClimaSemanal:
    def __init__(self):
        self.dias = []  # Lista de objetos ClimaDiario

    def ingresar_temperaturas(self):
        print("Ingrese las temperaturas diarias de la semana:")
        for i in range(7):
            temp = float(input(f"Día {i+1}: "))
            dia = ClimaDiario(temp)
            self.dias.append(dia)

    def calcular_promedio(self):
        total = sum(dia.get_temperatura() for dia in self.dias)
        return total / len(self.dias)


# Ejemplo de uso
if __name__ == "__main__":
    semana = ClimaSemanal()
    semana.ingresar_temperaturas()
    promedio = semana.calcular_promedio()
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} °C")