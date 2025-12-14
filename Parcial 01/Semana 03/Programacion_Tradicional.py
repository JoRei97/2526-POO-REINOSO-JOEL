# Programa para calcular el promedio semanal del clima usando programación tradicional

# Función para ingresar temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    print("Ingrese las temperaturas diarias de la semana:")
    for i in range(7):  # 7 días de la semana
        temp = float(input(f"Día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal
def main():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} °C")

# Ejecutar el programa
if __name__ == "__main__":
    main()