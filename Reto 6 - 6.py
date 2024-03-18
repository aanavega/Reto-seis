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