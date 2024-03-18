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