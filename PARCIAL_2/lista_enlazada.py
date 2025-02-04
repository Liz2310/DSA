# Listas Enlazadas

# Implementación de una lista enlazada simple.

# Ximena González

class Node:
    """Clase para crear un objeto nodo
    que es conformado por una campo de datos y otro
    campo que es un puntero que apunta al siguiente
    nodo"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Clase para representar una lista enlazada simple"""
    def __init__(self):
        self.head = None # guardar donde comienza la lista (el primer nodo de la lista)

    # Insertar nodo al principio de la lista
    # creando un nuevo nodo y luego apuntando
    # el encabezado (head) de la lista hacia él.
    def insert_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        print(f"Nodo con dato {new_data} agregado a la lista")

    # Insertar después de un nodo
    # insertar el nuevo nodo después del nodo que contenga
    # en el campo de datos el valor de target_node_data,
    # y cambiar el puntero del nuevo nodo para que apunte
    # al nodo que sigue.
    def insert_after(self, target_node_data, new_data):
        # Si el nodo headr no existe, significa
        # que la lista esta vacia, por lo que no hay
        # nodo existente al cual insertarle un siguiente
        # nodo.
        if self.head is None:
            print("La lista esta vacia")
            return

        new_node = Node(new_data)
        current = self.head

        while current is not None:
            if current.data == target_node_data:
                # Creando el nuevo nodo e insertando despues del
                # nodo anterior y cambiando los punteros segun correspondan
                # de forma que el nuevo nodo apunte al nodo después del anterior
                # y que el nodo anterior ahora apunte al nuevo nodo
                new_node.next = current.next
                current.next = new_node
                print(f"Nodo con dato {new_data} agregado despues de nodo con dato {target_node_data}")
                return
            current = current.next

        print(f"Nodo con dato {target_node_data} no existe en la lista")
        return

    # Insertar al final de la lista
    # recorrer toda la lista hasta llegar al
    # ultimo nodo y cambiar el puntero del ultimo
    # a que apunte al nuevo nodo, asi insertandolo
    # al final
    def insert_end(self, new_data):
        new_node = Node(new_data)

        # Si la lista no tiene principio (head),
        # insertar el nuevo nodo como primer nodo
        if self.head is None:
            self.head = new_node
            print(f"Nodo con datos {new_data} agregado a la lista")
            return

        # Recorrer la lista hasta llegar al
        # último nodo, esto mediante un while
        # que actualiza la variable "last"
        last = self.head
        while last.next:
            last = last.next

        # Cambiar el puntero del último nodo a
        # que apunte al nuevo nodo, insertandolo
        # asi a la lista
        last.next = new_node
        print(f"Nodo con dato {new_data} agregado a la lista")

    # Eliminando un nodo en una posición (índice) dado
    # Notar que las posiciones se cuentan desde 0
    def delete_node(self, position):
        # Si Head esta vacio no se puede borrar ningún elemento
        # porque significa que la lista esta vacia
        if self.head is None:
            print("La lista esta vacia")
            return

        # Se crea una variable donde se guardara el head
        # (el primer nodo de la lista)
        temp = self.head

        # Si la posicion es cero, significa que se quiere
        # eliminar el primer nodo de la lista.
        # Entonces el siguiente nodo de la lista (segundo nodo)
        # ahora se convierte en el nuevo head (ahora es el primer nodo).
        # Ahora temp no tiene ningun valor.
        if position == 0:
            self.head = temp.next
            temp = None
            print(f"Nodo en posicion {position} eliminado")
            return

        # Busca el nodo que se va a eliminar.
        # Recorrre los elementos de la lista hasta que
        # este en una posición anterior al nodo a eliminar.
        # temp tendra el valor del siguiente nodo.
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        # Si el nodo antes del nodo en la posicion dada
        # que se quiere eliminar, no existe (indicando que
        # se dio una posicion fuera de la longitud de la lista),
        # no se puede eliminar nada.
        if temp is None:
            print(f"La Posicion {position} Es Invalida")
            return

        # Si la posicion dada corresponde a una
        # más allá del último nodo, tampoco hay nada
        # que eliminar.
        if temp.next is None:
            print(f"La Posicion {position} Es Invalida")
            return

        # Se guarda en la varible "next" el
        # nodo a dos posiciones del nodo que
        # se encuentra una posicion antes del nodo
        # que se quiere eliminar
        next = temp.next.next

        # Se establece que el segundo nodo no es nada == 0
        # Desvinculando el nodo una posicion anterior del nodo
        # que se quiere eliminar.
        temp.next = None

        # temp.next sera el nodo dos nodos a la derecha
        temp.next = next
        print(f"Nodo en posicion {position} eliminado")

    # Buscar un elemento en la lista
    # recorriendo la lista desde el principio
    # (head) hasta encontrar el nodo que
    # su campo de datos coincida con el dato
    # proporcionado a la función.
    def search(self, data):
        index = 0 # Contador para indicar la posicion del nodo a buscar (si es que fue hallado); las posiciones comienzan desde 0
        current = self.head # Comenzando desde el principio
        while current is not None: # Mientras el nodo actual exista
            if current.data == data: # Fue encontrado el nodo con ese valor
                print(f"Nodo con dato {data} encontrado en la posicion {index}")
                return
            current = current.next # Actualizar el nodo actual con el nodo que sigue
            index += 1

        print(f"Nodo con dato {data} no encontrado") # No fue encontrado el nodo
        return

    # Ordernar de forma ascendente la lista implementando bubble sort
    def sort_linked_list(self, head):
        current = head # Empezar desde la cabeza
        index = Node(None) # Otro nodo para usarlo en comparaciones
        if head is None: # Si la lista esta vacia no hay nada que ordenar
            print("La lista esta vacia")
            return
        else:
            while current is not None: # Mientras haya un nodo actual (recorrer hasta el ultimo nodo)
                index = current.next # Nodo index va a tomar como valor los nodos que siguen del nodo actual
                # Si los datos del nodo actual son mayores
                # que los del nodo index, intercambiar
                # el nodo actual y nodo index
                while index is not None:
                    if current.data > index.data:
                        current.data, index.data = index.data, current.data
                    index = index.next # Cambiar al siguiente nodo a comparar
                # Una vez que se haya recorrido todos los nodos siguientes
                # al actual, entonces cambiar el nodo actual al nodo que sigue
                current = current.next

        print("La lista ha sido ordenada")

    # Imprimir la lista enlazada
    # desplegando los contenidos de la lista enlazada
    def print_list(self):
        print("Contenidos de Lista Enlazada:")
        temp = self.head
        while temp:
            print(f"{temp.data}")
            temp = temp.next

# Crear instancias de nodos
n1 = Node(1)
n2 = Node(2)
n3 = Node(4)
n4 = Node(3)

# Asignar punteros de nodos
n1.next = n2
n2.next = n3
n3.next = n4

linked_list = LinkedList() # Crear instancia de la lista
linked_list.head = n1 # Establecer el primer nodo de la lista
linked_list.print_list() # Debe imprimir 1 2 4 3

# Ambas posiciones son invalidas, por lo
# se debe desplegar un mensaje estableciendolo
linked_list.delete_node(5)
linked_list.delete_node(4)

# Insertando nodos nuevos al final de la lista
linked_list.insert_end(7) # Debe imprimir "Nodo con dato 7 agregado a la lista"
linked_list.insert_end(5) # Debe imprimir "Nodo con dato 5 agregado a la lista"
linked_list.print_list() # Debe imprimir 1 2 4 3 7 5

# Agregar nodo nuevo al principio
linked_list.insert_beginning(16) # Debe imprimir "Nodo con dato 16 agregado a la lista"
linked_list.print_list() # Debe imprimir 16 1 2 4 3 7 5

# Insertar nodo despues de nodo con el
# valor de dato igual a 4
linked_list.insert_after(4, 11) # Debe imprimir "Nodo con dato 11 agregado despues de nodo con dato 4"
linked_list.print_list() # Debe imprimir 16 1 2 4 11 3 7 5

# Insertar nodo despues de nodo con el
# valor de dato igual a 23, lo cual no
# es psoible porque tal nodo no existe en la lista
linked_list.insert_after(23, 11) # Debe imprimir "Nodo con dato 23 no existe en la lista"

# Ordenar la lista de forma ascendente
linked_list.sort_linked_list(linked_list.head) # Debe imprimir "La lista ha sido ordenada"
linked_list.print_list() # Debe imprimir 1 2 3 4 5 7 11 16
linked_list.search(3) # Debe imprimir "Nodo con dato 3 encontrado en la posicion 2"
linked_list.search(20) # Debe imprimir "Nodo con dato 20 no encontrado"

# Eliminar el nodo en la posicion 3
# (comenzando desde 0), en este caso
# corresponde al nodo con dato igual a 4
linked_list.delete_node(3) # Debe imprimir "Nodo en posicion 3 eliminado"
linked_list.print_list() # Debe imprimir 1 2 3 5 7 11 16

# Ultima Modificacion: 23 de Septiembre 2021

