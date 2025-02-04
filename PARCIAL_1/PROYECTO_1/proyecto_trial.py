#  Proyecto Parcial 1 Implementación de Pilas

#  En este proyecto se realizó un código cuyo objetivo es el
#  implementar la estructura de pilas o "stack" para poder saber
#  si en una palabra/oración existe algún (paréntesis), [corchete] o {llave}
#  sin su par que lo abra o cierre.
#  Es decir, si se tiene la palabra [estructura (de) {datos],
#  faltaría la llave despúes de que termina {datos}.
#  Una vez identificado si falta alguno de estos símbolos, se
#  indicará cual es el índice donde falta el símbolo
#  y si no hay ningún error, se regresará "Success".

#  Ximena González

#  Fecha de entrega: 18 de Septiembre 2021

class Stack:
    """Clase con los atributos y métodos de una Pila"""

    def __init__(self, size):
        """Clase constructora de una clase"""
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

    def __str__(self):
        """Desplegar en pantalla la lista de los elementos dentro
           de la pila"""
        return f"Stack: {self.stack}"


def bracket_checker():

    # Ciclo que solicita al usuario ingresar texto
    # de por lo menos un caracter de largo
    while True:
        string = input("Input the text: ")

        if len(string) < 1 or len(string) > 10 ** 5:
            print("The text must have between 1 and 100000 characters")
        else:
            break

    opening_brackets = ["[", "{", "("]
    closing_brackets = ["]", "}", ")"]

    stack = Stack(len(string))

    index = 0  # Contador para mantener los indices de la posicion de cada bracket

    # Recorriendo cada caracter en el texto
    for char in string:
        index += 1

        # Si el caracter es un bracket inicial, insertarlo al stack junto con su indice
        # (que es indicado por la variable index), dentro de una tupla
        if char in opening_brackets:
            stack.insert_item((char, index))

        # Si el caracter es un bracket final, sacar ultimo elemento (cima),
        # que es un bracket inicial, y comparar si son del mismo tipo
        elif char in closing_brackets:

            if not stack.is_empty():  # Primero revisar que el stack no este vacia
                peak = stack.delete_item()  # Sacar la tupla en la cima de la pila
                open_bracket = peak[0]  # Sacar el bracket de la tupla en la cima del stack y guardar en la variable

                # Obtener indice de la posicion del elemento en
                # la cima en la lista de brackets iniciales
                index_open_bracket = opening_brackets.index(open_bracket)

                # Obtener indice de la posicion del bracket final
                # en la lista de brackets finales
                index_closed_bracket = closing_brackets.index(char)

                # Si los indices de posicion de los brackets son diferentes, significan que
                # no son del mismo tipo, por ende hay un error en el texto
                if index_closed_bracket != index_open_bracket:
                    # Print opcional que da detalles del error
                    #print(f"Mistake at index : {index} \nClosed bracket {char} doesn't match open bracket {open_bracket}\n")

                    print(index)
                    return

            # Si el stack esta vacia, significa que en el texto solo hay un bracket final
            # sin bracket inicial que lo acompañe, por ende hay un error en el texto
            else:
                # Print opcional que da detalles del error
                #print(f"Mistake at index : {index}\nBracket {char} has no open bracket to match it.\n")

                print(index)
                return

    # Si el stack no esta vacia, signfica que quedaron brackets iniciales sin brackets finales
    # que los acompañen, por ende hay un error en el texto
    if not stack.is_empty():
        #print("Mistake: following opening brackets have no matching closing bracket.")
        for x in stack.stack:
            # Print opcional que da detalles del error
            #print(f"Bracket: {x[0]} Index: {x[1]}")

            print(f"Index: {x[1]}")
        print()
        return

    # Si el stack esta vacia, y no hubo error en las anteriores condiciones, el texto no tiene error
    else:
        print("Success!\n")
        return


tests = [
    "foo(bar[i);",  # False
    "[El diagrama de flujo y documentación valen 3 puntos y el programa 7 ptos.]",  # True
    "(Incluir: Infografía, diagrama de flujo y archivo.py)",  # True
    "[]",  # True
    "[(a + b) + {(c + d) * (e / f)}]",  # True
    "[(a + b) + {(c + d) * (e / f)]}",  # False
    "abc}",  # False
    "{abc(}",  # False
    "{}([]",  # False
    "{}((aa[]",  # False
    "f(a,b)-g[c]",  # True
    "{}([]["  # False
]


bracket_checker()

