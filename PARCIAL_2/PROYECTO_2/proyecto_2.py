#  Proyecto Parcial 2 Implementación de Arbol Binario de Búqueda

#  En este proyecto se realizó un código cuyo objetivo es el
#  implementar la estructura de árbol binario para poder saber
#  si el árbol ingresado por el usuario cumple con las propiedades
#  que hacen de un árbol binario un árbol binario de búsqueda.
#  Es decir, si los elementos en el subárbol izquierdo son menores
#  o igual que un nodo padre y los del subárbol derecho son mayores.
#  Para llevarlo acabo se decidió aprovechar la característica del
#  recorrido in-order de un árbol binario de búsqueda: todos los
#  elementos se despliegan de manera ascendente (menor a mayor).

#  Ximena González

#  Fecha de entrega: 30 de Octubre 2021

class Node:
    """Clase para representar un nodo con
       sus respectivos atributos"""
    def __init__(self, data):
        self.data = data  # datos del nodo
        self.child_right = None  # hijo derecho del nodo
        self.child_left = None  # hijo izquierdo del nodo


# Funcion para agregar en un arreglo
# los nodos de un arbol binario,
# recorriendolo de forma en-orden:
# izq - raiz - der
def in_order_helper(root: Node, arr):
    if root:
        in_order_helper(root.child_left, arr)  # recorre el lado izquierdo del árbol
        arr.append(int(root.data))  # agrega el dato del nodo
        in_order_helper(root.child_right, arr)  # recorre el lado derecho del árbol


def check_if_bst():
    vertices = int(input())  # número de nodos en el árbol

    if vertices < 0 or vertices > 10**5:
        print("Cantidad de nodos no aceptada")
        return

    # un árbol vacío es considerado un bst correcto
    if vertices == 0:
        print("CORRECT")
        return

    complete_info = []  # arreglo para guardar el input por cada línea

    # tomar el input del usuario y guardarlo dentro del arreglo, quitando
    # los espacios en blancos para obtener solo los números
    for i in range(vertices):
        info = input()
        complete_info.append([x.strip() for x in info.split(' ')])

    node_data = []  # guarda el valor de los nodos
    node_children_data = []  # guarda el valor de las posiciones de los hijos del nodo

    # por cada arreglo en complete_info
    # separar el dato del nodo (como instancia de Node)
    # y los índices de sus hijos
    # y ponerlos en el arreglo corrrespondiente
    for element in complete_info:
        if int(element[0]) < -1*(2**31) or int(element[0]) > (2**31)-1:
            print("Dato para nodo no aceptado")
            return
        node_data.append(Node(int(element[0])))

        if (int(element[1]) < -1 or int(element[1]) > vertices-1) or (int(element[2]) < -1 or int(element[2]) > vertices-1):
            print("Dato para nodo no aceptado")
            return
        node_children_data.append((int(element[1]), int(element[2])))  # arreglo que contiene tuplas

    # armando árbol binario a como el usuario lo indicó
    # esto se hace utilizando los indices de las posiciones de los hijos de cada nodo
    # una visualización de la lógica:

    # INPUT:
    # 4
    # 4 1 -1
    # 2 2 3
    # 1 -1 -1
    # 5 -1 -1

    # node_data = [4 2 1 5]
    # node_children_data = [(1,-1), (2,3), (-1,-1), (-1,-1)]

    # node = 4
    # node_children_data = (1,-1)
    # 4.child_left = node_data[1]

    # node = 2
    # node_children_data = (2, 3)
    # 2.child_left = node_data[2]
    # 2.child_right = node_data[3]

    # node = 1
    # node_children_data = (-1, -1)
    # skip

    # node = 5
    # node_children_data = (-1, -1)
    # skip

    cont = 0  # mantiene el indice de los elementos dentro de node_children_data
    for node in node_data:
        index_data = node_children_data[cont]

        # si las posiciones de los hijos de un nodo son ambas
        # diferente a -1, asignar hijo izquierdo e hijo derecho
        # usando los índices que corresponden (estos índices
        # corresponden a posiciones en node_data)
        if index_data[0] != -1 and index_data[1] != -1:
            node.child_left = node_data[index_data[0]]
            node.child_right = node_data[index_data[1]]

        # si las posiciones del hijo izquierdo de un nodo es -1 y
        # del hijo derecho es diferente a -1, asignar hijo derecho
        # usando el índice que corresponde (este índice
        # corresponde a una posición en node_data)
        if index_data[0] == -1 and index_data[1] != -1:
            node.child_right = node_data[index_data[1]]

        # si las posiciones del hijo derecho de un nodo es -1 y
        # del hijo izquierdo es diferente a -1, asignar hijo izquierdo
        # usando el índice que corresponde (este índice
        # corresponde a una posición en node_data)
        if index_data[0] != -1 and index_data[1] == -1:
            node.child_left = node_data[index_data[0]]

        cont += 1  # incrementar para poder seguir avanzando en el arreglo node_children_data

    # Una vez que se tiene armado el árbol binario acorde
    # a como lo estableció el nodo, se hace un recorrido en-orden
    # del árbol para verficar que los nodos se impriman de forma ascendente.
    # Si no resulta de esta forma, significa que el árbol de usuario
    # no cumple con lo característico de un bst.

    nodes_in_tree = []  # arreglo para guardar los nodos que se visiten durante el recorrido
    in_order_helper(node_data[0], nodes_in_tree)  # llamada a la funcion para recorrel el árbol en manera en-orden
    status = True  # bandera que indica si los elementos del arreglo (los nodos del árbol) estan de forma ascendiente

    # for para recorrer la lista que guarda los nodos
    for j in range(len(nodes_in_tree)-1):
        # si el número siguiente es menor que el
        # número actual, la lista no está en orden ascendiente
        if nodes_in_tree[j+1] < nodes_in_tree[j]:
            status = False  # marcar la bandera como Falso
            break  # salir del ciclo

    # si la bandera se quedó como True, es porque la lista de nodos
    # está de forma ascendiente, por lo que no hay error
    if status:
        print("CORRECT")
    # si la bandera se cambió a False, es porque la lista de nodos
    # no está de forma ascendiente, por lo que hay error
    else:
        print("INCORRECT")


check_if_bst()
