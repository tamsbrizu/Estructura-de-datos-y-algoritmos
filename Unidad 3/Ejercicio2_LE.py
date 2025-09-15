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
    __cabeza: Nodo

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
    
    def insertar (self, x):
        nuevo = Nodo(x)

        if self.vacia() or x < self.__cabeza.obtener_elemento():
            # si la lista esta vacia o el elemento es menor al elemento que se encuentra en la cabeza (o primer nodo)
            nuevo.set_sig(self.__cabeza) #El nuevo apunta al nodo que antes era la cabeza
            self.__cabeza = nuevo #El nuevo ahora es la cabeza
            self.__cant += 1
                
        elif not self.vacia():

            aux = self.__cabeza
            
            while aux.obtener_sig() is not None and x > aux.obtener_sig().obtener_elemento():
                # Si el siguiente nodo no es none y el elemento del siguiente elemento es menor a x
                aux = aux.obtener_sig() # Se recorre para apuntar al nodo anterior antes de insertar x

            nuevo.set_sig(aux.obtener_sig())  # El nuevo apunta al nodo en el cual se va a insertar
            aux.set_sig(nuevo)
            self.__cant += 1


    def buscar (self, x):
        i = 0
        ban = False
        aux = self.__cabeza
        while not ban and aux is not None:
            if aux.obtener_elemento() == x:
                ban = True
            else:
                aux = aux.obtener_sig()
                i += 1
        
        if ban:
            return i
        else:
            return -1
    
    def suprimir (self, x):
        if not self.vacia():
           if self.__cabeza.obtener_elemento() == x:
               eliminado = self.__cabeza.obtener_elemento()
               self.__cabeza = self.__cabeza.obtener_sig()
               self.__cant -= 1
               return eliminado
           else:
                aux = self.__cabeza
                while aux.obtener_sig() is not None:
                    if aux.obtener_sig().obtener_elemento() == x:
                        eliminado = aux.obtener_sig().obtener_elemento()
                        aux.set_sig(aux.obtener_sig().obtener_sig())
                        self.__cant -= 1
                        return eliminado
                    aux = aux.obtener_sig()

        else:
           print("La lista esta vacia.")
                       
        

    def siguiente_posicion (self, x):
        aux = self.__cabeza
        while aux.obtener_sig() is not None:
            if aux.obtener_elemento() == x:
                if aux.obtener_sig() is not None:
                    return aux.obtener_sig().obtener_elemento()
            
            aux = aux.obtener_sig()
        
        

    def anterior_posicion (self,x):
        if self.__cabeza.obtener_elemento () == x:
            print("No hay anterior")
        else:
            aux = self.__cabeza
            while aux.obtener_sig() is not None:
                if aux.obtener_sig().obtener_elemento() == x:
                    return aux.obtener_elemento()
                aux = aux.obtener_sig()

    def recuperar (self, p):
        if p >= 1 and p <= self.__cant:
            aux = self.__cabeza
            i = 0
            while i < p-1 and aux is not None:
                aux = aux.obtener_sig()
                i += 1
            return aux.obtener_elemento()
        else:
            print("Posicion invalida")

    def recorrer (self):
        aux = self.__cabeza
        while aux is not None:
            print(aux.obtener_elemento())
            aux = aux.obtener_sig()


if __name__ == '__main__':
    LE = le()

    LE.insertar(20)
    LE.insertar(10)

    LE.recorrer()

    print("\nSuprimiendo elemento")
    LE.suprimir(20)
    LE.recorrer()

    print("\nInsercion del 30")
    LE.insertar(30)
    LE.recorrer()

    print("\nPrimer elemento")
    print(LE.primero_elemento())

    print("\nUltimo Elemento")
    print(LE.ultimo_elemento())

    print("\nSiguiente Elemento del 10")
    print(LE.siguiente_posicion(10))

    print("\nAnterior elemento del 30")
    print(LE.anterior_posicion(30))

    print("\nRecuperar en la posicion 1")
    print(LE.recuperar(2))






        
