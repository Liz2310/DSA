# fibonacci recursivo

# Calcular el n-esimo numero fibonacci de forma recursiva
# Ximena González

# DECLARACION FUNCION
def calcular_numero_fib(n):
    # Calcula el numero en la posicion n en la serie fibonacci
    
    if n <= 0: # No es posible calcular la posicion 0 de la serie ya que no existe
        return "Input invalido"
    elif n == 1: # Caso de borde
        return 0
    elif n == 2: # Caso de borde
        return 1
    else: # Llama la funcion restando 1 y 2 respectivamente de num, y sumando estas dos
        return(calcular_numero_fib(n-1) + calcular_numero_fib(n-2))

num_calcular = int(input("Ingrese el n-esimo numero en la serie fibonacci a calcular: "))
print(f"El numero es: {calcular_numero_fib(num_calcular)}")

# Ultima Actualizacion: 12 de Agosto 2021