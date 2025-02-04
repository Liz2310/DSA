class Node:
    def __init__(self, t):  # t = minimos numero de child = (m-1)/2
        self.child = []  # Apuntadores
        self.keys = []  # Valores o claves a guardar
        self.n = 0  # Number of keys?

        for k in range(2 * t + 1):  # Para las llaves, 2*t = Maximo numero de claves
            self.keys.append(None)

        for k in range(2 * t + 2):  # Para los child
            self.child.append(None)

    def leaf(self):
        "Regresa si el nodo es hoja"
        if any(self.child):  # Si alguno elemento de la lista de child no es None, entonces no es hoja
            return False  # Regresa False
        return True  # Si no regresa True

    def full(self):
        "Regresa si el nodo esta lleno"
        if all(self.keys):  # Si todos los elementos del nodo son diferentes a None
            return True  # Regresa True
        return False  # Si no regresa False


# funcion auxiliar para desplegar los niveles del arbol
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

    def bTreeCreate(self):
        if not self.root:
            self.root = Node(self.t)
        return self.root

    def bTreeSplitChild(self, x, i):
        z = Node(self.t)
        y = x.child[i]
        z.n = self.t

        for j in range(0, self.t):
            z.keys[j] = y.keys[j + self.t + 1]
            y.keys[j + self.t + 1] = None

        if not y.leaf():
            for j in range(0, self.t + 1):
                z.child[j] = y.child[j + self.t + 1]
                y.child[j + self.t + 1] = None
        y.n = self.t

        for j in range(x.n + 1, i, -1):
            x.child[j] = x.child[j - 1]
        x.child[i + 1] = z

        for j in range(x.n, i, -1):
            x.keys[j] = x.keys[j - 1]
        x.keys[i] = y.keys[self.t]
        y.keys[self.t] = None
        x.n = x.n + 1

    def bTreeInsertNonFull(self, x, k):
        i = x.n
        if x.leaf():
            while i >= 1 and k < x.keys[i - 1]:
                x.keys[i] = x.keys[i - 1]
                i = i - 1
            x.keys[i] = k
            x.n += 1
        else:
            while i >= 1 and k < x.keys[i - 1]:  # AJUSTE
                i = i - 1

            self.bTreeInsertNonFull(x.child[i], k)
            if x.child[i].n == 2 * self.t + 1:
                self.bTreeSplitChild(x, i)
                if k > x.keys[i]:
                    i = i + 1

    def bTreeInsert(self, nodo, k):
        r = self.root

        if r.n == 2 * self.t and r.leaf():  # Raíz esta llena
            s = Node(self.t)
            self.root = s
            s.child[0] = r
            self.bTreeInsertNonFull(s.child[0], k)
            self.bTreeSplitChild(s, 0)
        else:
            self.bTreeInsertNonFull(r, k)

        if r.n == 2 * self.t + 1:
            s = Node(self.t)
            self.root = s
            s.child[0] = r
            self.bTreeSplitChild(s, 0)

    def bTreeSearch(self, nodo, k):
        x = nodo  # nodo en el cual se busca el valor k
        i = 0  # indice para recorrer las llaves

        if not x:  # si el nodo en el cual se quiere buscar es None, significa que ya no hay más donde buscar
            print("No Encontrado")
            return None

        # aumentar el indice mientras se busca el valor k (o
        # algun valor mayor que k)
        while i < x.n and k > x.keys[i]:
            i += 1

        # print(f"\ni: {i}\nllave del nodo: {x.keys[i]}")

        # si el indice esta dentro de la longitud de keys
        # y k está en el índice i en la lista de keys, el valor
        # a buscar (k) fue encontrado
        if i < x.n and k == x.keys[i]:
            print("Encontrado")
            return x, i

        # si no, seguir buscando
        else:
            if x.child:  # si el nodo cuenta con elementos en su lista child, buscar en los hijos
                self.bTreeSearch(x.child[i], k)
            else:  # si el nodo no cuenta con elementos en su lista child, ya no hay donde buscar
                return None

    # imprimir los niveles del arbol
    def bTreePrint(self):
        print("****************************")
        print_rec(self.root, 0)


if __name__ == "__main__":
    # Primer Arbol
    # BT = ArbolB(2)
    # actual = BT.bTreeCreate()
    # print("Nodo Creado")
    # print(BT.root.keys)
    #
    # BT.bTreeInsert(actual, 111)
    # BT.bTreeInsert(actual, 96)
    # BT.bTreeInsert(actual, 84)
    # BT.bTreeInsert(actual, 16)
    # BT.bTreeInsert(actual, 20)
    # print(BT.root.keys)
    #
    # for i in BT.root.child:
    #     if i:
    #         print(i.keys)

    # Segundo Arbol
    arbol = ArbolB(2)
    actual = arbol.bTreeCreate()
    nodos = [5, 8, 10, 11, 12, 13, 14, 15, 25, 30, 31, 32, 33, 40, 18, 20]

    for node in nodos:
        arbol.bTreeInsert(actual, node)
    nodos = [21, 22, 23, 24, 26, 27, 28]

    for node in nodos:
        arbol.bTreeInsert(actual, node)

    arbol.bTreeInsert(actual, 41)
    arbol.bTreeInsert(actual, 42)
    arbol.bTreeInsert(actual, 43)

    arbol.bTreePrint()

    a_buscar = 20  # variable a cambiar para buscar un valor
    print(f"\nBuscando : {a_buscar}")
    arbol.bTreeSearch(arbol.root, a_buscar)
