#  Nombre Alumno: Ximena González
#  Fecha: 28 Octubre 2021
#  Examen Parcial 2

class Node:
    """Clase para representar un nodo con
       sus respectivos atributos"""
    def __init__(self, data):
        self.data = data  # datos del nodo
        self.child_right = None  # hijo derecho del nodo
        self.child_left = None  # hijo izquierdo del nodo
        self.is_root = False  # indicador si es nodo raiz
        self.is_right = False  # indicador si es hijo derecho
        self.is_left = False  # indicador si es hijo izquierdo
        self.parent = None  # indicador si es padre


class BinaryTree:
    """Clase para representar un arbol binario con
       sus respectivos metodos y atributos"""

    def __init__(self):
        self.root = None  # la raiz del arbol
        self.weight = 0  # peso del arbol que indica cuantos nodos tiene

    # Revisar si el arbol esta vacio checando
    # si tiene raiz o no
    def is_empty(self):
        if self.root is None:
            return True
        return False

    # Recorrer el arbol para hallar en que posicion y de que lado insertar un nuevo nodo
    def get_place(self, value):
        aux = self.root  # aux es el nodo con el que se recorre el arbol

        # mientras aux no sea None
        while aux:
            temp = aux  # recuerda el ultimo nodo (el nodo padre) para insertar el nuevo nodo
            if value <= aux.data:  # irse a la parte izquierda
                aux = aux.child_left
                side = "left"  # side indica de que lado debe insertarse el nuevo nodo
            else:  # irse a la parte derecha
                aux = aux.child_right
                side = "right"

        return temp, side  # regresar el nodo padre del nuevo nodo y el lado donde debe insertarse

    # Insertar un nuevo nodo en el arbol
    def insert(self, value):
        new_node = Node(value)  # crear el nuevo nodo

        # si el arbol esta vacio, el nuevo nodo a insertar se
        # convierte en la raiz del arbol
        if self.is_empty():
            new_node.is_root = True
            self.root = new_node
        # si el arbol no esta vacio, recorrer (con ayuda
        # de la funcion get_place) el arbol hasta hallar
        # la posicion en donde corresponde el nuevo nodo
        else:
            position, side = self.get_place(value)

            # insertar en el lado derecho del padre del nuevo nodo
            if side == "right":
                position.child_right = new_node
                new_node.is_right = True

            # insertar en el lado izquierdo del padre del nuevo nodo
            else:
                position.child_left = new_node
                new_node.is_left = True

            # definir el atributo de padre del nuevo nodo
            new_node.parent = position

        # incrementar por 1 el peso del arbol
        self.weight += 1

    # Buscar en el arbol un nodo
    def search(self, root_node, target_value):

        # si el arbol esta vacio, no hay nada
        # que buscar o si el valor a buscar
        # no existe
        if root_node is None:
            # print(f"Nodo {target_value} no hallado o arbol está vacio")
            return None
        else:
            if root_node.data == target_value:  # si es igual, regresar el nodo
                # print(f"Nodo hallado: {root_node.data}")
                return root_node
            elif target_value <= root_node.data:  # si el valor a buscar es menor que el nodo, moverse a la izquierda
                return self.search(root_node.child_left, target_value)
            else:
                return self.search(root_node.child_right, target_value)  # si el valor a buscar es mayor que el nodo, moverse a la derecha

    # Encontrar el nodo mas grande del subarbol izquierdo de un nodo
    def max_node_value(self, node):

        current = node  # nodo actual
        child_node = current.child_left  # nodo donde empieza el subarbol izquierdo del nodo actual

        # recorrer hacia la derecha hasta hallar el nodo mas grande
        # del subarbol izquierdo
        while child_node.child_right is not None:
            child_node = child_node.child_right

        return child_node  # regresar el nodo mayor del subarbol izquierdo

    # Funcion para checar si tiene hijos, cuantos hijos y de que lado
    def children(self, target_node):
        node = self.search(self.root, target_node)  # buscar el nodo

        if node.child_left and node.child_right:  # si el nodo tiene los dos hijos
            children_indicator = "2"
        elif node.child_left and not node.child_right:  # si el nodo tiene un hijo izquierdo
            children_indicator = "1L"
        elif node.child_right and not node.child_left:  # si el nodo tiene un hijo derecho
            children_indicator = "1R"
        else:
            children_indicator = None  # si el nodo no tiene hijos

        return children_indicator

    # Eliminar un nodo
    def delete_node(self, target_value):
        # buscar nodo a eliminar
        current = self.search(self.root, target_value)

        # si el nodo no existe en el arbol, no hay nada que eliminar
        if current is None:
            print(f"Nodo {target_value} no hallado o arbol esta vacio")
            return None
        # si el nodo si existe, encontrar las condicion de los hijos
        # del nodo a eliminar
        else:
            children = self.children(target_value)

            # Caso 1: El nodo a eliminar es un nodo hoja (sin hijos)
            if children is None:
                # si el nodo actual no es la raiz,
                # identificar si es el hijo izquierdo
                # o derecho, y eliminarlo cambiando el puntero de
                # hijo (izquierdo o derecho) del padre a None
                if not current.is_root:
                    if current.parent.child_left == current:
                        current.parent.child_left = None
                    else:
                        current.parent.child_right = None
                # si el nodo actual es raiz, eliminar
                # la raiz cambiandolo a None
                else:
                    self.root = None

            # Caso 2: El nodo a eliminar es un nodo con solo un hijo
            elif children == "1L" or children == "1R":  # identificar si el hijo del nodo a eliminar es izq o der
                if children == "1L":
                    child = current.child_left
                else:
                    child = current.child_right

                if not current.is_root:  # si el nodo a eliminar no es raiz
                    if current == current.parent.child_left:  # si el nodo a eliminar es hijo izq, hacer que su hijo tome su lugar como hijo izq
                        current.parent.child_left = child
                        child.is_left = True
                    else:
                        current.parent.child_right = child  # si el nodo a eliminar es hijo der, hacer que su hijo tome su lugar como hijo der
                        child.is_right = True
                    child.parent = current.parent  # cambiar el puntero de parent del nodo nieto para que apunte al nodo abuelo
                else:  # si el nodo a eliminar si es raiz, hacer que el hijo tome el lugar de reaiz y asignar los atributos correspondientes
                    self.root = child
                    child.is_root = True
                    self.root.parent = None

            # Caso 3: El nodo a eliminar es un nodo con dos hijos
            else:
                # llamada para hallar el nodo mayor del subarbol izquierdo
                # (que es el sucesor del nodo a eliminar),
                # que tomara el lugar del nodo a eliminar
                successor = self.max_node_value(current)
                print("Sucesor es:", successor.data)

                val = successor.data  # guardar el valor del sucesor

                # llamada recursiva para eliminar el sucesor (que viene siendo un
                # nodo hoja ya que es el mas grande del subarbol izquierdo)
                self.delete_node(successor.data)
                self.weight += 1  # agregar uno para contrarrestar la llamada recursiva a delete

                current.data = val  # copiar el valor del sucesor en el nodo actual

        self.weight -= 1  # disminuir por uno el peso del arbol

    # hallar la altura del arbol
    def get_height(self, root: Node):
        if root is None:  # si no hay raiz el aborl esta vacio
            return 0

        # si la raiz tiene hijos, contar la altura en ambos subarboles
        elif root.child_left and root.child_right:
            return 1 + max(self.get_height(root.child_left), self.get_height(root.child_right))

        # si la raiz solo tiene hijo izquierdo, contar la altura en el subarbol izquierdo
        elif root.child_left:
            return 1 + self.get_height(root.child_left)

        # si la raiz solo tiene hijo derecho, contar la altura en el subarbol derecho
        elif root.child_right:
            return 1 + self.get_height(root.child_right)

        # si solo la raiz esta presente, la altura es 1
        else:
            return 1

    # regresar el peso del arbol
    def get_weight(self):
        if self.root is None:
            return 0

        return self.weight

    # hallar el valor menor en el arbol
    def get_min_node(self, root: Node):
        if root is None:  # si no hay raiz el arbol esta vacio
            print("El arbol esta vacio")
            return

        # recorrer el subarbol izquierdo del arbol hasta encontrar el
        # nodo hoja que tenga el valor menor
        current = root
        while current.child_left:
            current = current.child_left

        print(f"Nodo minimo: {current.data}")

    # hallar el valor maximo en el arbol
    def get_max_node(self, root: Node):
        if root is None:  # si no hay raiz el arbol esta vacio
            print("El arbol esta vacio")
            return

        # recorrer el subarbol derecho del arbol hasta encontrar el
        # nodo hoja que tenga el valor mayor
        current = root
        while current.child_right:
            current = current.child_right

        print(f"Nodo maximo: {current.data}")

    def in_order(self, node):
        # Imprimir nodos del arbol en orden:
        # izquierda - raiz - derecho
        if node:
            self.in_order(node.child_left)
            print(node.data)
            self.in_order(node.child_right)

    def post_order(self, node):
        # Imprimir nodos del arbol en orden:
        # izquierda - derecha - raiz
        if node:
            self.post_order(node.child_left)
            self.post_order(node.child_right)
            print(node.data)

    def pre_order(self, node):
        # Imprimir nodos del arbol en orden:
        # raiz - izquierda - derecha
        if node:
            print(node.data)
            self.pre_order(node.child_left)
            self.pre_order(node.child_right)

    # imprimir el arbol y sus nodos
    def display(self, node: Node, level=0):
        if node is not None:
            self.display(node.child_right, level + 1)
            print(' ' * 4 * level + '->', node.data)
            self.display(node.child_left, level + 1)

    # haciendo el espejo del arbol
    # recorriendo el arbol por niveles e intercambiando
    # los hijos de cada nodo
    def mirror(self, root: Node):
        if not root:  # si no hay raiz el arbol esta vacio
            return

        lista_nodos = [root]  # lista que guarda los valores de los nodos actuales (nodos hermanos por recorrer por nivel)

        while len(lista_nodos) != 0:
            # sacar el primer nodo (primer hermano) de la lista para realizar
            # intercambio de sus hijos izquierda y derecho
            curr = lista_nodos.pop(0)

            # intercambiar hijos izquierdo y derecho del nodo
            curr.child_left, curr.child_right = curr.child_right, curr.child_left

            # agregar los nuevos hijos izquierdo y derechos a la lista
            # para examinar los hijos de esos nodos y volver a hacer el
            # intercambio
            if curr.child_left:
                lista_nodos.append(curr.child_left)
            if curr.child_right:
                lista_nodos.append(curr.child_right)


binary_tree = BinaryTree()

# Basandote en la imagen del arbol realiza manualmente el recorrido PRE-ORDER.
array = [67, 44, 22, 9, 37, 39, 50, 47, 85, 73, 90, 88, 94]
print("Valores acomodados en pre orden")
print(array)

# Insertar en una lista, el recorrido PRE-ORDER, y con la ayuda de tu codigo Python, inserta los nodos para que crees el arbol.
for i in array:
    binary_tree.insert(i)
print(f"\nRaiz: {binary_tree.root.data}")
print(f"Hijo izquierdo raiz: {binary_tree.root.child_left.data}")
print(f"Hijo derecho raiz: {binary_tree.root.child_right.data}")

# Crea un Metodo para calcular la altura del árbol, e imprimile indicandoque es la altura.
print(f"\nAltura: {binary_tree.get_height(binary_tree.root)}")

# Crea un Metodo para calcular el valor Mayor y el valor Menor del árbol e imprimelo.
print()
binary_tree.get_max_node(binary_tree.root)
binary_tree.get_min_node(binary_tree.root)

# Realiza un recorrido IN-ORDER, e imprimelo en pantalla, con un mensaje que indique que recorrido es.
print("\nRecorrido en in-order")
binary_tree.in_order(binary_tree.root)

# Borra los siguientes datos, e indica en cada caso si el nodo a borrar es hoja, nodo con un hijo, y en caso de tener dos hijos cual sera el nodo sucesor.
# 73 66 50 47 39 94
borrar = [73, 67, 50, 47, 39, 94]  # lista de nodos a borrar
for num in borrar:
    print(f"\nValor a borrar: {num}")
    search_node = binary_tree.search(binary_tree.root, num)  # buscar si el nodo existe
    if search_node:
        hijos = binary_tree.children(num)  # buscar la cantidad de hijos que tiene
        if hijos is None:
            print(f"{num} es un nodo hoja")
        elif hijos == "1L" or hijos == "1R":
            print(f"{num} es un nodo con un hijo")
        else:
            print(f"{num} es un nodo con dos hijos")
        binary_tree.delete_node(num)  # eliminar el nodo
    else:
        print("Nodo no hallado")  # el nodo no fue hallado en el arbol

# Crea un Método para que intercambies la posición de los nodos, CREA UN METODO ESPEJO, para intercambiar la posicion de los valores en el arbol, e imprimelo IN_ORDER
print()
binary_tree.mirror(binary_tree.root)
print("Despues de espejeado, recorrido in-order")
binary_tree.in_order(binary_tree.root)
