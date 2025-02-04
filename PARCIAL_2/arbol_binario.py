# Implementacion de arbol binario

# Ximena González

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

                val = successor.data  # guardar el valor del sucesor

                # llamada recursiva para eliminar el sucesor (que viene siendo un
                # nodo hoja ya que es el mas grande del subarbol izquierdo)
                self.delete_node(successor.data)
                self.weight += 1  # agregar uno para contrarrestar la llamada recursiva a delete

                current.data = val  # copiar el valor del sucesor en el nodo actual

        self.weight -= 1  # disminuir por uno el peso del arbol

    def get_height(self, root: Node):

        if root is None:
            return 0

        elif root.child_left and root.child_right:
            return 1 + max(self.get_height(root.child_left), self.get_height(root.child_right))

        elif root.child_left:
            return 1 + self.get_height(root.child_left)

        elif root.child_right:
            return 1 + self.get_height(root.child_right)

        else:
            return 1

    def get_weight(self):
        if self.root is None:
            return 0

        return self.weight

    def print_leaf_nodes(self, root:Node):
        if root is None:
            return 0

        if not root.child_left and not root.child_right:
            print(root.data)
            return 1

        else:
            return self.print_leaf_nodes(root.child_left) + self.print_leaf_nodes(root.child_right)

    def get_min_node(self, root: Node):
        if root is None:
            print("El arbol esta vacio")
            return

        current = root
        while current.child_left:
            current = current.child_left

        print(f"Nodo minimo: {current.data}")
        return

    def get_nonleaf_nodes(self, root: Node):

        if root is None:
            return 0

        if root.child_left is None and root.child_right is None:
            return 0

        return 1 + self.get_nonleaf_nodes(root.child_left) + self.get_nonleaf_nodes(root.child_right)

    def get_max_node(self, root: Node):
        if root is None:
            print("El arbol esta vacio")
            return

        current = root
        while current.child_right:
            current = current.child_right

        print(f"Nodo maximo: {current.data}")
        pass

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


# Pruebas
binary_tree = BinaryTree()






# binary_tree.insert(44)

# BORRANDO CUANDO SOLO LA RAIZ ESTA EN EL ARBOL
# 44
# binary_tree.delete_node(44)  # borrar la raiz (y el unico nodo en el arbol)
# binary_tree.pre_order(binary_tree.root)  # imprime nada (no corre ya que no hay nodos que imprimir)
# print(binary_tree.root)  # imprime None porque no hay raiz
# print(binary_tree.is_empty())  # imprime True porque el arbol esta vacio

# BORRANDO LA RAIZ CUANDO LA RAIZ TIENE UN HIJO
#     44
#    /
#  10
# binary_tree.insert(10)  # insertando hijo izquierdo a la raiz
# binary_tree.pre_order(binary_tree.root)  # imprimiendo contenidos de arbol (44 y 10)
# binary_tree.delete_node(44)  # borrar la raiz (convirtiendo a 10 en la nueva raiz)
# print()
# binary_tree.pre_order(binary_tree.root) # imprime contenidos de arbol (solo la nueva raiz que es 10)
# print(f"Raíz: {binary_tree.root.data}")  # imprime que en la clase de arbol se vio reflejado el cambio de raiz
# print(f"Papá Raíz: {binary_tree.root.parent}")  # imprime None ya que al convertirse en raiz y
#                                                 # eliminar el 44, el 10 pierde al 44 en su puntero de parent

# BORRAR UN NODO CON DOS HIJOS
#                      44
#                /           \
#              10            50
#            /    \          /
#           8     12        49
#                   \       /
#                   14     47
#                     \
#                     24
# binary_tree.insert(10)
# binary_tree.insert(50)
# binary_tree.insert(8)
# binary_tree.insert(12)
# binary_tree.insert(14)
# binary_tree.insert(24)
# binary_tree.insert(49)
# binary_tree.insert(47)
# binary_tree.pre_order(binary_tree.root)  # imprimendo contenidos de arbol sin modificacion aun
# binary_tree.delete_node(10)  # nodo con dos hijos (hijos son 8 y 12)
# print()
# binary_tree.pre_order(binary_tree.root)  # imprimiendo contenidos de arbol (ya sin el 10)
# sucesor_del_10 = binary_tree.search(binary_tree.root, 8)  # sucesor del 10 es el 8 ya que es el mayor del subarbol izquierdo del 10
# print()
# print(f"Sucesor del 10 (quien tomo lugar del 10): {sucesor_del_10.data}")  # imprime 8 (sucesor del 10)
# print(f"8 ahora es hijo izquierdo: {sucesor_del_10.is_left}")  # imprime True porque el 8 tomo el lugar del 10 (que era hijo izquierdo del 44)
# print(f"Papá del 8: {sucesor_del_10.parent.data}")  # imprime 44 porque tomo el lugar del 10, cuyo papá era 44
# print(f"8 y sus hijos:")
# binary_tree.pre_order(sucesor_del_10) # imprime 8, 12, 14, 24 porque mantuvo el puntero de los hijos del 10

# BORRAR UN NODO HOJA
#     44
#    /  \
#  10    50
# binary_tree.insert(10)
# binary_tree.insert(50)
# binary_tree.pre_order(binary_tree.root)  # imprimendo contenidos de arbol sin modificacion aun
# binary_tree.delete_node(50)  # nodo hoja (del lado derecho)
# print()
# binary_tree.pre_order(binary_tree.root)  # imprimendo contenidos de arbol ahora sin el 50 (nodo hoja)
# print(f"Hijo derecho de raiz {binary_tree.root.data}: {binary_tree.root.child_right}")  # imprime None porque se elimino el nodo hoja (50) que era hijo derecho del 44 (raiz)

# BORRAR UN NODO CON UN HIJO A LA IZQUIERDA
#                      44
#                /           \
#              10            50
#            /    \          /
#           8     12        49
# binary_tree.insert(10)
# binary_tree.insert(50)
# binary_tree.insert(8)
# binary_tree.insert(12)
# binary_tree.insert(49)
# binary_tree.pre_order(binary_tree.root)  # imprimendo contenidos de arbol sin modificacion aun
# binary_tree.delete_node(50)  # nodo con un hijo a la izquierda (hijo es 49)
# print()
# binary_tree.pre_order(binary_tree.root)  # imprimendo contenidos de arbol ahora sin el 50
# hijo_izquierdo_de_eliminado = binary_tree.search(binary_tree.root, 49)  # hijo izquierdo del nodo eliminado
# print(f"Hijo izquierdo del nodo eliminado: {hijo_izquierdo_de_eliminado.data}")  # imprime 49
# print(f"Nuevo papá del hijo izquierdo del nodo eliminado: {hijo_izquierdo_de_eliminado.parent.data}")  #imprime 44 porque el papa del 50 era 44, pero ahora el hijo izquierdo (49) toma su lugar, haciendo a su nuevo papá el 44
# print(f"Hijo izquierdo ahora es hijo derecho: {hijo_izquierdo_de_eliminado.is_right}")  # imprime True porque 50 era hijo derecho de 44, pero ahora el 49 toma el lugar del 50, haciendolo el hijo derecho de 44
# print(f"Hijo derecho del nuevo papá del hijo izquierdo del nodo eliminado: {hijo_izquierdo_de_eliminado.parent.child_right.data}")  # imprime 49 porque el puntero de hijo derecho del 44 cambio de 50 a 49

# BORRAR UN NODO CON UN HIJO A LA DERECHA
#                      44
#                /           \
#              10            50
#            /    \          /
#           8     12        49
#                   \
#                   14
# binary_tree.insert(10)
# binary_tree.insert(50)
# binary_tree.insert(8)
# binary_tree.insert(12)
# binary_tree.insert(49)
# binary_tree.insert(14)
# binary_tree.pre_order(binary_tree.root)  # imprimendo contenidos de arbol sin modificacion aun
# binary_tree.delete_node(12)  # nodo con un hijo a la derecha (hijo es 14)
# print()
# binary_tree.pre_order(binary_tree.root)  # imprimendo contenidos de arbol ahora sin el 12
# hijo_derecho_de_eliminado = binary_tree.search(binary_tree.root, 14)  # hijo derecho del eliminado
# print(f"Hijo derecho del nodo eliminado: {hijo_derecho_de_eliminado.data}")  # imprime 14
# print(f"Nuevo papá del hijo derecho del nodo eliminado: {hijo_derecho_de_eliminado.parent.data}")  #imprime 10 porque el papa del eliminado era 10, pero ahora el 14 tomo su lugar, cambiando su puntero de parent
# print(f"Hijo derecho sigue siendo hijo derecho: {hijo_derecho_de_eliminado.is_right}")  # imprime True porque 12 era hijo derecho de 10, y 14 tomo su lugar como hijo derecho
# print(f"Hijo derecho del nuevo papá del hijo derecho del nodo eliminado: {hijo_derecho_de_eliminado.parent.child_right.data}")  # imprime 14 porque el puntero de hijo derecho del 10 cambio de 10 a 14

# Ultima modificacion 14 Octubre 2021

