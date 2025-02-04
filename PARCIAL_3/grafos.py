# Grafos: Representación de un grafo mediante listas de adyacencias

# Se implementan las clases de Vertice y Grafo para poder visualizar
# tanto un grafo dirigido como uno no dirigido. Asimismo se hace uso
# de la libreria networkx para visualizar el grafo.

# Link a Google Colab con los ejemplos de este programa junto con sus
# respectivas visualizaciones:
# https://colab.research.google.com/drive/1tS2hgZ4Cm2360g1C3AVJO5YsojceMnXH?usp=sharing

# Equipo:
# Gabriela Sanchez
# Ximena Gonzalez

import networkx as nx
import matplotlib.pyplot as plt

# clase para representar un nodo/vertice de un grafo
class Vertice:
    def __init__(self, n):
        self.nombre = n  # nombre de los nodos a los que se conecta un nodo

        # C <- A -> B
        #      ↓         vecinos de A = [B, C, D]
        #      D
        self.vecinos = list()

        self.distancia = 0
        self.color = "blanco"
        self.pred = -1

        self.tiempo_descubrimiento = 0
        self.tiempo_termino = 0

    # agregar un nodo/vertice a la lista de vecinos del nodo
    def agregar_vecino(self, v):
        if v not in self.vecinos:  # si v no existe en vecinos del nodo, ai agregarlo
            self.vecinos.append(v)  # agregar a lista
            self.vecinos.sort()  # ordenar lista


# clase para representar un grafo con sus nodos/vertices
class Grafo:
    def __init__(self):
        # diccionario que guarda el valor de vertice
        # {A : memoria, B : memoria, C : memoria, D : memoria }
        # memoria indica donde esta guardado el nodo
        self.vertices = {}
        self.tiempo = 0

    # agregar un vertice o nodo al grafo
    def agregar_vertice(self, vertice):
        # si el vertice si es una instancia de la clase Vertice y su
        # nombre no se encuentra ya en la lista de vertices, si agregarlo al diccionario
        # (la llave es su nombre y su valor es la instancia/espacio en memoria)
        if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
            self.vertices[vertice.nombre] = vertice
            return True
        else:
            return False

    # agregar un arista al un vertice o nodo
    # u y v son nodos/vertices
    # este metodo es para grafos NO DIRIGIDOS porque agrega aristas
    # en ambos sentidos (u, v) y (v, u) o u ↔ v
    def agregar_arista_no_dirigido(self, u, v):
        # si ambos nodos/vertices existen en el diccionario de vertices
        # del grafo, si es una conexión valida

        # al recorrer el diccionario, si la llave es igual al nodo/vertice u,
        # al valor (que es el espacio de memoria de u) llamarle el metodo
        # de agregar_vecino para agregar a v como vecino de u.

        # lo anterior aplica para el nodo/vertice v
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.agregar_vecino(v)
                    self.matriz[u][v] = 1
                if key == v:
                    value.agregar_vecino(u)
                    self.matriz[v][u] = 1
            return True
        else:
            return False

    # agregar un arista al un vertice o nodo
    # u y v son nodos/vertices
    # este metodo es para grafos DIRIGIDOS porque agrega arista
    # en un sentido (u, v) o u -> v
    def agregar_arista_dirigido(self, u, v):
        # si ambos nodos/vertices existen en el diccionario de vertices
        # del grafo, si es una conexión valida

        # al recorrer el diccionario, si la llave es igual al nodo/vertice u,
        # al valor (que es el espacio de memoria de u) llamarle el metodo
        # de agregar_vecino para agregar a v como vecino de u.

        # lo anterior NO aplica para el nodo/vertice v, ya que
        # la conexion va en una sola direccion
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.agregar_vecino(v)
            return True
        else:
            return False

    # imprimir cada vertice y la lista de sus vecinos
    def imprimir_grafo(self):
        for key in sorted(list(self.vertices.keys())):
            print(f"Vertice {key}\nSus vecinos son {self.vertices[key].vecinos}\n")

    def bfs(self, grafo, vertice_inicio):
        # Funcion para desplegar distancia a cada uno de los vertices a partir del vertice_inicio
        print(f"BFS DESDE {vertice_inicio.nombre}\n")

        # Poner los valores en default para todos los nodos
        # en el grafo
        for k, v in grafo.vertices.items():
            v.color = "blanco"  # blanco indica que no ha sido visitado
            v.distancia = 0  # Distancia desde el nodo de origen
            v.pred = None  # Predecesor del nodo

        vertice_inicio.color = "gris"  # Marcar el color de nodo de partida como gris
        vertice_inicio.distancia = 0  # Marcar la distancia de nodo de partida como 0
        vertice_inicio.pred = None  # El nodo de partida no tiene predecesor

        keys = list(grafo.vertices.keys())  # Lista de las llaves en el diccionario del grafo (nombre nodos)
        values = list(grafo.vertices.values())  # Lista de valores en el diccionario del grafo (objeto nodos)

        Q = [vertice_inicio]  # Pila para ir encolando los nodos visitados, comenzando con el nodo de partida

        # Mientras la pila no este vacía
        while len(Q) != 0:
            u = Q.pop(0)  # Sacar primer nodo de la pila

            # Por cada vecino que tenga el nodo
            # cambair los atributos del vecino para
            # indicar que ya fue visitado, indicar
            # las cantidad de nodos que se recorrió
            # para llegar e indicar su predecesor
            for vecino in u.vecinos:
                index = keys.index(vecino)
                v = values[index]

                if v.color == "blanco":
                    v.color = "gris"
                    v.distancia = u.distancia + 1
                    u.pred = u
                    Q.append(v)  # Agregar veciono a la pila para visitar sus vecinos
                    print(f"Vertice : {v.nombre}")
                    print(f"Distancia : {v.distancia}\n")

            u.color = "negro"  # Inidcar que el nodo ya fue visitado

    def dfsVisitar(self, vert):
        # Funcion para saber por que vertices ha pasado
        global tiempo
        tiempo = tiempo + 1
        vert.tiempo_descubrimiento = tiempo
        vert.color = "gris"

        # Por cada vertice, si esta en blanco significa que no ha pasado por ahi,
        # una vez que pasa se pone como negro
        # Se suma el tiempo del recorrido por cada vertice que visita
        for v in vert.vecinos:
            if self.vertices[v].color == "blanco":
                self.vertices[v].pred = vert
                self.dfsVisitar(self.vertices[v])

        vert.color = "negro"
        tiempo = tiempo+1
        vert.tiempo_termino = tiempo

    def dfs(self):
        global tiempo
        tiempo = 0

        # Si en el recorrido el vertice esta en blanco sig. que no ha pasado por ahi
        for u in sorted(list(self.vertices.keys())):
            if self.vertices[u].color == "blanco":
                self.dfsVisitar(self.vertices[u])

    def imprimeGrafoDFS(self):
        # Funcion que imprime el paso que hizo para descubrir el primero vertice, y cuanto recorre del sig. al original
        # del Grafo DFS
        for key in sorted(list(self.vertices.keys())):
            print(f"\nVertice: {key}")
            print(f"Descubrimiento/Termino: {str(self.vertices[key].tiempo_descubrimiento)} / {str(self.vertices[key].tiempo_termino)}")

    # dibujar un grafo no dirigido
    def visualizar_grafo_no_dirigido(self):
        G = nx.Graph()  # Crear instancia de grafo no dirigido
        G.add_nodes_from(self.vertices.keys())  # Agregar vertices a grafo
        edges = []  # Lista que guarda todas las aristas del grafo

        # Colocar la llave y sus respectivo vecino(s) juntos,
        # para formar una tupla con el arista, y esta tupla
        # se agregue a la lista de edges que es la lista de
        # todos los aristas del grafo
        for key, value in self.vertices.items():
            for vecino in value.vecinos:
                edges.append((key, vecino))

        G.add_edges_from(edges)

        # Visualizar el grafo
        nx.draw_circular(G, with_labels=True, font_weight="bold")
        plt.show()

        A = nx.adjacency_matrix(G)
        matriz = A.todense()
        print(f"{A.todense()}\n")

    # dibujar un grafo dirigido
    def visualizar_grafo_dirigido(self):
        DG = nx.DiGraph()  # Crear instancia de grafo dirigido
        DG.add_nodes_from(self.vertices.keys())

        edges = []  # Lista que guarda todas las aristas del grafo

        # Colocar la llave y sus respectivo vecino(s) juntos,
        # para formar una tupla con el arista, y esta tupla
        # se agregue a la lista de edges que es la lista de
        # todos los aristas del grafo
        for key, value in self.vertices.items():
            for vecino in value.vecinos:
                edges.append((key, vecino))
        DG.add_edges_from(edges)

        # Visualizar el grafo
        nx.draw_circular(DG, with_labels=True, font_weight="bold")
        plt.show()

        A = nx.adjacency_matrix(DG)
        matriz = A.todense()
        print(f"{A.todense()}\n")


if __name__ == "__main__":

    # EJEMPLO GRAFO NO DIRIGIDO
    # grafo = Grafo()
    # a = Vertice("A")
    # grafo.agregar_vertice(a)
    #
    # for i in range(ord("A"), ord("K")):
    #     grafo.agregar_vertice(Vertice(chr(i)))
    #
    # edges = ["AB", "AE", "BF", "CG", "DH", "EH", "FG", "FI", "FJ", "GJ"]
    #
    # for edge in edges:
    #     grafo.agregar_arista_no_dirigido(edge[:1], edge[1:])
    #
    # grafo.imprimir_grafo()

    # EJEMPLO GRAFO NO DIRIGIDO
    # 1 --- 2
    # |   / |  \
    # |  /  |   3
    # | /   |  /
    # 5 --- 4

    grafo_nd = Grafo()
    a = Vertice("1")
    grafo_nd.agregar_vertice(a)

    for i in range(ord('1'), ord('6')):
        grafo_nd.agregar_vertice(Vertice(chr(i)))

    edges = ["12", "21", "15", "51", "25", "52", "24", "42", "23", "32", "34", "43", "54", "45"]

    for edge in edges:
        grafo_nd.agregar_arista_dirigido(edge[:1], edge[1:])

    # grafo_nd.imprimir_grafo()
    grafo_nd.visualizar_grafo_no_dirigido()

    # RECORRIDOS

    # BFS
    # grafo_nd.bfs(grafo_nd, a)

    # DFS
    # grafo_nd.dfs()
    # grafo_nd.imprimeGrafoDFS()

    # EJEMPLO GRAFO DIRIGIDO
    # 1 -->  2     3
    # |    ↗ |   / |
    # |  /   |  /  |
    # ↓ /    ↓ ↙   ↓
    # 4 <--- 5     6 <-
    #              |__|

    grafo_d = Grafo()
    a = Vertice("1")
    grafo_d.agregar_vertice(a)

    for i in range(ord('1'), ord('7')):
        grafo_d.agregar_vertice(Vertice(chr(i)))

    edges = ["12", "14", "25", "42", "54", "35", "36", "66"]

    for edge in edges:
        grafo_d.agregar_arista_dirigido(edge[:1], edge[1:])

    # grafo_d.imprimir_grafo()
    grafo_d.visualizar_grafo_dirigido()

    # RECORRIDOS

    # BFS
    # grafo_d.bfs(grafo_d, a)

    # DFS
    # grafo_d.dfs()
    # grafo_d.imprimeGrafoDFS()


# Ultima Modificacion 23 Noviembre 2021





