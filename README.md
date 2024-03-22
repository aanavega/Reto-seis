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

### Codigo numero 7

- Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
  - El promedio
  - La mediana
  - El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
  - Ordenar los números de forma ascendente
  - Ordenar los números de forma descendente
  - La potencia del mayor número elevado al menor número
  - La raíz cúbica del menor número

```Python

# Definir funcion para obtener promedio
def promedio(Primer_numero: float, Segundo_numero: float, Tercer_numero: float, Cuarto_numero: float, Quinto_numero: float):
    return ((Primer_numero+Segundo_numero+Tercer_numero+Cuarto_numero+Quinto_numero)/5)

# Definir funcion para obtener promedio multiplicativo
def promediomultiplicativo(Primer_numero: float, Segundo_numero: float, Tercer_numero: float, Cuarto_numero: float, Quinto_numero: float):
    return ((Primer_numero*Segundo_numero*Tercer_numero*Cuarto_numero*Quinto_numero)**(1/5))

# Definir funcion para ordenar los numeros de forma ascendente y descendente, para el caso 1 > numeros
def ordenarnumeros(Primer_numero, Segundo_numero, Tercer_numero, Cuarto_numero, Quinto_numero):

# Realizar una serie de condicionales para los casos de cada numero
    if Primer_numero > Segundo_numero and Segundo_numero > Tercer_numero and Tercer_numero > Cuarto_numero and Cuarto_numero > Quinto_numero: #1>2>3>4>5
        print("Los numeros ordenados de forma descendente van: " +str(Primer_numero)+ ","+ str(Segundo_numero)+ ","+ str(Tercer_numero)+ ","+ str( Cuarto_numero)+ ","+ str(Quinto_numero)+ ".")
        print("Los numeros ordenados de forma ascendente van: "+ str(Quinto_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Segundo_numero)+ ","+ str(Primer_numero)+".")
    elif Primer_numero > Segundo_numero and Segundo_numero > Tercer_numero and  Tercer_numero > Quinto_numero and Quinto_numero > Cuarto_numero:#1>2>3>5>4
        print("Los numeros ordenados de forma descendente van: " +str(Primer_numero)+ ","+ str(Segundo_numero)+ ","+ str(Tercer_numero)+ ","+ str(Quinto_numero)+ ","+ str(Cuarto_numero)+ ".")
        print("Los numeros ordenados de forma ascendente van: "+ str(Cuarto_numero)+ ","+ str(Quinto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Segundo_numero)+ ","+ str(Primer_numero)+".") 
    elif Primer_numero > Segundo_numero and Segundo_numero > Cuarto_numero and Cuarto_numero > Quinto_numero and Quinto_numero > Tercer_numero:#1>2>4>5>3
        print("Los numeros ordenados de forma ascendente van: " +str(Tercer_numero)+ ","+ str(Quinto_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Segundo_numero)+ ","+ str(Primer_numero)+ ".")
        print("Los numeros ordenados de forma descendente van: " + str(Primer_numero)+ ","+ str(Segundo_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Quinto_numero)+ ","+ str(Tercer_numero)+ ".")
    elif Primer_numero > Segundo_numero and Segundo_numero >  Cuarto_numero and Cuarto_numero > Tercer_numero and Tercer_numero > Quinto_numero:#1>2>4>3>5
        print("Los numeros ordenados de forma ascendente van: " +str(Quinto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Segundo_numero)+ ","+ str(Primer_numero)+ ".")
        print("Los numeros ordenados de forma descendente van: " + str(Primer_numero)+ ","+ str(Segundo_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Quinto_numero)+ ".")
    elif Primer_numero > Segundo_numero and Segundo_numero > Quinto_numero and Quinto_numero > Tercer_numero and Tercer_numero > Cuarto_numero:#1>2>5>3>4
        print("Los numeros ordenados de forma ascendente van: " +str(Cuarto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Quinto_numero)+ ","+ str(Segundo_numero)+ ","+ str(Primer_numero)+ ".")
        print("Los numeros ordenados de forma descendente van: " + str(Primer_numero)+ ","+ str(Segundo_numero)+ ","+ str(Quinto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Cuarto_numero)+ ".")
    elif Primer_numero > Segundo_numero and Segundo_numero > Quinto_numero and Quinto_numero > Cuarto_numero and Cuarto_numero > Tercer_numero:#1>2>5>4>5
        print("Los numeros ordenados de forma ascendente van: " +str(Cuarto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Quinto_numero)+ ","+ str(Segundo_numero)+ ","+ str(Primer_numero)+ ".")
        print("Los numeros ordenados de forma descendente van: " + str(Primer_numero)+ ","+ str(Segundo_numero)+ ","+ str(Quinto_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Quinto_numero)+ ".")
    elif Primer_numero > Tercer_numero and Tercer_numero > Segundo_numero and Segundo_numero > Cuarto_numero and Cuarto_numero > Quinto_numero:#1>3>2>4>5:
        print("Los numeros ordenados de forma ascendente van: " +str(Quinto_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Segundo_numero)+ ","+ str(Tercer_numero)+ ","+ str(Primer_numero)+ ".")
        print("Los numeros ordenados de forma descendente van: " + str(Primer_numero)+ ","+ str(Tercer_numero)+ ","+ str(Segundo_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Quinto_numero)+ ".") 
    elif Primer_numero > Tercer_numero and Tercer_numero > Segundo_numero and Segundo_numero > Quinto_numero and Quinto_numero > Cuarto_numero:#1>3>2>5>4
        print("Los numeros ordenados de forma ascendente van: " +str(Cuarto_numero)+ ","+ str(Quinto_numero)+ ","+ str(Segundo_numero)+ ","+ str(Tercer_numero)+ ","+ str(Primer_numero)+ ".")
        print("Los numeros ordenados de forma descendente van: " + str(Primer_numero)+ ","+ str(Tercer_numero)+ ","+ str(Segundo_numero)+ ","+ str(Quinto_numero)+ ","+ str(Cuarto_numero)+ ".")
    elif Primer_numero > Tercer_numero and Tercer_numero > Cuarto_numero and Cuarto_numero > Segundo_numero and Segundo_numero > Quinto_numero: #1>3>4>2>5
        print("Los numeros ordenados de forma ascendente van: " +str(Quinto_numero)+ ","+ str(Segundo_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Primer_numero)+ ".")
        print("Los numeros ordenados de forma descendente van: " + str(Primer_numero)+ ","+ str(Tercer_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Segundo_numero)+ ","+ str(Quinto_numero)+ ".")
    elif Primer_numero > Tercer_numero and Tercer_numero > Cuarto_numero and Cuarto_numero >Quinto_numero and Quinto_numero > Segundo_numero: #1>3>4>5>2
        print("Los numeros ordenados de forma ascendente van: " +str(Segundo_numero)+ ","+ str(Quinto_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Primer_numero)+ ".")
        print("Los numeros ordenados de forma descendente van: " + str(Primer_numero)+ ","+ str(Tercer_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Quinto_numero)+ ","+ str(Segundo_numero)+ ".")
    elif Primer_numero > Tercer_numero  and Tercer_numero > Quinto_numero and Quinto_numero > Cuarto_numero and Cuarto_numero > Segundo_numero: #1>3>5>4>2
        print("Los numeros ordenados de forma ascendente van: " +str(Segundo_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Quinto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Primer_numero)+ ".")
        print("Los numeros ordenados de forma descendente van: " + str(Primer_numero)+ ","+ str(Tercer_numero)+ ","+ str(Quinto_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Segundo_numero)+ ".")
    elif Primer_numero > Tercer_numero and Tercer_numero > Quinto_numero and Quinto_numero > Segundo_numero and Segundo_numero > Cuarto_numero: # 1>3>5>2>4
        print("Los numeros ordenados de forma ascendente van: " +str(Cuarto_numero)+ ","+ str(Segundo_numero)+ ","+ str(Quinto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Primer_numero)+ ".")
        print("Los numeros ordenados de forma descendente van: " + str(Primer_numero)+ ","+ str(Tercer_numero)+ ","+ str(Segundo_numero)+ ","+ str(Segundo_numero)+ ","+ str(Cuarto_numero)+ ".")
    elif Primer_numero > Cuarto_numero and Cuarto_numero > Tercer_numero and Tercer_numero > Segundo_numero and Segundo_numero > Quinto_numero: #1>4>3>2>5
        print("Los numeros ordenados de forma ascendente van: " +str(Quinto_numero)+ ","+ str(Segundo_numero)+ ","+ str(Tercer_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Primer_numero)+ ".")
        print("Los numeros ordenados de forma descendente van: " + str(Primer_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Segundo_numero)+ ","+ str(Quinto_numero)+ ".")
    elif Primer_numero > Cuarto_numero and Cuarto_numero > Tercer_numero and Tercer_numero > Quinto_numero  and Quinto_numero  >  Segundo_numero:
        print("Los numeros ordenados de forma ascendente van: " +str(Segundo_numero)+ ","+ str(Quinto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Primer_numero)+ ".")
        print("Los numeros ordenados de forma descendente van: " + str(Primer_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Quinto_numero)+ ","+ str(Segundo_numero)+ ".")
    elif Primer_numero > Cuarto_numero and Cuarto_numero > Segundo_numero and Segundo_numero > Tercer_numero and Tercer_numero > Quinto_numero:
        print("Los numeros ordenados de forma ascendente van: " +str(Quinto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Segundo_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Primer_numero)+ ".")
        print("Los numeros ordenados de forma descendente van: " + str(Primer_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Segundo_numero)+ ","+ str(Tercer_numero)+ ","+ str(Quinto_numero)+ ".")
    elif Primer_numero > Cuarto_numero and Cuarto_numero > Segundo_numero and Segundo_numero > Quinto_numero and Quinto_numero > Tercer_numero:
        print("Los numeros ordenados de forma ascendente van: " +str(Tercer_numero)+ ","+ str(Quinto_numero)+ ","+ str(Segundo_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Primer_numero)+ ".")
        print("Los numeros ordenados de forma descendente van: " + str(Primer_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Segundo_numero)+ ","+ str(Quinto_numero)+ ","+ str(Tercer_numero)+ ".")

# Definir funcion para obtener el mayor numero
def obtenermayornumero(Primer_numero, Segundo_numero, Tercer_numero, Cuarto_numero, Quinto_numero):
    return max(Primer_numero, Segundo_numero, Tercer_numero, Cuarto_numero, Quinto_numero)

# Definir funcion para obtener el menor numero
def obtenermenornumero(Primer_numero, Segundo_numero, Tercer_numero, Cuarto_numero, Quinto_numero):
    return min(Primer_numero, Segundo_numero, Tercer_numero, Cuarto_numero, Quinto_numero)

# Definir funcion para obtener la potencia del mayor numero elevado al menor numero
def potencia(Primer_numero: float, Segundo_numero: float, Tercer_numero: float, Cuarto_numero: float, Quinto_numero: float):
    mayornumero = obtenermayornumero(Primer_numero, Segundo_numero, Tercer_numero, Cuarto_numero, Quinto_numero)
    menornumero = obtenermenornumero(Primer_numero, Segundo_numero, Tercer_numero, Cuarto_numero, Quinto_numero)
    return mayornumero**menornumero

# Definir funcion para la raiz cubica del menor numero
def raizcubica(Primer_numero: float, Segundo_numero: float, Tercer_numero: float, Cuarto_numero: float, Quinto_numero: float):
    menornumero = obtenermenornumero(Primer_numero, Segundo_numero, Tercer_numero, Cuarto_numero, Quinto_numero)
    return menornumero**(1/3)

# Definir variables dentro de las funciones creadas
if __name__ == "__main__":
    Primer_numero= float(input("Ingrese su primer numero real: "))
    Segundo_numero= float(input("Ingrese su segundo numero real: "))
    Tercer_numero= float(input("Ingrese su Tercer numero real: "))
    Cuarto_numero= float(input("Ingrese su Cuarto numero real: "))
    Quinto_numero= float(input("Ingrese su Quinto numero real: "))

calcularpromedio = promedio(Primer_numero, Segundo_numero, Tercer_numero, Cuarto_numero, Quinto_numero)
calcularpromediomultiplicativo = promediomultiplicativo(Primer_numero, Segundo_numero, Tercer_numero, Cuarto_numero, Quinto_numero)
calcularpotencia = potencia(Primer_numero, Segundo_numero, Tercer_numero, Cuarto_numero, Quinto_numero)
calcularraiz = raizcubica(Primer_numero, Segundo_numero, Tercer_numero, Cuarto_numero, Quinto_numero)
calcularorden = ordenarnumeros(Primer_numero, Segundo_numero, Tercer_numero, Cuarto_numero, Quinto_numero)

# Definir los mensajes de cada operacion
print("El promedio de los numeros es: " + str(calcularpromedio))
print("El promedio multiplicativo es: " + str(calcularpromediomultiplicativo))
print("La potencia del mayor numero elevado al menor numero es " + str(calcularpotencia))
print("La raiz cubica del menor numero es " + str(calcularraiz))

```

### Codigo numero 8

- Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.

```Python

from Reto_6_Punto_7 import *

Promedio = promedio(Primer_numero, Segundo_numero, Tercer_numero, Cuarto_numero, Quinto_numero)
Promedio_multiplicativo = promediomultiplicativo (Primer_numero, Segundo_numero, Tercer_numero, Cuarto_numero, Quinto_numero)
Ordenar_numeros = ordenarnumeros(Primer_numero, Segundo_numero, Tercer_numero, Cuarto_numero, Quinto_numero)
Mayor_numeros = obtenermayornumero(Primer_numero, Segundo_numero, Tercer_numero, Cuarto_numero, Quinto_numero)
Menor_numeros = obtenermenornumero(Primer_numero, Segundo_numero, Tercer_numero, Cuarto_numero, Quinto_numero)
Potencia = potencia(Primer_numero, Segundo_numero, Tercer_numero, Cuarto_numero, Quinto_numero)
Raiz_cubica = raizcubica(Primer_numero, Segundo_numero, Tercer_numero, Cuarto_numero, Quinto_numero)

```

### Punto numero 9

- Consultar qué es y cómo funciona pip en python.

Pip es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python. Para instalarlo podemos instalar un codigo pre-determinado, lo ejecutamos y alli podremos instalar pip.

### Punto numero 10

- Hacer un listado de módulos populares para python que se puedan instalar com pip y consultar cómo instalarlos.

## Listado

  - NumPy: Biblioteca fundamental para la computación científica en Python, especialmente para trabajar con matrices y arreglos multidimensionales.
  - Pandas: Librería utilizada para la manipulación y análisis de datos en Python, ofrece estructuras de datos flexibles y eficientes.
  - Matplotlib: Librería para la creación de gráficos y visualizaciones en Python.
  - Scikit-learn: Biblioteca de aprendizaje automático de código abierto que ofrece herramientas simples y eficientes para análisis predictivo de datos.
  - TensorFlow: Plataforma de código abierto para aprendizaje automático desarrollada por Google, que permite construir y entrenar modelos de aprendizaje automático.
  - PyTorch: Biblioteca de aprendizaje automático de código abierto desarrollada por Facebook, que proporciona herramientas para construir y entrenar modelos de aprendizaje profundo.
  - Django: Framework web de alto nivel que fomenta un desarrollo rápido y limpio, basado en el patrón de diseño Modelo-Vista-Controlador (MVC).
  - Flask: Microframework web minimalista para Python, utilizado para crear aplicaciones web rápidas y eficientes.
  - Requests: Librería HTTP elegante y simple para Python, utilizada para realizar solicitudes HTTP.
  - Beautiful Soup: Librería utilizada para extraer datos de archivos HTML y XML.

## Instalacion

Para instalar cualquiera de estos modulos, abrimos la terminal del computador y escribimos, pip list; alli se nos desplegaran los modulos que ya tenemos instalados. Para instalar uno nuevo, simplemente escribimos alli mismo, pip install (nombre del modulo). De este modo:

```Python
pip install numpy

```
```Python
pip install pandas
```
```Python
pip install matplotlib
```
```Python
pip install scikit-learn
```
```Python
pip install tensorflow
```
```Python
pip install torch
```
```Python
pip install django
```
```Python
pip install flask
```
```Python
pip install requests
```
```Python
pip install beautifulsoup4
```

