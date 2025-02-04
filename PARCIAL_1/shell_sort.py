# Algoritmos de Ordenamiento: Shell Sort
# Algoritmos de Búsqueda: Búsqueda Binaria

# Organizar una lista de elementos de forma ascendiente
# implementando el algoritmo Shell Sort, que busca una
# lista usando intervalos como espacios.
# Se comparan los numeros espaciados por el intervalo
# y se hacen comparaciones e intercambios de acuerdo los valores.
# Despues se le pide al usuario un elemento a buscar en
# la lista ya ordenada y se hace la búsqueda usando Binary Search.
# Binary Search empieza buscando el elemento a la mitad del arreglo
# y dependiendo del valor (si es mayor o menor) busca la mitad
# ya sea de la parte izquierda o derecha del arreglo.

# Ximena Gonzalez

def busqueda_binaria(arr, izq, der, elemento):

    if der >= izq:  # comprobar que se siguen dividiendo las listas

        mitad = izq + (der - izq) // 2  # obtener la mitad del arreglo

        if arr[mitad] == elemento:  # si la mitad es igual que el elemento, fue encontrado
            print(f"El dato se encuentra en la lista")
            print(f"Numeros antes del dato: {mitad}")  # indicar cuantos numeros hay detras del dato a buscar (la variable mitad ya lo indica por el sistema de indexing de los arrays)

        elif arr[mitad] > elemento:  # si la mitad es mayor que el elemento, buscar en la parte izquierda (donde los elementos son menores) del arreglo
            return busqueda_binaria(arr, izq, mitad - 1, elemento)

        else:  # si la mitad es menos que el elemento, buscar en la parte derecha (donde los elementos son mayores) del arreglo
            return busqueda_binaria(arr, mitad + 1, der, elemento)

    else:
        print(f"El dato no se encuentra en la lista")


def shell_sort(arr):
    inter = len(arr) + 1  # intervalo (distancia) entre elementos a comparar
    while inter > 1:  # mientras el intervalo no sea menor que 1
        inter = inter // 2  # dividir intervalo entre 2 (para ir reduciendolo)
        bandera = True  # bandera que indica el estado de ordenamiento de la lista (si bandera regresa como False indica que ya esta en orden)
        while bandera:
            bandera = False  # indica que un cambio no se hizo
            i = 0  # contador que recorre el arreglo
            while i + inter <= (len(arr) - 1):  # asegura que las comparaciones no se salgan de la longitud del arreglo
                if arr[i] > arr[i + inter]:  # se hace un intercambio
                    aux = arr[i]
                    arr[i] = arr[i + inter]
                    arr[i + inter] = aux
                    bandera = True  # indica que un cambio se hizo
                i += 1
    return arr


def ss():
    """Funcion que auxiliar que pide al usuario dos inputs: uno
       que indica el tamaño del arreglo y otro que son los elementos
       del arreglo separados por un espacio.

       Despues pide al usuario un elemento a buscar en la lista ya ordenada"""

    while True:
        # hacer arreglo con elementos separados por espacio
        while True:
            num_elementos = int(input("Ingrese el numero de elementos dentro del arreglo (longitud del arreglo): "))

            if num_elementos < 1:
                print("La lista debe tener minimo un elemento")
            else:
                break

        arr_original = [int(x) for x in input("Ingrese los elementos del arreglo separados por un espacio: ").split()]

        if len(arr_original) != num_elementos:
            print("El numero de elementos ingresados no es el mismo que la longitud ya establecida del arreglo")
        else:
            break


    # Manda a llamar el shell sort
    print(f"Lista original : {arr_original}")
    arr_ordenado = shell_sort(arr_original)
    print(f"Lista ordenada : {arr_ordenado}")

    # Pide al usuario un elemento a buscar y lo busca en la lista ordenada llamando a busqueda binaria
    elemento_a_buscar = int(input("Ingresa un elemento a buscar en la lista: "))
    busqueda_binaria(arr_ordenado, 0, len(arr_ordenado)-1, elemento_a_buscar)


ss()


# Ultima Modificacion 2 Septiembre 2021

