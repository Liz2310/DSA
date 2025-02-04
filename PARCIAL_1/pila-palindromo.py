# Practica: Pilas-Palindromos

# Verficar que una entrada ingresada es un palindromo,
# implementando la estructura de Stack (Pila)
# Ejemplos Palindromo :
# 2002
# racecar
# A cavar a Caravaca

# Ximena Gonzalez

class Stack:
    """Clase para construir y operar sobre la estructura
       de stack (pila)"""

    def __init__(self, size):
        """Funcion constructora de stack (pila)"""
        self.size = size
        self.stack = []  # Arreglo de los elementos en la stack
        self.top = -1  # Indice del elemento en la cima

    def is_empty(self):
        """Revisar si el stack esta vacio (no tiene
           elementos)"""
        if self.top == -1:
            return True
        return False

    def is_full(self):
        """Revisar si el stack esta lleno (comparar el indice
           del elemento en la cima y el valor del tamaño)"""
        if self.top + 1 is self.size:
            return True
        return False

    def insert_item(self, item):
        """Agregar un elemento al stack (primero
           revisar que el stack no este lleno)"""
        if not self.is_full():
            self.stack.append(item)
            self.top += 1
            return True
        return False

    def delete_item(self):
        """Sacar del stack el elemento en la cima y
           guardarlo en una variable y regresarla (en un
           arreglo el elemento en la cima es el ultimo;
           pop() por default saca el ultimo elemento de un
           arreglo)"""
        if not self.is_empty():
            x = self.stack.pop()
            self.top -= 1
            return x
        return False

    def __str__(self):
        """Imprimir el stack (pila) completo"""
        return f"Stack: {self.stack}"


def es_palindromo():

    entrada = input("Ingrese la palabra u oracion a revisar: ")  # Recibir palabra u oracion del usuario
    entrada = entrada.replace(" ", "").lower()  # Eliminar espacios en blanco y hacer minusculas
    stack = Stack(len(entrada))  # Instancia de un stack (pila) con longitud igual a la longitud de la entrada

    for caracter in entrada:  # Iterar caracter por caracter en la entrada
        stack.insert_item(caracter)  # Insertar en la instancia del stack (pila)

    entrada_al_reves = ""  # String para meter la entrada al reves y comparar con la entrada original

    while not stack.is_empty():  # Mientras el stack no este vacia, insertar sus elementos al string al reves
        entrada_al_reves += stack.delete_item()  # Usar metodo de stack que elimina y regresa el primer elemento del stack

    #  Comparar entrada original con al reves
    if entrada == entrada_al_reves:
        return f"La palabra {entrada} SI es un palindromo \nPrograma elaborado por Ximena Gonzalez y David Roldan"
    else:
        return f"La palabra {entrada} NO es un palindromo \nPrograma elaborado por Ximena Gonzalez y David Roldan"


print(es_palindromo())

# Ultima Modificacion: 9 de Septiembre 2021
