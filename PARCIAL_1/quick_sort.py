# Algoritmos de Ordenamiento: Quick Sort

# Organizar una lista de elementos de forma ascendiente
# implementando el algoritmo Quick Sort,
# que toma un pivote y divide el array en dos partes: una
# donde los elementos son menores o igual al pivote, y otra
# donde los elementos son mayores al pivote.
# Quick Sort es recursivo por lo que de sublistas resultan mas
# sublistas que son sujetas al mismo procedimiento.

# Ximena Gonzalez

from random import randint


def partition(arr, l, r):
    x = arr[l]  # Pivote
    j = l  # Indice con valor l
    for i in range(l+1, r+1):  # Recorre desde uno mas alla del indice del pivote hasta el valor de r
        if arr[i] <= x:  # Si el elemento actual es menor que el pivote
            j = j + 1  # Incrementa el indice j
            arr[j], arr[i] = arr[i], arr[j] # Intercambio de elemento actual por elemento que no es menor-igual que pivote
            print(f"Corrida {arr}")
    arr[l], arr[j] = arr[j], arr[l]  # Cambiar de posicion el pivote para que quede en medio de los elementos menores y mayores
    return j  # Regresar el indice de la nueva posicion del pivote


def quick_sort(arr, l, r):
    if l >= r:  # Si l es igual o mayor que r, signifca que ya se recorrio el arreglo completo
        return
    m = partition(arr, l, r)  # Pivote
    # Llamadas recursivas para la sublista antes del pivote y para la sublista despues del pivote
    quick_sort(arr, l, m - 1)
    quick_sort(arr, m + 1, r)


def qs():
    """Funcion que auxiliar que crea un array de numeros aleatorios
       y llama a quicksort pasando como argumentos el array, l (que
       en este caso es 0) y r (que en este caso es el ultimo indice del
       array)"""

    # Ciclo para pedir un numero de entradas valido
    while True:
        num_entradas = int(input("Ingrese la cantidad de elementos de la lista (no menor de 1 y no mayor de 50): "))
        if 1 <= num_entradas <= 50:
            break
        else:
            print("Input Invalido")

    # Generar un array con elementos aleatorios del 1 al 100
    start = 1
    stop = 100
    arr = [randint(start, stop) for k in range(num_entradas)]
    print(f"Lista original {arr}")

    # Llamada a quicksort
    quick_sort(arr, 0, len(arr)-1)
    print(f"Lista ordenada {arr}")


qs()


# Ultima Modificacion: 26 de Agosto 2021