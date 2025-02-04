def heapify(arr, longitud, indice_raiz):
    indice_mayor = indice_raiz  # El elemento mayor siempre esta en la raiz
    nodo_izq = 2 * indice_raiz + 1  # nodo hijo izquierdo
    nodo_der = 2 * indice_raiz + 2  # nodo hijo derecho

    # Verificar que el nodo hijo izquierdo exista (si el indice del
    # nodo sea menor que la longitud del array) y verificar si es
    # mayor que el de raiz.
    # De ser asi, cambiar el indice del valor mayor al indice del
    # nodo hijo izquierdo
    if nodo_izq < longitud and arr[indice_mayor] < arr[nodo_izq]:
        indice_mayor = nodo_izq

    # Verificar que el nodo hijo derecho exista (si el indice del
    # nodo sea menor que la longitud del array) y verificar si es
    # mayor que el de raiz.
    # De ser asi, cambiar el indice del valor mayor al indice del
    # nodo hijo derecho
    if nodo_der < longitud and arr[indice_mayor] < arr[nodo_der]:
        indice_mayor = nodo_der

    # Si una de las comparaciones pasadas resulto ser satisfechas,
    # significa que el elemento mayor no es el que esta en la raiz,
    # de ser asi se intercambia el nodo raiz con el nodo mayor, haciendo
    # que el mayor ahora quede en la raiz
    # Si el nodo raiz no es el mayor, intercambiar con el que si es mayor
    # y continuar aplicando heapify
    if indice_mayor != indice_raiz:
        arr[indice_raiz], arr[indice_mayor] = arr[indice_mayor], arr[indice_raiz]

        # Llamada recursiva para aplicar heapify a la raiz hasta que
        # sea mayor que sus nodos hijos (en caso de ser el mayor)
        # o se convierta en un nodo hoja (en caso de no ser el mayor)
        heapify(arr, longitud, indice_mayor)

    print(arr)


def heap_sort(arr):
    n = len(arr)  # Longitud del array

    # Construyendo max-heap inicial (donde el elemento mas grande esta en la raiz)
    # Heapify no necesita aplicarse en nodos hoja (leaf nodes) porque no tienen
    # hijos con que compararlos, por lo cual se usa el conocimiento de que el
    # ultimo nodo padre se encuentra en el indice (n//2 - 1), que es en donde
    # se comienza el proceso heapify (que asegura que el elemento mayor este
    # en la raiz).
    # Este for es armando el max heap completo, sin alteracion ninguna mas que el
    # cambio de posicion del valor mayor del arreglo entero
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Ciclo for donde se intercambian de lugar el nodo raiz por el ultimo nodo
    # se reduce el tamaño de heap por 1 (esto para asegurar que el valor mayor
    # quede al ultimo, sea almacenado en el ultimo indice del array y no sea
    # considerado para la proxima llamada de heapify). De nuevo se vuelve
    # aplicar heapify en el nodo raiz.
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Intercambio nodo raiz con ultimo nodo
        heapify(arr, i, 0)  # Heapify el elemento raiz con la longitud reducida (i)


arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
