class Nodo:
    def __init__(self, elemento):
        # Atributos del nodo
        self.elemento = elemento

        # Punteros al siguiente nodo y anterior nodo
        self.psig = None
        self.pprev = None


# Circular Doubly Linked List has properties
# of both doubly linked list and circular
# linked list in which two consecutive
# elements are linked or connected by
# previous and next pointer and the
# last node points to first node by next
# pointer and also the first node points to
# last node by the previous pointer.
class ListaDoble:
    def __init__(self):
        self.primero = None  # Primero nodo de la lista
        self.ultimo = None  # Ultimo nodo de la lista
        self.num_nodos = 0  # Tamaño de la lista

    def insertar_principio(self, datos):
        nuevo = Nodo(datos)

        if self.primero is None:
            self.primero = self.ultimo = nuevo
            return

        else:
            nuevo.psig = self.primero
            self.primero.pprev = nuevo
            self.primero = nuevo
            self.primero.pprev = self.ultimo
            self.ultimo.psig = self.primero

        self.num_nodos += 1

    def insertar_final(self, datos):
        nuevo = Nodo(datos)

        if self.primero is None:
            self.primero = self.ultimo = nuevo

        else:
            self.ultimo.psig = nuevo
            nuevo.pprev = self.ultimo
            self.ultimo = nuevo
            self.ultimo.psig = self.primero
            self.primero.pprev = self.ultimo

        self.num_nodos += 1

    def eliminar_principio(self):
        if self.primero is None:
            print("La lista esta vacia, no hay nada que eliminar")
            return

        elif self.primero == self.ultimo:
            self.primero = None
            self.ultimo = None

        else:
            segundo = self.primero.psig
            self.primero = segundo
            self.ultimo.psig = self.primero

        self.num_nodos -= 1

    def eliminar_final(self):
        if self.primero is None:
            print("La lista esta vacia, no hay nada que eliminar")
            return

        elif self.primero == self.ultimo:
            self.primero = None
            self.ultimo = None

        else:
            penultimo = self.ultimo.pprev
            self.ultimo = penultimo
            self.ultimo.psig = self.primero
            self.primero.pprev = self.ultimo

        self.num_nodos -= 1

    def imprimir_lista(self):
        # Si la lista esta vacia, no hay
        # nada que imprimir
        if self.primero is None:
            print("La lista esta vacia")
            return

        s = ""
        print("Contenidos de la lista:")
        temp = self.primero
        while temp:
            s += str(temp.elemento) + " "
            temp = temp.psig

            if temp == self.primero:
                break
        print(s + "\n")

    def imprimir_nodos(self):

        # Si la lista esta vacia, no hay
        # nada que imprimir
        if self.primero is None:
            print("La lista esta vacia")
            return

        print("Nodos y sus respectivos nodos siguientes: ")
        temp = self.primero
        for i in range(self.num_nodos-1):
            print(f"{temp.pprev.elemento} <- {temp.elemento} -> {temp.psig.elemento}")
            temp = temp.psig


lista_doble = ListaDoble()

lista_doble.insertar_final(1)
lista_doble.insertar_final(23)
lista_doble.insertar_final(5)

print("Despues de insertar al final 1, 23 y 5")
lista_doble.imprimir_lista()

lista_doble.imprimir_nodos()

lista_doble.insertar_principio(44)
lista_doble.insertar_principio(800)
lista_doble.insertar_principio(12)

print()
print("Despues de insertar al principio 44, 800 y 12")
lista_doble.imprimir_lista()

lista_doble.imprimir_nodos()

print()
print("Despues de eliminar al final dos veces")
lista_doble.eliminar_final()
lista_doble.eliminar_final()

lista_doble.imprimir_lista()

lista_doble.imprimir_nodos()

lista_doble.insertar_final(33)
lista_doble.insertar_final(17)
lista_doble.insertar_final(51)

print()
print("Despues de insertar al final 33, 17 y 51")
lista_doble.imprimir_lista()

lista_doble.imprimir_nodos()

lista_doble.eliminar_final()

print()
print("Despues de eliminar al final una vez")
lista_doble.imprimir_lista()

lista_doble.imprimir_nodos()



