from claseNodo import Nodo

class colaE:
    __pri: Nodo
    __ul: Nodo
    __cant: int

    def __init__ (self):
        self.__pri = None
        self.__ul = None
        self.__cant = 0

    def vacia (self):
        return self.__cant == 0
    
    def insertar (self, x):
        nuevo = Nodo(x)
        if self.__ul is None:
            self.__pri = nuevo
            self.__ul = nuevo
        else:
            self.__ul.set_sig(nuevo)
            self.__ul = nuevo
        self.__cant += 1

    def suprimir (self):
        if not self.vacia():
            eliminado = self.__pri.obtener_elemento()
            self.__pri = self.__pri.obtener_sig()
            self.__cant -= 1
        
            if self.__pri is None:
                self.__ul = None

            return eliminado
        
    def obtener_cant (self):
        return self.__cant