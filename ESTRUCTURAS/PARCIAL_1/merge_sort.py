# Algoritmos de Ordenamiento: Merge Sort

# Organizar una lista de elementos de forma ascendiente
# implementando el algoritmo Merge Sort, que funciona
# de manera recursiva al dividir una lista en sublistas
# hasta llegar a listas con solo un elemento.
# Despues une estas listas, en una lista vacia,
# haciendo comparaciones para que queden en orden los elementos.

# Ximena Gonzalez

def merge(arr1, arr2):
    """Funcion que une las sublistas en una lista ordenada"""

    i = 0  # apuntador de arr1
    j = 0  # apuntador de arr2
    D = []  # array vacio
    global cont  # variable por fuera de las funciones que cuenta las inversiones hechas en el arreglo

    # while loop para recorrer arr1 y arr2, comparar sus elementos y agregarlos a D conforme su orden
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            D.append(arr1[i])
            i += 1
        else:
            D.append(arr2[j])
            cont += 1  # una inversion fue hecha
            j += 1

    # los proximos while loops meten en el arreglo vacio los elementos restantes en arr1 y arr2
    while i < len(arr1):
        D.append(arr1[i])
        i += 1

    while j < len(arr2):
        D.append(arr2[j])
        j += 1

    return D


def merge_sort(arr):
    """Funcion que se llama asi misma y al final llama a merge() para unir las sublistas B y C"""

    # si len(arr) = 1 significa que ya esta ordenado
    if len(arr) == 1:
        return arr

    # punto medio; donde partir el arreglo
    m = len(arr) // 2

    # llamadas recursivas
    B = merge_sort(arr[:m])
    C = merge_sort(arr[m:])

    print(f"B = {B} C = {C}")

    # llamada para unir sublistas y almacenar la lista ordenada en A
    A = merge(B, C)
    return A


def ms():
    """Funcion que auxiliar que pide al usuario dos inputs: uno
       que indica el tamaño del arreglo y otro que son los elementos
       del arreglo separados por un espacio"""

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

    print(f"Lista original : {arr_original}")
    arr_ordenado = merge_sort(arr_original)
    print(f"Lista ordenada : {arr_ordenado}")


cont = 0
ms()
print(f"Cambios : {cont}")


# Ultima Modificacion: 31 de Agosto

