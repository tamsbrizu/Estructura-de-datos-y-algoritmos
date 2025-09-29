from claseNodo import Nodo

class pilaE:
    __tope: Nodo
    __cant: int

    def __init__ (self):
        self.__tope = None
        self.__cant = 0

    def vacia (self):
        return self.__cant == 0
    
    def insertar (self, x):
        nuevo = Nodo(x)
        nuevo.set_sig(self.__tope)
        self.__tope = nuevo
        self.__cant += 1

    def suprimir (self):
        if not self.vacia():
            eliminado = self.__tope.obtener_elemento()
            self.__tope = self.__tope.obtener_sig()
            self.__cant -= 1
            return eliminado
