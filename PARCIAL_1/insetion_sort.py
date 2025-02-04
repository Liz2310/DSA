# Algoritmos de Ordenamiento: Insertion Sort (Insercion Directa)

# Organizar una lista de elementos de forma ascendiente
# implementando el algoritmo Insertion Sort (Insercion Directa),
# que divide el array en una parte ordenada y otra desordenada.
# Los valores de la parte desordenada se seleccionan y se colocan
# en la posición correcta en la parte ordenada.

# Ximena Gonzalez

from random import randint


def insertion_sort(arr):

    # # Ciclo para pedir un numero de entradas valido
    # while True:
    #     num_entradas = int(input("Ingrese la cantidad de elementos de la lista (no menor de 1 y no mayor de 50): "))
    #     if 1 <= num_entradas <= 50:
    #         break
    #     else:
    #         print("Input Invalido")
    #
    # # Generar un array con elementos aleatorios del 1 al 100
    # start = 1
    # stop = 100
    # arr = [randint(start, stop) for k in range(num_entradas)]

    print(f"Lista original {arr}")

    for i in range(1, len(arr)):
        aux = arr[i]  # Elemento actual
        j = i - 1  # Indice que esta justo detras del elemento actual
        while j >= 0 and arr[j] > aux:  # Si el elemento detras del elemento actual es mayo que el actual, hacer cambio
            arr[j+1] = arr[j]  # Recorrer el elemento que esta detras, a la derecha
            j -= 1  # Disminuir indice para la comparacion en caso de que haya otros elementos anteriores

        arr[j+1] = aux  # Colocar en el indice correcto el elemento actual
        print(f"Corrida {i} : {arr}")

    print(f"Lista ordenada {arr}")

#"Supongamos que desea ordenar las siguientes claves del arreglo unidimensional A,
# utilizando el metodo de inserción directa (baraja) en forma ascendente, como
# quedaria el vector en la 3ra. Pasada. A[15,67,08,16,44,27,12,35]"
print("INSERCION")
insertion_sort([15,67,8,16,44,27,12,35])

# Ultima Modificacion: 24 de Agosto 2021

