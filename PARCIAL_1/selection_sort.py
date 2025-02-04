# Algoritmos de Ordenamiento: Selection Sort

# Organizar una lista de elemento de forma ascendiente
# implementando el algoritmo Selection Sort, que
# halla el elemento más chico y recorriendolo al 
# inicio del arreglo.

# Ximena Gonzalez

from random import randint

# start = 0
# stop = 101
# num_data = int(input("Ingrese la cantidad de numeros: "))
# nums_lst = [randint(start,stop) for i in range(num_data)]
#

def selection_sort(array, len_array):

    print(f"Lista original: {array}")

    for i in range(len_array):
        min_index = i # El indice del elemento mas chico (se comienza asumiendo que es el indice del primer elemento)
        for j in range(i+1, len_array):
            if array[min_index] > array[j]: # Si se encuentra un nuevo elemento mas chico que el anteriormente seleccionado
                min_index = j # Cambiar el indice minimo al indice del elemento mas chico nuevo

        # Cambiar de lugar el elemento "viejo" y el elemento "nuevo"
        # de forma que el mas chico quede en el lugar del "viejo" y 
        # el mas grande quede en lugar del "nuevo"

        array[i] , array[min_index] =  array[min_index] , array[i]
        print(f"Corrida {i+1} : {arr}")

    print(f"Lista ordenada: {array}")

# Usando el Metodo de seleccion directa como quedaria en la primera pasada el siguiente arreglo A[15,67,08,16,44,27,12,35]"
print("SELECCION")
arr = [15,67,8,16,44,27,12,35]

selection_sort(arr, len(arr))

# Ultima Modificacion: 19 de Agosto 2021
