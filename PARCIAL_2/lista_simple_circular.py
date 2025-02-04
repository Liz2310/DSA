# Lista Circular Simple

# Implementacion de una lista circular simple

# Ximena Gonzalez

class Node:
    """Clase para crear un objeto nodo
    que es conformado por una campo de datos y otro
    campo que es un puntero que apunta al siguiente
    nodo"""
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    """Clase para representar una lista simple circular"""
    def __init__(self):
        self.head = None  # guardar donde comienza la lista (el primer nodo de la lista)
        self.tail = None  # guardar el ultimo nodo de la lista (nodo que apunta al primer nodo de la lista)
        self.num_nodes = 0  # tamaño de la lista

    # Insertar nodo al principio de la lista
    # creando un nuevo nodo que apunte al actual
    # primer nodo y despues haciendo ese nuevo nodo
    # la cabeza (o primer nodo) de la lista.
    # Finalmente cambiar el puntero del ultimo nodo
    # a la nueva cabeza.
    def insert_at_beginning(self, data):
        new_node = Node(data)

        # Si la lista esta vacia, agregar un solo elemento
        # (haciendolo la cabeza y la cola)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head

        self.num_nodes += 1  # Aumentar tamaño de la lista

    # Insertar nodo al final de la lista
    # creando un nuevo nodo.
    # Se cambia que la cola apunte al nuevo nodo,
    # despues hacer ese nuevo nodo la cola y finalmente
    # hacer que apunte a la cabeza.
    def insert_at_end(self, data):
        new_node = Node(data)

        # Si la lista esta vacia, agregar un solo elemento
        # (haciendolo la cabeza y la cola)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

        self.num_nodes += 1  # Aumentar tamaño de la lista

    # Eliminar el primer nodo de la lista
    # tomando el segundo nodo de la lista,
    # hacer que la cabeza ahora tome el valor
    # del segundo nodo y finalmente hacer
    # que la cola apunte a la nueva cabeza
    def delete_at_beginning(self):

        # Si la lista esta vacia, no
        # hay nada que eliminar
        if self.head is None:
            print("La lista esta vacia, no hay nada que eliminar")

        # Si solo hay un nodo, cambiar el valor
        # de ambos cabeza y cola a None
        elif self.head == self.tail:
            self.head = None
            self.tail = None

        else:
            second = self.head.next
            self.head = second
            self.tail.next = self.head

    # Eliminar el ultimo nodo de la lista
    # recorriendo la lista hasta llegar al
    # penultimo nodo.
    # Hacer que la cola ahora tome el valor
    # del penultimo nodo y hacer que la nueva
    # cola ahora apunte a la cabeza.
    def delete_at_end(self):

        # Si la lista esta vacia, no
        # hay nada que eliminar
        if self.head is None:
            print("La lista esta vacia, no hay nada que eliminar")

        # Si solo hay un nodo, cambiar el valor
        # de ambos cabeza y cola a None
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next.next != self.head:
                temp = temp.next

            self.tail = temp
            self.tail.next = self.head

    # Imprimir la lista completa en un renglon
    # separada por espacios
    def print_full_list(self):

        # Si la lista esta vacia, no hay
        # nada que imprimir
        if self.head is None:
            print("La lista esta vacia")
            return

        s = ""
        print("Contenidos de la lista:")
        temp = self.head
        while temp:
            s += str(temp.data) + " "
            temp = temp.next
            if temp == self.head:
                break
        print(s + "\n")

    # Imprimir un nodo y el nodo que le
    # sigue, separados por una flecha
    def print_nodes(self):

        # Si la lista esta vacia, no hay
        # nada que imprimir
        if self.head is None:
            print("La lista esta vacia")
            return

        print("Nodos y sus respectivos nodos siguientes: ")
        temp = self.head
        while temp:
            print(f"{temp.data} -> {temp.next.data}")
            temp = temp.next
            if temp == self.head:
                break
        print("\n")


# Instancia de lista simple circular
circular_list = CircularLinkedList()

# a) Inserta 5 valores al inicio y 5 al final
circular_list.insert_at_beginning(2)
circular_list.insert_at_beginning(30)
circular_list.insert_at_beginning(13)
circular_list.insert_at_beginning(4)
circular_list.insert_at_beginning(99)

# Print para desplegar la lista despues de la inserciones al principio
# circular_list.print_full_list()  # Debe imprimir 99 4 13 30 2

circular_list.insert_at_end(1)
circular_list.insert_at_end(7)
circular_list.insert_at_end(23)
circular_list.insert_at_end(14)
circular_list.insert_at_end(29)

# b) Imprime en pantalla la lista capturada
# Print para desplegar la lista despues de las inserciones al principio y a l final
circular_list.print_full_list()  # Debe imprimir 99 4 13 30 2 1 7 23 14 29

# c) Borra dos elementos al inicio y uno al final
circular_list.delete_at_beginning()
circular_list.delete_at_beginning()
circular_list.delete_at_end()

# d) Vuelve a imprimir la lista para verificar que el borrado sea el correcto.
# Print para desplegar la lista despues de borrar dos elementos al inicio y uno al final
circular_list.print_full_list()  # Debe imprimir 13 30 2 1 7 23 14

# e) Imprime los nodos restantes uno en cada renglon con su respectivo nodo siguiente.
circular_list.print_nodes()
# Debe imprimir:
# 13 -> 30
# 30 -> 2
# 2 -> 1
# 1 -> 7
# 7 -> 23
# 23 -> 14
# 14 -> 13

# Ultima Modificacion: 30 de Septiembre 2021

