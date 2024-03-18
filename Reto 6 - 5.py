# Definir funcion para calcular el valor de un prestamo
def calcularvalorprestamo(C: float, i: float, n: int) -> float:
    valorprestamo = C * ((1 + i) ** n)
    return valorprestamo

# Definir las variables dentro de la funcion
if __name__ == "__main__":
    C = float(input("Ingrese el monto inicial del préstamo:"))
    i = float(input("Ingrese la tasa de interés anual en porcentaje:"))
    n = int(input("Ingrese la cantidad de meses del prestamo:"))
    valorprestamo = calcularvalorprestamo(C, i, n)
    print("El valor del préstamo después de: " + str(n) + " meses es: " +str(valorprestamo))
