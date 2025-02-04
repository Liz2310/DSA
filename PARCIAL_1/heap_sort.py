# Algoritmos de Ordenamiento: Heap Sort

# Organizar una lista de elementos de forma ascendiente
# implementando el algoritmo Heap Sort, que funciona
# visualizando los elementos del arreglo como un tipo
# especial de árbol binario completo llamado Heap.

# Se construye el max heap (arbol donde el elemento máximo es
# el nodo raiz), a partir de un árbol binario completo.

# Se elimina la raíz y reemplaza con el último elemento del heap,
# se reduce el tamaño del heap en 1 y se vuelve a formar un
# max heap con los nodos restantes.

# Se repite el paso 2 hasta que solo quede 1 nodo.

# Ximena Gonzalez

# NOTA: Se incluyen dos Clases sobre dos implementaciones de Heap Sort,
# en lo personal la clase HeapSort2 me ayudo mas a comprender el funcionamiento
# del algoritmo.

class HeapSort1:
    def __init__(self, a):
        self.a = a

    def sift_down(self, a, start, end):
        """Funcion que intercambia un nodo (que es menor que sus
           hijos) y su nodo hijo, hasta que el nodo menor sea menor
           que su nodo padre"""

        root = start  # Nodo a mover a la parte baja del heap (raiz)

        while (root * 2 + 1) <= end:  # Mientras que el inidce del nodo hijo izquierdo este dentro del array
            child = root * 2 + 1  # Nodo hijo izquierdo
            swap = root  # Variable para guardar el indice del nodo mayor (inicialmente es raiz)

            # Si el nodo raiz es menor que el nodo hijo izquierdo, ahora el nodo mayor es el hijo
            # izquierdo, entonces guardar su indice en swap
            if a[swap] < a[child]:
                swap = child

            # Si existe el nodo hijo derecho (verificar que el indice este dentro del array) y si
            # el nodo raiz es menor que el nodo hijo derecho, ahora el nodo mayor es el hijo derecho,
            # entonces guardar su indice en swap
            if (child + 1) <= end and a[swap] < a[child + 1]:
                swap = child + 1

            # Si el nodo original (root) ya no es el mayor (originalmente swap = root, pero si
            # alguna de las comparaciones fueron satisfechas, significa que root ya no es el mayor,
            # si no uno de sus hijos), intercambiar de lugar los valores con el indice swap
            # y root
            if swap != root:
                a[root], a[swap] = a[swap], a[root]
                root = swap

            # No hubo intercambios, por lo que el nodo ya quedo ordenado
            else:
                return

            print(a)

    def heapify(self, a, count):
        """Funcion que llama a sift_down para mover nodos a la parte baja
           del heap"""

        # Se usa el conocimiento de que el ultimo nodo padre
        # se encuentra en el indice (n//2 - 1), n siendo la
        # longitud del array
        start = int((count - 2) / 2)

        # Ciclo para comenzar a mover los nodos en el orden correcto,
        # mandando los nodos mayores a la parte baja del heap, una vez
        # que el nodo mayor del heap quede en la parte baja, se reduce
        # el tamaño del heap por 1 (de esa manera el nodo mayor queda
        # en la ultima parte del array y ya no se toma en cuenta para
        # las consecuentes iteraciones)
        while start >= 0:
            self.sift_down(a, start, count - 1)
            start -= 1

    def heapsort(self, a):
        """Funcion que inicializa el heap de manera que el elemento mayor
           del arreglo entero quede como nodo raiz. Despues se hace  intercambio
           del nodo raiz y el ultimo nodo, y se va reduciendo la longitud del
           arreglo"""

        self.heapify(a, len(a))  # Heap inicial (el mayor queda en la raiz)
        end = len(a)-1  # Ultimo indice del arreglo

        # Ciclo que hace el intercambio del nodo raiz por el ultimo, reduce la
        # longitud (por la izquierda) y llama a sift_down desde la raiz hasta
        # la nueva longitud reducida
        while end > 0:
            a[end], a[0] = a[0], a[end]
            end -= 1
            self.sift_down(a, 0, end)


# Prueba para clase HeapSort1
h1 = HeapSort1([13, 6, 45, 10, 3, 22, 5])
print("Clase HeapSort1")
h1.heapsort(h1.a)
print(h1.a)
print("\n")


class HeapSort2:
    def __init__(self, arr):
        self.arr = arr

    def heapify(self, arr, longitud, indice_raiz):
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
            self.heapify(arr, longitud, indice_mayor)

        print(arr)

    def heap_sort(self, arr):
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
            self.heapify(arr, n, i)

        # Ciclo for donde se intercambian de lugar el nodo raiz por el ultimo nodo
        # se reduce el tamaño de heap por 1 (esto para asegurar que el valor mayor
        # quede al ultimo, se almacenado en el ultimo indice del array y no sea
        # considerado para la proxima llamada de heapify). De nuevo se vuelve
        # aplicar heapify en el nodo raiz.
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # Intercambio nodo raiz con ultimo nodo
            self.heapify(arr, i, 0)  # Heapify el elemento raiz con la longitud reducida (i)


# Prueba para clase HeapSort2
h2 = HeapSort2([10, 1, 7, 2, 5])
print("Clase HeapSort2")
h2.heap_sort(h2.arr)
print(h2.arr)


# Ultima Modificacion 5 Septiembre 2021

