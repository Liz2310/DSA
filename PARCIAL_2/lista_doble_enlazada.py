
class Nodo:
    def __init__(self, elemento):
        # Atributos del nodo
        self.elemento = elemento

        # Punteros al siguiente nodo y anterior nodo
        self.psig = None
        self.pprev = None

    def getElemento(self):
        # Regresar el dato que contiene el nodo
        return self.elemento


class ListaDoble:
    def __init__(self):
        self.primero = None  # Primero nodo de la lista
        self.ultimo = None  # Ultimo nodo de la lista
        self.num_nodos = 0  # Tamaño de la lista

    def get_num_elementos(self):
        return self.num_nodos  # Regresar el tamaño de la lista

    def get_vacio(self):
        if self.get_num_elementos() == 0:  # Regeresa si la lista esta vacia o no
            return True
        return False

    def insertar_principio(self, datos):
        nuevo = Nodo(datos)

        if self.get_vacio():
            # Si la lista esta vacia, hacer al nuevo nodo el primero y ultimo de la lista
            self.primero = self.ultimo = nuevo
        else:
            # Si la lista no esta vacia, hacer que el psig del nuevo nodo apunte al actualemente primer nodo
            # Hacer que el pprev del actualemente primer nodo en vez de apuntar a None, que apunte al nuevo nodo
            # Hacer el primero nodo de la lista el nuevo nodo
            nuevo.psig = self.primero
            self.primero.pprev = nuevo
            self.primero = nuevo

        self.num_nodos += 1  # Aumentar por 1 el tamaño de la lista

    def insertar_final(self, datos):
        nuevo = Nodo(datos)

        if self.get_vacio():
            # Si la lista esta vacia, hacer al nuevo nodo el primero y ultimo de la lista
            self.primero = self.ultimo = nuevo
        else:
            # Si la lista no esta vacia, hacer que el pprev del nuevo nodo apunte al actualemente ultimo nodo
            # Hacer que el ppsig del actualemente ultimo nodo en vez de apuntar a None, que apunte al nuevo nodo
            # Hacer el ultimo nodo de la lista el nuevo nodo
            nuevo.pprev = self.ultimo
            self.ultimo.psig = nuevo
            self.ultimo = nuevo

        self.num_nodos += 1  # Aumentar por 1 el tamaño de la lista

    def eliminar_principio(self):
        if self.get_vacio():  # Si la lista esta vacia, no hay nada que eliminar
            print("La lista esta vacia, no hay que eliminar")
            return

        # Si la lista solo contiene un elemento, hacer que ese único nodo tome el valor de None (eliminarlo)
        if self.primero.psig is None:
            self.primero = None
            self.num_nodos -= 1  # Disminuir por 1 el tamaño de la lista
            return

        # Si la lista contiene más de un elemento, hacer que el primero nodo de la lista tome el valor
        # del actualmente segundo nodo de la lista
        # Cambiar el puntador del actualmente segundo nodo de la lista a None
        self.primero = self.primero.psig
        self.primero.pprev = None
        self.num_nodos -= 1  # Disminuir por 1 el tamaño de la lista

    def eliminar_final2(self):
        if self.get_vacio():  # Si la lista esta vacia, no hay nada que eliminar
            print("La lista esta vacia, no hay que eliminar")
            return

        # Si la lista solo contiene un elemento, hacer que ese único nodo tome el valor de None (eliminarlo)
        if self.primero.psig is None:
            self.primero = None
            self.num_nodos -= 1  # Disminuir por 1 el tamaño de la lista
            return

        self.ultimo = self.ultimo.pprev
        self.ultimo.psig = None

    def eliminar_final(self):
        if self.get_vacio():  # Si la lista esta vacia, no hay nada que eliminar
            print("La lista esta vacia, no hay que eliminar")
            return

        # Si la lista solo contiene un elemento, hacer que ese único nodo tome el valor de None (eliminarlo)
        if self.primero.psig is None:
            self.primero = None
            self.num_nodos -= 1  # Disminuir por 1 el tamaño de la lista
            return

        # Si la lista tiene más de un elemento, iterar hasta llegar al último nodo
        temp = self.primero
        while temp.psig:
            temp = temp.psig

        temp.pprev.psig = None  # Cambiando el ppsig del penultimo nodo a None, "desencadenando" el último nodo
        self.ultimo = temp.pprev
        self.num_nodos -= 1  # Disminuir por 1 el tamaño de la lista

    def imprimir_lista(self):
        # Imprimir los contenidos de la lista
        print("Contenidos de Lista:")
        temp = self.primero
        while temp:
            print(f"{temp.elemento}")
            temp = temp.psig


lista = ListaDoble()

print(lista.get_vacio())

lista.insertar_principio(1)
lista.insertar_final(2)
lista.insertar_final(5)

lista.imprimir_lista()
print()

lista.eliminar_principio()
lista.imprimir_lista()

lista.insertar_final(8)
lista.imprimir_lista()

lista.eliminar_final2()
lista.imprimir_lista()

# print()
# lista.eliminar_final()
# lista.imprimir_lista()
#
# print()
# lista.insertar_final(3)
# lista.imprimir_lista()
#
# print()
# print(lista.get_num_elementos())
#
# print()
# print(lista.get_vacio())

