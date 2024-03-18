# Reto-seis

A continuacion los programas planteados del reto correspondiente, cada archivo individual esta adjuntado:

## Codigo numero 1

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

