# Definir funcion para obtener promedio
def promedio(Primer_numero: float, Segundo_numero: float, Tercer_numero: float, Cuarto_numero: float, Quinto_numero: float):
    return ((Primer_numero+Segundo_numero+Tercer_numero+Cuarto_numero+Quinto_numero)/5)

# Definir funcion para obtener promedio multiplicativo
def promediomultiplicativo(Primer_numero: float, Segundo_numero: float, Tercer_numero: float, Cuarto_numero: float, Quinto_numero: float):
    return ((Primer_numero*Segundo_numero*Tercer_numero*Cuarto_numero*Quinto_numero)**(1/5))

# Definir funcion para ordenar los numeros de forma ascendente y descendente, para el caso 1 > numeros
def ordenarnumeros(Primer_numero, Segundo_numero, Tercer_numero, Cuarto_numero, Quinto_numero):
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

print("El promedio de los numeros es: " + str(calcularpromedio))
print("El promedio multiplicativo es: " + str(calcularpromediomultiplicativo))
print("La potencia del mayor numero elevado al menor numero es " + str(calcularpotencia))
print("La raiz cubica del menor numero es " + str(calcularraiz))