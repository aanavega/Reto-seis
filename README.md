# Reto-seis

A continuacion los programas planteados del reto correspondiente, cada archivo individual esta adjuntado:

### Codigo numero 1

- Dado la figura de la imagen, desarrolle:
  - Una función matemática para calcular el volumen y el área superficial.
  - Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
  - Revise como utilizar el valor de pi usando import math y math.pi
 
```Python

import math as m

# Definir funcion para calcular el area de la esfera
def calcularareaesfera(radio_esfera:float) -> float:
  return 4*m.pi*(radio_esfera)**2

# Definir funcion para calcular area del cono
def calcularareacono(radio_cono: float, generatriz:float) -> float:
  return (m.pi*radio_cono*generatriz)+(m.pi*radio_cono**2)

# Definir funcion para calcular el volumen de la esfera
def calcularvolumenesfera(radio_esfera:float) -> float:
  return (4/3)*(m.pi)*(radio_esfera)**3

# Definir funcion para calcular el volumen del cono
def calcularvolumencono(area_base:float, altura:float) -> float:
  return (area_base*altura)/3

# Primera funcion para calcular los valores, teniendo en cuenta los radios y la generatriz
def calcularareasuperficial():
  radio_esfera=float(input("Ingrese radio de la esfera:"))
  radio_cono=float(input("Ingrese radio del cono:"))
  generatriz=float(input("Ingrese generatriz del cono:"))

  areaesfera = calcularareaesfera(radio_esfera)
  areacono = calcularareacono(radio_cono, generatriz)
  
  areatotal = areaesfera+areacono
  return areatotal

if __name__ == "__main__":
  areasuperficial = calcularareasuperficial()
  print("El area superficial de la figura es:" + str(areasuperficial))

# Segunda funcion para calcular los valores, teniendo en cuenta los radios y la altura
def calcularvolumensuperficial():
  radio_esfera=float(input("Ingrese radio de la esfera:"))
  radio_cono=float(input("Ingrese radio del cono:"))
  altura=float(input("Ingrese altura del cono:"))

  volumenesfera = calcularvolumenesfera(radio_esfera)
  area_base = m.pi*radio_cono**2
  volumencono = calcularvolumencono(area_base, altura)
  
  volumentotal = volumenesfera+volumencono
  return volumentotal

if __name__ == "__main__":
  volumentotal = calcularvolumensuperficial()
  print("El volumen superficial de la figura es:" + str(volumentotal))

```

### Codigo numero 2

- Dado la figura de la imagen, desarrolle:
  - Una función matemática para calcular el área y el perimetro.
  - Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.
  - Revise como utilizar el valor de pi usando import math y math.pi
 
```Python

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

```

### Codigo numero 3

- Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

```Python

# Definir funcion para calcular la cantidad de carne de aves en kilos
def calcularcantidadcarne(N:int, M:int, K:int, gallinas:int, gallos:int, pollitos: int) -> int:
  cantidadcarne = (N*gallinas)+(M*gallos)+(K*pollitos)
  return cantidadcarne

# Definir las variables dentro de la funcion
if __name__ == "__main__":
  N = int(input("Ingrese cantidad de gallinas:"))
  M = int(input("Ingrese cantidad de gallos:"))
  K = int(input("Ingrese cantidad de pollitos:"))
  gallinas = 6
  gallos = 7
  pollitos= 1
  carne = calcularcantidadcarne(N, M, K, gallinas, gallos, pollitos)
  print("La  cantidad de carne son " + str(carne) + " kilos")

```

### Codigo numero 4

- Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

```Python

# Definir funcion para saber las vueltas tras una compra
def calcularcantidadvueltas(P:int, M:int, H: int, B: int, panes:int, bolsasleche:int, huevos:int) -> int:
  cantidadvueltas = B-((P*panes)+(M*bolsasleche)+(H*huevos))
  return cantidadvueltas

# Definir las variables dentro de la funcion
if __name__ == "__main__":
  P = int(input("Ingrese cantidad de panes:"))
  M = int(input("Ingrese cantidad de bolsas de leche:"))
  H = int(input("Ingrese cantidad de huevos:"))
  B = int(input("Ingrese valor del billete dado en pesos colombianos:"))
  panes= 300
  bolsasleche= 3300
  huevos= 350
  vueltas = calcularcantidadvueltas(P, M, H, B, panes, bolsasleche, huevos)
  print("La  cantidad de vueltas son: " + str(vueltas))

  if vueltas < 0:
    print("No le alcanza la plata :(")

```

### Codigo numero 5

- Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.

```Python

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

```

### Codigo numero 6

- El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

```Python

# Definir funcion para saber el numero de contagiados de covid-19, si este se duplica cada dia
def calcularcontagiados(D:int, C:int) -> int:
  contagiadoscovid = C*2**D
  return contagiadoscovid

# Definir las variables dentro de la funcion
if __name__ == "__main__":
  D = int(input("Ingrese numero de dias a partir de hoy:"))
  C = int(input("Ingrese cantidad de contagiados actuales:"))
  contagiados = calcularcontagiados(D, C)
  print("El numero total de personas contagiadas es: " + str(contagiados))

```

  

