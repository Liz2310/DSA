#  Implementacion de pila estatica (con arreglos)

class Stack:
    def __init__(self, size):
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
        """Sacar del stack el elemento en la cima (en un
           arreglo el elemento en la cima es el ultimo;
           pop() por default saca el ultimo elemento de un
           arreglo)"""
        if not self.is_empty():
            x = self.stack.pop()
            self.top -= 1
            return x
        return False

    def print_stack(self):
        print(self.stack)

    def __str__(self):
        return f"Stack: {self.stack}"


if "__name__" == "main":
    stack1 = Stack(8)
    stack1.insert_item(2)
    print(stack1)
    print(stack1.is_empty())
    print(stack1.is_full())
    for i in range(7):
        stack1.insert_item(i)
    stack1.print_stack()
    print(stack1.is_full())




