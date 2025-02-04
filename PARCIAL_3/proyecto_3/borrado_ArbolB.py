#  Proyecto Parcial 3 Implementación de Borrado Arbol B

#  En este proyecto se realizó un código cuyo objetivo es el
#  implementar la estructura de árbol B para poder desarrollar
#  el algoritmo de borrado de una llave.

#  Al borrar una llave se busca que la estructura de árbol B
#  mantenga sus propiedades:
#       -> Que las llaves del hijo de la izquierda del nodo sean menores que la
#          llave en el nodo padre.
#       -> Que las llaves del hijo de la derecha del nodo sean mayores que la
#          llave en el nodo padre.
#       -> Que ningún nodo tenga menos llaves que el mínimo (t).
#       -> Que la diferencia entre número de hijos y número de llaves de un nodo
#          no puede ser mayor a 1.
#       -> Que el máximo de llaves de un nodo es 2*t
#       -> Que el máximo de hijos de un nodo es 2*t + 1

#  Ximena González

#  Fecha de entrega: 27 de Noviembre 2021

import random

class Node:
    def __init__(self, t):  # t = minimos numero de child = (m-1)/2
        self.child = []  # Apuntadores
        self.keys = []  # Claves a guardar
        self.n = 0  # Número de llaves

        for k in range(2 * t + 1):  # Para las llaves, 2*t = Maximo numero de claves
            self.keys.append(None)

        for k in range(2 * t + 2):  # Para los child
            self.child.append(None)

    # Indica si el nodo es hoja
    def leaf(self):
        if any(self.child):  # Si alguno elemento de la lista de child no es None, entonces no es hoja
            return False  # Regresa False
        return True  # Si no regresa True

    # Agrgar una llave a las lista de llaves de un nodo
    def add_key(self, k):
        for i in range(len(self.keys)):
            if self.keys[i] is None:
                self.keys[i] = k
                return

    # Tomar la última llave de la lista de llaves de un nodo
    def grab_last_key(self):
        for i in range(len(self.keys)-1, -1, -1):
            if self.keys[i] is not None:
                return self.keys[i], i

    # Tomar el último hijo de la lista de hijos de un nodo
    def grab_last_child(self):
        for i in range(len(self.child)-1, -1, -1):
            if self.child[i] is not None:
                return self.child[i], i

    # Calcular el numero de llaves de un nodo
    def calculate_n(self):
        self.n = 0
        for i in self.keys:
            if i is not None:
                self.n += 1

    # Agregar un nodo a la lista de hijos de un nodo
    def add_child(self, c):
        for i in range(len(self.child)):
            if self.child[i] is None:
                self.child[i] = c
                return

    # Funcion auxiliar para revisar que un hijo
    # no este en una posicion en la lista de hijos de un nodo (padre)
    # donde resulte que todas las llaves del hijo sean mayor
    # que una de las llaves del nodo (padre)
    def check(self, list1, val):
        for x in list1:
            if x:
                if x > val:
                    return True
        return False

    # Mover los hijos de posicion de acuerdo las llaves
    # del nodo padre, para que de esa forma no haya discrepancia
    # en la posicion segun los valores de las llaves del nodo hijo
    # (que los numeros dentro de los nodos queden dentro de los
    # rangos apropieados segun las llaves del nodo padre)
    def shift_children(self):
        j = 0
        for i in range(self.n):
            flag = self.check(self.child[j].keys, self.keys[i])
            if flag:
                temp = self.child[j]
                self.child[i] = None
                self.child.pop()
                self.child.insert(i+1, temp)
            j += 1

    # Contar la cantidad de hijos de un nodo
    def count_children(self):
        num = 0
        for child in self.child:
            if child is not None:
                num += 1
        return num


# Funcion auxiliar para desplegar los niveles del arbol
def print_rec(nodo, level):
    if nodo is not None:
        i = nodo.n - 1
        while i >= 0:
            print_rec(nodo.child[i + 1], level + 1)
            for j in range(level):
                print("   ", end="")
            print(nodo.keys[i])
            i -= 1
        print_rec(nodo.child[0], level + 1)


class ArbolB:
    def __init__(self, gradoMinimo):
        self.t = gradoMinimo  # gradoMinimo = (m-1)/2, donde m = Grado del arbol
        self.root = None  # Raíz del arbol

    # Funcion para crear arbol
    def bTreeCreate(self):
        if not self.root:  # Si no hay root
            self.root = Node(self.t)  # Se crea una instancial del nodo y se guarda en la raíz.
        return self.root

    # Funcion para partir un nodo x que está lleno
    # y un índice i de donde se comienza a guardar
    # los hijos del nodo x
    def bTreeSplitChild(self, x, i):
        z = Node(self.t)  # Se crea un nuevo nodo que será el nuevo hijo del nodo x
        y = x.child[i]  # Se asigna la lista de los hijos del nodo x
        z.n = self.t  # Ambos deben cumplir con la regla del grado mínimo

        # Recorrido en el que se mueven los keys con sus nodos correspondientes
        # cuando se realiza el movimiento de y a z, la mitad de las llaves estarán
        # en z, y la otra en y
        for j in range(0, self.t):
            z.keys[j] = y.keys[j + self.t + 1]
            y.keys[j + self.t + 1] = None

        # Si el nodo "y" (Hijo a separar) no es hoja
        # se realiza el recorrido para mover los child
        # cuando se realiza el movimiento de y a z, ya no hay apuntador
        if not y.leaf():
            for j in range(0, self.t + 1):
                z.child[j] = y.child[j + self.t + 1]
                y.child[j + self.t + 1] = None
        y.n = self.t

        for j in range(x.n + 1, i, -1):
            x.child[j] = x.child[j - 1]  # Se recorren los hijos de x (el nodo padre)
        x.child[i + 1] = z  # Se agrega ese nuevo nodo x (donde se dividieron la segunda mitad de las llaves)

        for j in range(x.n, i, -1):  # Ajustar las llaves de x (el nodo padre)
            x.keys[j] = x.keys[j - 1]
        x.keys[i] = y.keys[self.t]  # Copiar la nueva llave que se va a subir
        y.keys[self.t] = None  # Borrarla del nodo hijo
        x.n = x.n + 1  # Se aumenta en 1 el numero de keys de x

    # Función para insertar en un nodo que no esta lleno
    def bTreeInsertNonFull(self, x, k):
        i = x.n  # Indice de la cantidad de keys que hay en el nodo x

        if x.leaf():  # si el nodo "x" es un nodo hoja

            # Se realiza el movimiento del key (se recorre)
            # Mientras el indice sea 1 o mayor y "k" sea menor al key del nodo "x"
            while i >= 1 and k < x.keys[i - 1]:
                x.keys[i] = x.keys[i - 1]
                i = i - 1
            x.keys[i] = k  # Se inserta "k" dentro de los keys del nodo "x"
            x.n += 1  # Se incrementa la cantidad de keys en 1, ya que se inserto un valor nuevo
        else:
            # Para cuando no es hoja
            # Reduce el indice mientras el indice sea 1 o mayor
            # y "k" sea menor al key del nodo "x"
            while i >= 1 and k < x.keys[i - 1]:  #  # Analizar el índice del hijo donde se va a insertar el número
                i = i - 1

            # Se realiza la recursividad para los hijos del nodo
            self.bTreeInsertNonFull(x.child[i], k)

            # Si se llena el nodo, realizar la separación
            # y si el valor a insertar es mayor al key en "x",
            # movernos al indice siguiente
            if x.child[i].n == 2 * self.t + 1:
                self.bTreeSplitChild(x, i)
                if k > x.keys[i]:
                    i = i + 1

    # Función para insertar keys en el árbol
    # Se apoya con las funciones de bTreeInsertNonFull y bTreeSplitChild
    def bTreeInsert(self, nodo, k):
        r = self.root  # Raíz de árbol

        # Si la raiz esta llena y es hoja
        # Se crea un nuevo nodo, donde se inserta la raiz
        # después se inserta el nuevo valor y se realiza la separación del nodo
        if r.n == 2 * self.t and r.leaf():  # Raíz esta llena
            s = Node(self.t)
            self.root = s
            s.child[0] = r
            self.bTreeInsertNonFull(s.child[0], k)
            self.bTreeSplitChild(s, 0)

        else:
            # Si la raiz no esta llena
            # inserta el nuevo valor
            self.bTreeInsertNonFull(r, k)

        # Si keys de la raíz excede el máximo número de keys
        # se crea un nuevo nodo y se inserta la raíz como un hijo
        # se realiza la separación de la raíz pasada, con padre "s",
        # para que la media se pase a esta nueva raíz.
        if r.n == 2 * self.t + 1:
            s = Node(self.t)
            self.root = s
            s.child[0] = r
            self.bTreeSplitChild(s, 0)

    # Buscar una llave en el árbol
    def bTreeSearch(self, nodo, k):
        x = nodo  # Nodo en el cual se busca el valor k
        i = 0  # Indice para recorrer las llaves

        if not x:  # Si el nodo en el cual se quiere buscar es None, significa que ya no hay más donde buscar
            return None, None

        # Aumentar el indice mientras se busca el valor k (o
        # algun valor mayor que k)
        while i < x.n and k > x.keys[i]:
            i += 1

        # Si el indice esta dentro de la longitud de keys
        # y k está en el índice i en la lista de keys, el valor
        # a buscar (k) fue encontrado
        if i < x.n and k == x.keys[i]:
            return x, i

        # Si no, seguir buscando
        else:
            if x.child:  # Si el nodo cuenta con elementos en su lista child, buscar en los hijos
                x, i = self.bTreeSearch(x.child[i], k)
                return x, i
            else:  # Si el nodo no cuenta con elementos en su lista child, ya no hay donde buscar
                return None

    # Imprimir los niveles del arbol
    def bTreePrint(self):
        if self.root is None:
            print("Arbol Vacio")
            return
        print("****************************")
        print_rec(self.root, 0)

    # Buscar el nodo padre del nodo que contenga la llave k
    def bTreeSearchParent(self, nodo, k, parent=None):
        x = nodo  # Nodo en el cual se busca el valor
        i = 0  # Indice para recorrer las llaves

        if not x:  # Si el nodo en el cual se quiere buscar es None, significa que ya no hay más donde buscar
            return None

        # Aumentar el indice mientras se busca el valor k (o
        # algun valor mayor que k)
        while i < x.n and k > x.keys[i]:
            i += 1

        # Si el indice esta dentro de la longitud de keys
        # y k está en el índice i en la lista de keys, el valor
        # a buscar (k) fue encontrado
        if i < x.n and k == x.keys[i]:
            return parent

        # Si no, seguir buscando
        else:
            if x.child:  # Si el nodo cuenta con elementos en su lista child, buscar en los hijos
                parent = x  # Guarda al nodo con hijos como padre
                parent = self.bTreeSearchParent(x.child[i], k, parent=parent)  # Llamada recursiva para seguir buscando el padre
                return parent
            else:  # Si el nodo no cuenta con elementos en su lista child, ya no hay donde buscar
                return None

    # Funcion para fusionar las llaves de dos nodos, y una llave extra
    # en un mismo nodo
    def mergeKeys(self, node: Node, key_parent, leaf: Node):
        # node es el nodo en donde se van a colocar el resto de
        # las llaves, tomar su numero de llaves
        node.n = 0

        arr_1 = [key_parent] + leaf.keys  # Arreglo donde se colocar la llave extra y las llaves del otro nodo

        # Quitar los valores None y ordenar el primer arreglo,
        # y colocar el resultado en un arreglo nuevo
        arr_2 = sorted(list(filter(None, arr_1)))

        j = 0  # Contador para el indice del arreglo ordenado

        # Recorrer las llaves del primer nodo e ir insertando
        # los elementos del nuevo arreglo ordenado en cuanto
        # se tope con un valor None
        for i in range(len(node.keys)):
            if node.keys[i] is None:
                node.keys[i] = arr_2[j]
                j += 1

            # Ya al haber insertado los elementos del arreglo
            # a las llaves del nodo, salir del ciclo para
            # evitar IndexError
            if j == len(arr_2):
                break

        # Actualizar el indicador del
        # numero de claves del nodo
        node.calculate_n()

    # Eliminar una llave del árbol de manera iterativa
    def bTreeDelete(self, k):
        # Encontrar el nodo y el índice dentro del nodo, donde
        # se encuentra k (el valor a borrar)
        x, index = self.bTreeSearch(self.root, k)

        # Si k no fue encontrado, salir
        if not x and not index:
            print(f"Valor {k} no encontrado")
            return

        # Si k si fue encontrado, continuar
        else:

            # Si el nodo es hoja
            if x.leaf():
                leaf = x  # Asignar el nodo que contiene k a variable leaf
                leaf.keys.pop(index)  # Sacar k de las llaves del nodo
                leaf.keys.append(None)  # Agregar un espacio None

            # Si el nodo es un nodo intermedio (no hoja)
            else:
                # Buscar suplente para k
                # El valor suplente de k va a ser la primer clave en el
                # nodo hoja al que se llego al hacer el recorrido a la derecha
                # del nodo que contiene k, y recorrer la rama izquierda
                right_of_x = x.child[index+1]  # Agarrar para la derecha de la clave a eliminar
                temp = right_of_x
                while not temp.leaf():
                    # Agarrar para la izquierda hasta topar con un nodo hoja
                    temp = temp.child[0]

                # temp.keys[0] es el suplente de k
                x.keys[index], temp.keys[0] = temp.keys[0], x.keys[index]  # Intercambio de k por la su suplente
                leaf = temp  # hoja = nodo que contiene la clave suplente
                leaf.keys.pop(0)  # Sacar k de las llaves del nodo hoja
                leaf.keys.append(None)  # Agregar un espacio None

            leaf.calculate_n()  # Recalcular el numero de llaves del nodo hoja

            # Si se llega a borrar la unica llave que hay en root
            # (terminar con un arbol vacio), salir
            if leaf.n == 0 and leaf == self.root:
                self.root = None
                return

            # Si hoja es la raiz y cumple con las propiedades/reglas
            # del mínimo de llaves en un nodo, salir
            if leaf == self.root or leaf.n >= self.t:
                return

            # Si hoja NO cumple con las propiedades/reglas
            # del mínimo de llaves en un nodo, continuar
            else:

                # Ciclo que recorre de hoja hacia arriba, para que de
                # forma iterativa se puedan adecuar los nodos para que
                # cumplan con las propiedades/reglas
                while leaf != self.root:

                    # Buscar el padre de hoja, usando como k la primer llave
                    first_of_leaf = leaf.keys[0]
                    parent = self.bTreeSearchParent(self.root, first_of_leaf)

                    # Encontrar hermano izquierdo y derecho de hoja
                    index_of_leaf = parent.child.index(leaf)
                    left_sibling = parent.child[index_of_leaf - 1]
                    right_sibling = parent.child[index_of_leaf + 1]

                    # Si existe el nodo hermano derecho y contiene más claves que el mínimo
                    if right_sibling and right_sibling.n > self.t:
                        # Pasar una clave del hermano derecho a padre, y la clave de padre a hoja
                        # ---> agarrando clave más chica del hermano derecho

                        index_rs = parent.child.index(right_sibling)  # Indice del hermano derecho en la lista de hijos
                        key_parent = parent.keys[index_rs - 1]  # Llave en padre que apunta a hoja
                        parent.keys[index_rs - 1] = right_sibling.keys[0]  # Pasar primer llave del nodo derecho a nodo padre
                        parent.calculate_n()  # Calcular el numero de llaves de nodo padre

                        right_sibling.keys.pop(0)  # Quitar la primera llave del nodo hermnao derecho
                        right_sibling.keys.append(None)  # Agregar un None a las llaves del nodo hermano derecho
                        right_sibling.calculate_n()  # Calcular el numero de llaves del nodo hermano derecho

                        # Si el nodo hermano derecho tiene mas hijos que llaves, pasar
                        # el primer hijo como ultimo hijo de hoja
                        if right_sibling.count_children() - right_sibling.n > 1:
                            first_child = right_sibling.child[0]  # Primer hijo del nodo hermano derecho
                            right_sibling.child.pop(0)  # Quitar primer hijo del nodo hermano derecho
                            right_sibling.child.append(None)  # Agregar un None a los hijos del nodo hermano derecho

                            # Agregar hijo en la ultima posicion posible en la lista de hijos de nodo hoja
                            leaf_last_child, index_leaf_last_child = leaf.grab_last_child()
                            leaf.child[index_leaf_last_child+1] = first_child

                        # Agregar llave del padre a las llaves de hoja
                        leaf.add_key(key_parent)

                        # Si hoja resulta tener hijos, acomodar el orden de los hijos en caso
                        # de ser necesario
                        if not leaf.leaf():
                            leaf.shift_children()

                        # if not right_sibling.leaf():
                        #     right_sibling.shift_children()

                        leaf.calculate_n()  # Calcular el numero de llaves del nodo hoja

                        return  # Salir

                    # Si existe el nodo hermano izquierdo y contiene más claves que el mínimo
                    elif left_sibling and left_sibling.n > self.t:
                        # Pasar una clave del hermano izquierdo a padre, y la clave de padre a hoja
                        # ---> agarrando clave más grande del hermano izquierdo

                        index_ls = parent.child.index(left_sibling)  # Indice del hermano izquierdo en la lista de hijos
                        key_parent = parent.keys[index_ls]  # Llave en padre que apunta a hoja

                        # Tomar la ultima llave y su indice del nodo hermano izquierdo
                        last_key, last_key_index = left_sibling.grab_last_key()
                        left_sibling.keys[last_key_index] = None  # Quitar la ultima llave del nodo hermano izquierdo
                        left_sibling.calculate_n()  # Calcular el numero de llaves del nodo hermano izquierdo

                        # Si el nodo hermano izquierdo tiene mas hijos que llaves, pasar
                        # el ultimo hijo como primer hijo de hoja
                        if left_sibling.count_children() - left_sibling.n > 1:

                            # Ultimo hijo y sus indice del nodo hermano izquierdo
                            last_child, index_last_child = left_sibling.grab_last_child()

                            # Insertar como primer hijo de hoja al ultimo hijo del nodo hermano izquierdo
                            leaf.child.insert(0, last_child)
                            leaf.child.pop()  # Quitar un None de la lista de hijos de hoja

                            # Eliminar el ultimo hijo del nodo hermano izquierdo
                            left_sibling.child[index_last_child] = None

                        parent.keys[index_ls] = last_key  # Pasar la llave del hermano izquierdo a padre
                        parent.calculate_n()  # Calcular el numero de llaves del nodo padre

                        leaf.keys.insert(0, key_parent)  # Pasar la llave de padre a hoja
                        leaf.keys.pop()  # Quitar un None de la lista de llaves de hoja

                        # Si hoja resulta tener hijos, acomodar el orden de los hijos en caso
                        # de ser necesario
                        if not leaf.leaf():
                            leaf.shift_children()

                        # if not left_sibling.leaf():
                        #     left_sibling.shift_children()

                        leaf.calculate_n()  # Calcular el numero de llaves del nodo hoja

                        return  # Salir

                    # Si existe el nodo hermano derecho y NO contiene más claves que el mínimo
                    elif right_sibling:
                        # Fundir en hoja las llaves de hoja y derecho, y ademas
                        # agregar la clave (en padre) que apunta a hoja

                        index_rs = parent.child.index(right_sibling)  # Indice del hermano derecho en la lista de hijos de padre
                        key_parent = parent.keys[index_rs - 1]  # Llave en padre que apunta a hoja

                        # Quitar la llave en padre que apunta a hoja
                        parent.keys.pop(index_rs - 1)
                        parent.keys.append(None)

                        # Fundir/unir las llaves en nodo hoja
                        self.mergeKeys(leaf, key_parent, right_sibling)

                        # Pasar los hijos del nodo hermano derecho como hijos de hoja
                        for child in right_sibling.child:
                            leaf.add_child(child)

                        # Borrar nodo hermano derecho de la lista de hijos de padre
                        parent.child.pop(index_rs)
                        parent.child.append(None)

                        parent.calculate_n()  # Calcular el numero de llaves del nodo padre

                        # Si hoja resulta tener hijos, acomodar el orden de los hijos en caso
                        # de ser necesario
                        if not leaf.leaf():
                            leaf.shift_children()

                        # if not parent.leaf():
                        #     parent.shift_children()

                        leaf.calculate_n()  # Calcular el numero de llaves de hoja

                        # Si el padre de hoja es raiz y no tiene llaves, hoja ahora es la nueva raiz
                        if parent == self.root and parent.n == 0:
                            self.root = leaf
                            return  # Salir

                    # Si existe el nodo hermano izquierdo y NO contiene más claves que el mínimo
                    elif left_sibling:
                        # Fundir en izquierdo las llaves de hoja e izquierdo, y ademas
                        # agregar la clave (en padre) que apunta a hoja

                        index_ls = parent.child.index(left_sibling)  # Indice del nodo hermano izquierdo en la lista de hijos de padre
                        key_parent = parent.keys[index_ls]   # Llave en padre que apunta a hoja

                        # Quitar la llave en padre que apunta a hoja
                        parent.keys.pop(index_ls)
                        parent.keys.append(None)

                        # Fundir/unir las llaves en nodo hermano izquierdo
                        self.mergeKeys(left_sibling, key_parent, leaf)  # fundir/unir

                        # Pasar los hijos de hoja como hijos del nodo hermano izquierdo
                        for child in leaf.child:
                            left_sibling.add_child(child)

                        # Borrar hoja de la lista de hijos de nodo padre
                        parent.child.pop(index_of_leaf)
                        parent.child.append(None)

                        parent.calculate_n()  # Calcular el numero de llaves del nodo padre

                        # Si nodo hermano izquierdo resulta tener hijos, acomodar el orden de los hijos en caso
                        # de ser necesario
                        if not left_sibling.leaf():
                            left_sibling.shift_children()

                        left_sibling.calculate_n()  # Calcular el numero de llaves del nodo hermano izquierdo

                        # Si el padre de hoja es raiz y no tiene llaves
                        # hoja ahora es la nueva raiz
                        if parent == self.root and parent.n == 0:
                            self.root = left_sibling
                            return

                    leaf = parent  # Moverse un nodo hacia arriba

                    # Si hoja cumple con las propiedades, salir
                    if leaf is not None and leaf != self.root and leaf.n >= self.t:
                        return


if __name__ == "__main__":

    arbol = ArbolB(2)
    actual = arbol.bTreeCreate()

    def prueba_facil(arbol):
        keys = [20, 30, 10, 90, 40, 80, 50, 60, 70]

        for node in keys:
            arbol.bTreeInsert(actual, node)

        print(f"\nARBOL INICIAL")
        arbol.bTreePrint()

        print(f"\nBORRANDO 50")
        arbol.bTreeDelete(50)
        arbol.bTreePrint()

        print(f"\nBORRANDO 60")
        arbol.bTreeDelete(60)
        arbol.bTreePrint()

        print(f"\nBORRANDO 10")
        arbol.bTreeDelete(10)
        arbol.bTreePrint()

        print(f"\nBORRANDO 40")
        arbol.bTreeDelete(40)
        arbol.bTreePrint()

        print(f"\nBORRANDO 90")
        arbol.bTreeDelete(90)
        arbol.bTreePrint()

    def prueba_media(arbol):
        for i in range(55):
            arbol.bTreeInsert(actual, i)

        print(f"\nARBOL INICIAL")
        arbol.bTreePrint()

        print(f"\nBORRANDO 54")
        arbol.bTreeDelete(54)
        arbol.bTreePrint()

        print(f"\nBORRANDO 32")
        arbol.bTreeDelete(32)
        arbol.bTreePrint()

        print(f"\nBORRANDO 47")
        arbol.bTreeDelete(47)
        arbol.bTreePrint()

        print(f"\nBORRANDO 44")
        arbol.bTreeDelete(44)
        arbol.bTreePrint()

        print(f"\nBORRANDO 0")
        arbol.bTreeDelete(0)
        arbol.bTreePrint()

        print(f"\nBORRANDO 26")
        arbol.bTreeDelete(26)
        arbol.bTreePrint()

        print(f"\nBORRANDO 34")
        arbol.bTreeDelete(34)
        arbol.bTreePrint()

        print(f"\nBORRANDO 8")
        arbol.bTreeDelete(8)
        arbol.bTreePrint()

        print(f"\nBORRANDO 5")
        arbol.bTreeDelete(5)
        arbol.bTreePrint()

        print(f"\nBORRANDO 20")
        arbol.bTreeDelete(20)
        arbol.bTreePrint()

        print(f"\nBORRANDO 6")
        arbol.bTreeDelete(6)
        arbol.bTreePrint()

        print(f"\nBORRANDO 35")
        arbol.bTreeDelete(35)
        arbol.bTreePrint()

        print(f"\nBORRANDO 30")
        arbol.bTreeDelete(30)
        arbol.bTreePrint()

        print(f"\nBORRANDO 28")
        arbol.bTreeDelete(28)
        arbol.bTreePrint()

        print(f"\nBORRANDO 15")
        arbol.bTreeDelete(15)
        arbol.bTreePrint()

        print(f"\nBORRANDO 50")
        arbol.bTreeDelete(50)
        arbol.bTreePrint()

        print(f"\nBORRANDO 41")
        arbol.bTreeDelete(41)
        arbol.bTreePrint()

        print(f"\nBORRANDO 31")
        arbol.bTreeDelete(31)
        arbol.bTreePrint()

        print(f"\nBORRANDO 1")
        arbol.bTreeDelete(1)
        arbol.bTreePrint()

        print(f"\nBORRANDO 12")
        arbol.bTreeDelete(12)
        arbol.bTreePrint()

        print(f"\nBORRANDO 21")
        arbol.bTreeDelete(21)
        arbol.bTreePrint()

        print(f"\nBORRANDO 11")
        arbol.bTreeDelete(11)
        arbol.bTreePrint()

        print(f"\nBORRANDO 53")
        arbol.bTreeDelete(53)
        arbol.bTreePrint()

        print(f"\nBORRANDO 49")
        arbol.bTreeDelete(49)
        arbol.bTreePrint()

        print(f"\nBORRANDO 48")
        arbol.bTreeDelete(48)
        arbol.bTreePrint()

        print(f"\nBORRANDO 23")
        arbol.bTreeDelete(23)
        arbol.bTreePrint()

        print(f"\nBORRANDO 17")
        arbol.bTreeDelete(17)
        arbol.bTreePrint()

        print(f"\nBORRANDO 38")
        arbol.bTreeDelete(38)
        arbol.bTreePrint()

        print(f"\nBORRANDO 2")
        arbol.bTreeDelete(2)
        arbol.bTreePrint()

        print(f"\nBORRANDO 29")
        arbol.bTreeDelete(29)
        arbol.bTreePrint()

        print(f"\nBORRANDO 18")
        arbol.bTreeDelete(18)
        arbol.bTreePrint()

        print(f"\nBORRANDO 40")
        arbol.bTreeDelete(40)
        arbol.bTreePrint()

        print(f"\nBORRANDO 10")
        arbol.bTreeDelete(10)
        arbol.bTreePrint()

        print(f"\nBORRANDO 22")
        arbol.bTreeDelete(22)
        arbol.bTreePrint()

        print(f"\nBORRANDO 39")
        arbol.bTreeDelete(39)
        arbol.bTreePrint()

        print(f"\nBORRANDO 33")
        arbol.bTreeDelete(33)
        arbol.bTreePrint()

        print(f"\nBORRANDO 16")
        arbol.bTreeDelete(16)
        arbol.bTreePrint()

        print(f"\nBORRANDO 45")
        arbol.bTreeDelete(45)
        arbol.bTreePrint()

        print(f"\nBORRANDO 52")
        arbol.bTreeDelete(52)
        arbol.bTreePrint()

        print(f"\nBORRANDO 27")
        arbol.bTreeDelete(27)
        arbol.bTreePrint()

        print(f"\nBORRANDO 14")
        arbol.bTreeDelete(14)
        arbol.bTreePrint()

        print(f"\nBORRANDO 4")
        arbol.bTreeDelete(4)
        arbol.bTreePrint()

        print(f"\nBORRANDO 13")
        arbol.bTreeDelete(13)
        arbol.bTreePrint()

        print(f"\nBORRANDO 46")
        arbol.bTreeDelete(46)
        arbol.bTreePrint()

        print(f"\nBORRANDO 36")
        arbol.bTreeDelete(36)
        arbol.bTreePrint()

        print(f"\nBORRANDO 9")
        arbol.bTreeDelete(9)
        arbol.bTreePrint()

        print(f"\nBORRANDO 24")
        arbol.bTreeDelete(24)
        arbol.bTreePrint()

        print(f"\nBORRANDO 19")
        arbol.bTreeDelete(19)
        arbol.bTreePrint()

        print(f"\nBORRANDO 3")
        arbol.bTreeDelete(3)
        arbol.bTreePrint()

        print(f"\nBORRANDO 25")
        arbol.bTreeDelete(25)
        arbol.bTreePrint()

        print(f"\nBORRANDO 43")
        arbol.bTreeDelete(43)
        arbol.bTreePrint()

        print(f"\nBORRANDO 51")
        arbol.bTreeDelete(51)
        arbol.bTreePrint()

        print(f"\nBORRANDO 42")
        arbol.bTreeDelete(42)
        arbol.bTreePrint()

        print(f"\nBORRANDO 37")
        arbol.bTreeDelete(37)
        arbol.bTreePrint()

        print(f"\nBORRANDO 7")
        arbol.bTreeDelete(7)
        arbol.bTreePrint()

        print(f"\nBORRANDO 154")
        arbol.bTreeDelete(154)
        arbol.bTreePrint()

    def prueba_random(arbol):
        rand_list = random.sample(range(100), 40)

        for number in rand_list:
            arbol.bTreeInsert(actual, number)

        print(f"\nARBOL INICIAL")
        arbol.bTreePrint()

        num_pruebas_borrado = 10
        for i in range(num_pruebas_borrado):
            random_index = random.randint(0, len(rand_list) - 1)
            num_to_delete = rand_list[random_index]
            print(f"\nBORRANDO {num_to_delete}")
            arbol.bTreeDelete(num_to_delete)
            arbol.bTreePrint()

    # prueba_media(arbol, actual)
    # prueba_facil(arbol)
    # prueba_random(arbol)

    def examen(arbol):
        arbol.bTreeInsert(actual, 10)
        arbol.bTreeInsert(actual, 20)
        arbol.bTreeInsert(actual, 65)
        arbol.bTreeInsert(actual, 73)
        arbol.bTreeInsert(actual, 5)
        arbol.bTreeInsert(actual, 9)
        arbol.bTreeInsert(actual, 12)
        arbol.bTreeInsert(actual, 18)
        arbol.bTreeInsert(actual, 25)
        arbol.bTreeInsert(actual, 52)
        arbol.bTreeInsert(actual, 67)
        arbol.bTreeInsert(actual, 69)
        arbol.bTreeInsert(actual, 70)
        arbol.bTreeInsert(actual, 72)
        arbol.bTreeInsert(actual, 92)
        arbol.bTreeInsert(actual, 99)

        arbol.bTreePrint()

        arbol.bTreeInsert(actual, 68)

        arbol.bTreePrint()

    examen(arbol)