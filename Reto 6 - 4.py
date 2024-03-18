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