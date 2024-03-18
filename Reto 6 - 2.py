import math as m

# Definir funcion para calcular el area del rectangulo
def calculararearectangulo(base:float, altura:float) -> float:
  return base*altura

# Definir funcion para calcular el area de los circulos
def calcularareacirculos(radio_circulo:float) -> float:
  return (m.pi*(radio_circulo)**2)*2

# Definir funcion para calcular el perimetro del rectangulo
def calcularperimetrorectangulo(base:float, altura:float) -> float:
  return 2*(base+altura)

# Definir funcion para calcular el perimetro de los circulos
def calcularperimetrocirculos(radio_circulo:float) -> float:
  return (2*(m.pi*radio_circulo))*2

# Primera funcion para calcular los valores, teniendo en cuenta la base, la altura y el radio
def calculararea():
  base=float(input("Ingrese base del rectangulo:"))
  altura=float(input("Ingrese altura del rectangulo:"))
  radio_circulo=float(input("Ingrese radio del circulo:"))

  arearectangulo = calculararearectangulo(base, altura)
  areacirculos = calcularareacirculos(radio_circulo)
  
  areatotal = arearectangulo+areacirculos
  return areatotal

if __name__ == "__main__":
  areatotal = calculararea()
  print("El area  de la figura es:" + str(areatotal))

# Segunda funcion para calcular los valores, teniendo en cuenta la base, la altura y el radio
def calcularperimetro():
  base=float(input("Ingrese base del rectangulo:"))
  altura=float(input("Ingrese altura del rectangulo:"))
  radio_circulo=float(input("Ingrese radio del circulo:"))

  perimetrorectangulo = calcularperimetrorectangulo(base, altura)
  perimetrocirculos = calcularperimetrocirculos(radio_circulo)
  
  perimetrototal = perimetrorectangulo+perimetrocirculos
  return perimetrototal

if __name__ == "__main__":
  perimetrototal = calcularperimetro()
  print("El perimetro de la figura es:" + str(perimetrototal))

