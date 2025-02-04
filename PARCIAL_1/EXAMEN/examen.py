#  Nombre Alumno: Ximena González
#  Fecha: 14 Septiembre 2021
#  Examen Parcial 1

#  Solicitar al usuario una lista de numeros desordenados,
#  ordenarla implementando Quick Sort.
#  Despues solicitar al usuario numeros a buscar en la lista
#  ya ordenada implementando Busqueda Binaria.
#  Desplegar lista ordenada y los indices de la posiciones
#  que ocupan en la lista ordena los números buscados.

def binary_search(arr, elemento):
    index_izquierdo = 0  # Limite inferior
    index_derecho = len(arr) - 1  # Limite superior
    index_mitad = 0  # Indice en la mitad del arreglo

    while index_izquierdo <= index_derecho:  # Mientras no se haya recorrido completamente el arreglo
        index_mitad = (index_izquierdo + index_derecho) // 2  # Indice en la mitad es el promedio de los limites
        guess = arr[index_mitad]  # Numero en el indice de index_mitad

        # Si se ha encontrado el elemento a buscra regresa el indice
        if guess == elemento:
            return index_mitad  # En caso de haber elementos repetidos, se regresa el indice de la primer instancia hallada en cualquiera de las dos mitades

        # Si el intento fue menor que el elemento a buscar, significa que el elemento
        # esta en la parte derecha del arreglo, entonces aumentar el limite inferior
        # a uno mas que el indice de la mitad
        elif guess < elemento:
            index_izquierdo = index_mitad + 1

        # Si el intento fue mayor que el elemento a buscar, significa que el elemento
        # esta en la parte izquierd del arreglo, entonces decrementar el limite superior
        # a uno menos que el indice de la mitad
        else:
            index_derecho = index_mitad - 1

    # Si no se encontro el elemento, regresar -1
    return -1


def partition(arr, l, r):  # l y r son los limites inferior y superior respectivamente
    x = arr[l]  # Pivote
    j = l  # Indice con valor l (que recuerda la posicion del ultimo intercambio hecho)
    for i in range(l+1, r+1):  # Recorre desde uno mas alla del indice del pivote hasta el valor de r
        if arr[i] <= x:  # Si el elemento actual es menor que el pivote
            j = j + 1  # Incrementa el indice j
            arr[j], arr[i] = arr[i], arr[j] # Intercambio de elemento actual por elemento que no es menor-igual que pivote
    arr[l], arr[j] = arr[j], arr[l]  # Cambiar de posicion el pivote para que quede en medio de los elementos menores y mayores
    return j  # Regresar el indice de la nueva posicion del pivote


def quick_sort(arr, l, r):  # l y r son los limites inferior y superior respectivamente
    if l >= r:  # Si l es igual o mayor que r, signifca que ya se recorrio el arreglo completo
        return
    m = partition(arr, l, r)  # Pivote (hallado mediante la particion que hace partition)
    # Llamadas recursivas para la sublista antes del pivote y para la sublista despues del pivote
    quick_sort(arr, l, m - 1)
    quick_sort(arr, m + 1, r)


def main():

    # Primer ciclo es para solicitar al usuario el tamaño de la lista y sus elementos
    while True:

        # Meter en una lista el tamaño y los elementos
        lista = [int(x) for x in input("Ingrese el tamaño del arreglo y los elementos (separados por un espacio): ").split()]

        # El primer numero de la entrada representa el tamaño
        n = lista.pop(0)  # Sacar el primer elemento de la lista

        # Si el tamaño ingresado es igual al tamaño de la lista
        # y esta entre 1 y 30000, continuar
        if 1 <= n <= (3 * (10 ** 4)) and n == len(lista):

            # Si los elementos de la lista desordenada
            # estan entre 1 y 100000, continuar
            estado_positivos_lista = all(1 <= elemento <= (10 ** 5) for elemento in lista)
            if estado_positivos_lista:
                break
            else:
                print("Los elementos de la lista deben estar entre 1 y 100000")
        else:
            print("El tamaño no esta entre 1 y 30000 y/o la cantidad de elementos no es igual al tamaño")

    # OPCIONAL : Imprimir tamaño y lista (sin ordenar aun)
    # print("\n")
    # print(f"Tamaño de la lista: {n}")
    # print(f"Lista original: {lista}\n")

    # Segundo ciclo es para solicitar al usuario la cantidad de elementos a buscar y
    # los elementos a buscar
    while True:

        # Meter en una lista la cantidad de elementos a buscar y los elementos
        numeros_a_buscar =  [int(x) for x in input("Ingrese el número de elementos buscar y los números a buscar (separados por un espacio): ").split()]

        # El primer numero de la entrada representa la cantidad
        cantidad_a_buscar = numeros_a_buscar.pop(0)  # Sacar el primer elemento de la lista

        # Si la cantidad a buscar es mayor que 0 y si es igual al tamaño de la lista
        # de elementos a buscar, continuar
        if cantidad_a_buscar > 0 and cantidad_a_buscar == len(numeros_a_buscar):

            # Si los elementos de la lista de numeros a buscar
            # estan entre 1 y 100000, continuar
            estado_positivos_busqueda = all(1 <= elemento <= (10 ** 5) for elemento in numeros_a_buscar)
            if estado_positivos_busqueda:
                break
            else:
                print("Los numeros a buscar deben estar entre 1 y 100000")
        else:
            print("La cantidad a buscar debe ser mayor a 0 y/o la cantidad a buscar no es igual a la cantidad de numeros ingresados")

    # OPCIONAL : Imprimir la cantidad y lista de elementos a buscar
    # print(f"Cantidad de numeros a buscar: {cantidad_a_buscar}")
    # print(f"Numeros a buscar: {numeros_a_buscar}\n")

    # Llamada a Quick Sort con el limite inferior (l) siendo el inicio de la lista
    # y el limite superior (r) siendo el final de la lista
    quick_sort(lista, 0, len(lista)-1)
    print(f"Lista ordenada: {lista}")  # Imprimir la lista ordenada

    # Lista para guardar los indices de los elementos a buscar en la lista ordenada
    indices_bb = []

    # Ciclo para buscar con Busqueda Binaria cada
    # elemento en la lista de elementos a bucar, y
    # agregar a la lista de indices el indice donde el
    # elemento se encuentra (si es que fue encontrado)
    for num in numeros_a_buscar:
        i = binary_search(lista, num)
        indices_bb.append(i)

    # Imprimir los indices de los elementos a buscar en la lista ordenada
    print(f"Indices de elementos a buscar en lista ordenada: {indices_bb}")


main()

