"""
Clase para representar un nodo en un arbol AVL
"""
class Node:
    def __init__(self, data):
        self.data = data  # datos del nodo
        self.child_right = None  # hijo derecho del nodo
        self.child_left = None  # hijo izquierdo del nodo
        self.is_root = False  # indicador si es nodo raiz
        self.is_right = False  # indicador si es hijo derecho
        self.is_left = False  # indicador si es hijo izquierdo
        self.parent = None  # indicador cual es su padre

"""
Clase para representar un árbol AVL 
con sus respectivos
atributos y métodos
"""
class AVL_Tree:
    def __init__(self):
        self.root = None
        self.weight = 0

    # Rotacion a la derecha a partir del nodo z
    def right_rotate(self, z: Node):
        #         z                        y
        #        / \                    /     \
        #       y   t4                 x       z
        #      / \       --->        /  \    /   \
        #     x  t3                 t1   t2 t3   t4
        #    / \
        #   t1  t2
        sub_root = z.parent  # padre del nodo del cual se inicia la rotacion
        y = z.child_left  # hijo del nodo del cual se inicia la rotacion
        t3 = y.child_right  # guardar el hijo derecho que pueda tener el hijo del nodo del cual se inicia la rotacion

        # Rotacion (cambio de nodo padre e hijo)
        y.child_right = z  # mover el hijo del nodo del cual se inicia la rotacion, para que ahora se convierta en raiz

        z.is_right = True  # z pasa a ser hijo derecho de y
        z.is_left = False  # z ya no es hijo izquierdo (en caso de haberlo sido)
        z.parent = y  # cambiar puntero de padre del nodo del cual se inicia la rotacion

        z.child_left = t3  # pasar los hijo del nodo que queda como raiz como hijos del nodo que anteriormente era raiz

        # si y tiene un hijo, cambiar sus respectivos punteros
        if t3 is not None:
            t3.parent = z  # el papá de t3 ahora es z
            t3.is_left = True  # t3 pasa a ser hijo izquierdo de z
            t3.is_right = False  # t3 ya no es hijo derecho de y

        y.parent = sub_root  # el papá de z ahora es papá de y

        # si z no tenía papá, significa que era raíz,
        # pero como y tomó el lugar de z, ahora y es raíz
        if y.parent is None:
            self.root = y
        else:
            if y.parent.child_left == z:  # si z era hijo izquierdo, hacer que y ahora sea hijo izquierdo
                y.parent.child_left = y
                y.is_left = True
                y.is_right = False
            else: # si z era hijo derecho, hacer que y ahora sea hijo derecho
                y.parent.child_right = y
                y.is_right = True
                y.is_left = False

    # Rotacion a la izquierda a partir del nodo z
    def left_rotate(self, z: Node):

        #      z                                y
        #    /   \                           /     \
        #   t1    y                         z       x
        #        / \          ------>      / \     / \
        #       t2  x                     t1 t2   t3  t4
        #          / \
        #         t3  t4
        sub_root = z.parent  # padre del nodo del cual se inicia la rotacion
        y = z.child_right  # hijo del nodo del cual se inicia la rotacion
        t2 = y.child_left   # guardar el hijo izquierdo que pueda tener el hijo del nodo del cual se inicia la rotacion

        # Rotacion (cambio de nodo padre e hijo)
        y.child_left = z  # hacer que y tome el lugar de z cambiando el puntero de su hijo izquierdo

        z.is_left = True  # z ahora se convierte el hijo izquierdo de y
        z.is_right = False  # z ahora ya no es hijo derecho (en caso de serlo)
        z.parent = y  # el papá de z ahora es y

        z.child_right = t2  # z ahora adopta como hijo derecho el hijo izquierdo de y

        # si y tiene un hijo, cambiar sus respectivos punteros
        if t2 is not None:
            t2.parent = z  # el papá de t2 ahora es z
            t2.is_right = True  # t2 ahora es hijo derecho de z
            t2.is_left = False  # t2 ya no es hijo izquierdo de y

        y.parent = sub_root  # el papá de z ahora es papá de y

        # si z no tenía papá, significa que era raíz,
        # pero como y tomó el lugar de z, ahora y es raíz
        if y.parent is None:
            self.root = y
        else:  # si z si tenía papá, cambiar los punteros del papá para que ahora apunten a y
            if y.parent.child_left == z:  # si z era hijo izquierdo, hacer que y ahora sea hijo izquierdo
                y.parent.child_left = y
                y.is_left = True
                y.is_right = False
            else: # si z era hijo derecho, hacer que y ahora sea hijo derecho
                y.parent.child_right = y
                y.is_right = True
                y.is_left = False

    # nodo mas alto
    def taller_child(self, cur_node):
        # guardar las alturas del hijo izquierdo e hijo derecho del nodo actual
        left = self.get_height(cur_node.child_left)
        right = self.get_height(cur_node.child_right)

        # regresar el más alto de los dos
        if left >= right:
            return cur_node.child_left
        else:
            return cur_node.child_right

    # regresar la altura de un nodo dado
    def get_height(self, node: Node):
        if node:
            return max(self.get_height(node.child_left), self.get_height(node.child_right)) + 1
        return 0

    # funcion auxiliar de insertar
    def inspect_insertion(self, cur_node: Node, path=[]):

        # cuando se llege al nodo raiz, la recursividad se detiene
        if cur_node.parent is None:
            return

        # el path guarda los nodos que se han traversado
        path = [cur_node] + path

        # alturas de los hijos izquierdos y derechos del papá del nodo actual
        left_height = self.get_height(cur_node.parent.child_left)
        right_height = self.get_height(cur_node.parent.child_right)

        print(f"Altura izq: {left_height} y derecha: {right_height}")

        # comparar la diferencia entre las alturas para verificar si el papá
        # del nodo actual está balanceado
        # si la diferencia (el factor de balance) es mayor a 1, hay un desbalance
        if abs(left_height - right_height) > 1:
            # rebalancear
            # path[0] = z path[1] = y path[2] = x
            # z es el nodo que esta en desbalance
            # por lo que se pasan para un rebalance (segun toque la rotacion)
            path = [cur_node.parent] + path
            self.rebalance_node(path[0], path[1], path[2])
            return  # al insertar solo se necesita un rebalance para balancear el árbol (si es que se necesita un rebalance)

        # llamada recursiva para moverse hacia arriba en el árbol
        self.inspect_insertion(cur_node.parent, path)

    def inspect_deletion(self, cur_node: Node):

        # cuando se llege al nodo raiz, la recursividad se detiene
        if cur_node is None:
            return

        # alturas de los hijos izquierdos y derechos del nodo actual
        left_height = self.get_height(cur_node.child_left)
        right_height = self.get_height(cur_node.child_right)

        # comparar la diferencia entre las alturas para verificar si el
        # nodo actual está balanceado
        # si la diferencia (el factor de balance) es mayor a 1, hay un desbalance
        if abs(left_height - right_height) > 1:
            # hallar los nodos y y x que le siguen a z para realizar un
            # rebalanceo con la rotación según sea necesaria
            y = self.taller_child(cur_node)
            x = self.taller_child(y)
            self.rebalance_node(cur_node, y, x)

        # llamada recursiva para moverse hacia arriba en el árbol
        self.inspect_deletion(cur_node.parent)

    # rebalancear un nodo con rotaciones
    def rebalance_node(self, z: Node, y: Node, x: Node):
        # si los tres nodos están inclinados a la derecha
        if y == z.child_left and x == y.child_left:
            self.right_rotate(z)

        # hacer una rotacion doble a la derecha
        elif y == z.child_left and x == y.child_right:
            self.left_rotate(y)
            self.right_rotate(z)

        # si los tres nodos están inclinados a la izquierda
        elif y == z.child_right and x == y.child_right:
            self.left_rotate(z)

        # hacer una rotacion doble a la izquierda
        elif y == z.child_right and x == y.child_left:
            self.right_rotate(y)
            self.left_rotate(z)

        else:
            raise Exception("z, y, x configuracion del nodo no reconocida")

    # Buscar en el arbol un nodo
    def search(self, root_node, target_value):

        # si el arbol esta vacio, no hay nada
        # que buscar o si el valor a buscar
        # no existe
        if root_node is None:
            return None
        else:
            if root_node.data == target_value:  # si es igual, regresar el nodo
                return root_node
            elif target_value <= root_node.data:  # si el valor a buscar es menor que el nodo, moverse a la izquierda
                return self.search(root_node.child_left, target_value)
            else:
                return self.search(root_node.child_right, target_value)  # si el valor a buscar es mayor que el nodo, moverse a la derecha

    # obtener el factor de balance de un nodo dado
    # con la formula altura subarbol derecho - altura subarbol izquierdo
    def get_balance(self, root: Node):
        if root is None:
            return 0
        return self.get_height(root.child_left) - self.get_height(root.child_right)

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

    # insertar un nodo en el arbol AVL
    def insert(self, value):
        new_node = Node(value)  # crear nuevo nodo

        # si no hay raiz, hacer el nuevo nodo
        # la raiz
        if self.root is None:
            self.root = new_node
            new_node.is_root = True
        # si ya existe una raiz, ubicar la posicion y el
        # lado donde se insertaria el nuevo nodo
        else:
            position, side = self.get_place(value)
            # insertar el nodo donde corresponda, ya sea
            # lado izquierdo o lado derecho
            if side == "right":
                position.child_right = new_node
                new_node.is_right = True
            else:
                position.child_left = new_node
                new_node.is_left = True

            new_node.parent = position  # cambiar el puntero de papá del nuevo nodo
            self.inspect_insertion(new_node)  # inspeccionar el árbol para checar que esté balanceado

        self.weight += 1  # incrementar el peso por 1

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
                    self.inspect_deletion(current.parent)  # inspeccionar que el arbol se mantenga balanceado
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
                    self.inspect_deletion(current.parent)  # inspeccionar que el arbol se mantenga balanceado
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
                self.inspect_deletion(successor.parent)  # inspeccionar que el arbol se mantenga balanceado
                self.weight += 1  # agregar uno para contrarrestar la llamada recursiva a delete

                current.data = val  # copiar el valor del sucesor en el nodo actual

        self.weight -= 1  # disminuir por uno el peso del arbol

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
            self.display(node.child_right, level+1)
            print(' ' * 4 * level + '->', node.data)
            self.display(node.child_left, level+1)


myTree = AVL_Tree()







# Prueba 1: Insertar tres numeros consecutivos
# myTree.insert(9)
# myTree.insert(8)
# myTree.insert(7)
# myTree.display(myTree.root)

# Prueba 2: Insertar otro dos numeros consecutivos
# myTree.insert(6)
# myTree.insert(5)
# print()
# myTree.display(myTree.root)

# Prueba 3: Insertar 10, 11 y 4
# myTree.insert(10)
# myTree.insert(11)
# myTree.insert(4)
# print()
# myTree.display(myTree.root)

# Prueba 4: Borrando 11 (nodo hoja)
# myTree.delete_node(11)
# print()
# myTree.display(myTree.root)

# Prueba 5: Borrando 10 (nodo con un hijo)
# myTree.delete_node(10)
# print()
# myTree.display(myTree.root)

# Prueba 6: Borrando 8 (nodo con dos hijos)
# myTree.delete_node(8)
# print()
# myTree.display(myTree.root)

# Ultima modificacion 22 Octubre 2021
