# Algoritmos de Ordenamiento: Bubble Sort

# Organizar una lista de elementos de forma ascendiente
# implementando el algoritmo Bubble Sort, que realiza una
# comparacion con elementos adyacentes para ubicarlos en la 
# lista.

# Ximena Gonzalez

def bubble_sort(lst_numeros):
    # lst_numeros = []
    #
    # n = int(input("Ingrese la cantidad de numeros a ingresar: "))
    # cont = 0
    #
    # while cont < n:
    #     num = int(input("Ingrese un numero: "))
    #     lst_numeros.append(num)
    #     cont += 1
    
    print(f"Lista NO oderdana: {lst_numeros}")

    interruptor = True # Indica cuando se ha hecho un cambio o no (para evitar hacer comparaciones donde no sean necesarias)

    # Ciclo para accesar a cada elemento del arreglo
    for i in range(len(lst_numeros)-1):
        if interruptor is True:
            interruptor = False # No se ha hecho un intercambio
            # Ciclo para comparar los elementos
            for j in range(len(lst_numeros)-i-1): # el -1 es para no obterner un IndexError al comparar [j+1]; el -i excluye los elementos que ya fueron vistados/ordenados
                # Comparando dos elementos adyacentes (en este caso en orden ascendente)
                if lst_numeros[j] > lst_numeros[j+1]:
                    # Intercambiando elementos en caso de no estar en orden
                    interruptor = True # Se hizo un intercambio
                    temp = lst_numeros[j]
                    lst_numeros[j] = lst_numeros[j+1]
                    lst_numeros[j+1] = temp
        else:
            break
        print(lst_numeros)
            
    print(f"Lista ordenada: {lst_numeros}")


# "Suponga que tiene el siguiente arreglo unidimensional A[25,60,45,35,12,92,85,30]
# Usando el metodo burbuja(Intercambio directo), como quedaria el vector
# en la segunda pasada?(considera que el vector se recorre de izq. a der.
# Y quedara en orden ascendente al finalizar, es decir el elemento menor se recorre a la izq.)"
print("BUBBLE")
bubble_sort([25, 60, 45, 35, 12, 92, 85, 3])



# Ultima Modificacion: 17 de Agosto 2021



# OTRA FORMA DE BUBBLE
# def bubble(arr):
#     for i in range(len(arr)-1):
#         swapped = False
#         for j in range(len(arr)-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swapped = True
#         if not swapped:
#             return arr