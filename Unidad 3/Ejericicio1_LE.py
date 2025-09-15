##Se ultiza un ultimo (si es opcional). En buscar primero se debe buscar la posicion y es valida se inserta
##insertar, suprimir, recuperar, buscar, primero, ultimo, siguiente, anterior, recorrer, vacia

class Nodo:
    __elemento: None
    __sig: None

    def __init__ (self, elem):
        self.__elemento = elem
        self.__sig = None

    def obtener_elemento (self):
        return self.__elemento
    
    def obtener_sig (self):
        return self.__sig
    
    def set_elemento (self, valor):
        self.__elemento = valor

    def set_sig (self, valor):
        self.__sig = valor


class le:
    __cant: int
    __cabeza: int

    def __init__ (self):
        self.__cabeza = None
        self.__cant = 0

    def vacia (self):
        return self.__cant == 0
    
    def primero_elemento (self):
        return self.__cabeza.obtener_elemento()
    
    def ultimo_elemento (self):
        aux = self.__cabeza
        while aux.obtener_sig() is not None:
            aux = aux.obtener_sig()
        return aux.obtener_elemento()
    
    '''def siguiente_posicion (self, p):
        if p >= 1 and p <= self.__cant:
            i = 0
            aux = self.__cabeza
            while i < p-1:
                aux = aux.obtener_sig()
                i += 1
            if aux.obtener_sig() is not None:
                return aux.obtener_sig().obtener_elemento()
        else:
            print("Posicion invalida para obtener siguiente")
    
    def anterior_posicion (self, p):
        if p >= 1 and p <= self.__cant:
            i = 0
            aux = self.__cabeza
            while aux is not None and i < p-2:
                aux = aux.obtener_sig()
                i+= 1
            return aux.obtener_elemento()
        else:
            print("Posicion invalida para obtener anterior")'''
    
    def siguiente_posicion (self, p):
        if p >= 1 and p <= self.__cant:
            if p + 1 <= self.__cant:
                p = p +1
            return p
        else:
            print("Posicion invalida para obtener siguiente")

    
    def anterior_posicion (self, p):
        if p >= 1 and p <= self.__cant:
            if p - 1 >= 0:
                p = p -1
            return p
        else:
            print("Posicion invalida para obtener anterior")


    def insertar (self, x, p):
        if p>=1 and p <= self.__cant + 1:
            if p == 1:
                nuevo = Nodo(x)
                nuevo.set_sig(self.__cabeza)
                self.__cabeza = nuevo
                self.__cant += 1

            else:
                nuevo = Nodo(x)
                aux = self.__cabeza
                i = 1
                while i < p -1 and aux is not None:
                    aux = aux.obtener_sig()
                    i += 1
                
                nuevo.set_sig(aux.obtener_sig())
                aux.set_sig(nuevo)

                self.__cant += 1

        else:
            print("Posicion invalida para insertar.")

    def suprimir (self, p):
        if p >= 1 and p <= self.__cant:
            aux = self.__cabeza
            i = 0
            if p == 1:
                x = self.__cabeza.obtener_elemento()
                self.__cabeza = self.__cabeza.obtener_sig()
            else:
                aux = self.__cabeza
                i = 1

                while i < p - 2 and aux is not None:
                    aux = aux.obtener_sig()
                    i += 1
                
                x = aux.obtener_sig().obtener_elemento()
                if x is not None:
                    aux.set_sig(aux.obtener_sig().obtener_sig())

            self.__cant -= 1
            return x
        else:
            print("Posicion invalida para suprimir.")

    def buscar (self, x):
        ban = False
        aux = self.__cabeza
        i = 0
        while not ban and aux is not None:
            if aux.obtener_elemento () == x:
                ban =True
            else:
                aux = aux.obtener_sig()
                i+= 1
        
        if ban:
            return i
        else:
            return -1
        
    def recuperar (self, p):
        if p >= 1 and p <= self.__cant:
            aux = self.__cabeza
            i = 1
            while i < p  and aux is not None:
                aux = aux.obtener_sig()
                i += 1

            x = aux.obtener_elemento()
            return x
        else:
            print("Posicion invalida para recuperar")

    def recorrer (self):
        aux = self.__cabeza
        while aux is not None:
            print(aux.obtener_elemento())
            aux = aux.obtener_sig()


if __name__ == "__main__":
    # Crear lista
    mi_lista = le()

    # Insertar elementos
    print("Insertando elementos...")
    mi_lista.insertar(10, 1)  # Insertar 10 en posición 1
    mi_lista.insertar(20, 2)  # Insertar 20 en posición 2
    mi_lista.insertar(30, 3)  # Insertar 30 en posición 3
    mi_lista.insertar(15, 2)  # Insertar 15 en posición 2

    # Recorrer lista
    print("\nRecorriendo lista:")
    mi_lista.recorrer()  # Debería mostrar: 10, 15, 20, 30

    # Recuperar elemento en posición 3
    print("\nElemento en posición 3:", mi_lista.recuperar(3))  # Debería mostrar 20

    # Buscar elemento
    pos = mi_lista.buscar(15)
    if pos != -1:
        print(f"\nElemento 15 encontrado en la posición {pos + 1}")
    else:
        print("\nElemento 15 no encontrado")

    # Obtener primero y último elemento
    print("\nPrimer elemento:", mi_lista.primero_elemento())
    print("Último elemento:", mi_lista.ultimo_elemento())

    # Suprimir elemento en posición 2
    print("\nSuprimiendo elemento en posición 2...")
    mi_lista.suprimir(2)

    # Recorrer lista nuevamente
    print("\nRecorriendo lista después de suprimir:")
    mi_lista.recorrer()  # Debería mostrar: 10, 20, 30

    # Obtener siguiente y anterior posición
    print("\nSiguiente elemento de la posición 2:", mi_lista.siguiente_posicion(2))  # Debería mostrar 30
    print("Elemento anterior a la posición 2:", mi_lista.anterior_posicion(2))       # Debería mostrar 10
