import numpy as np

class colaC:
    __max: int
    __ul: int
    __pri: int
    __cant: int
    __elementos: np.array

    def __init__ (self, maxx):
        self.__max = maxx
        self.__ul = 0
        self.__pri = 0 
        self.__cant = 0
        self.__elementos = np.empty(self.__max, dtype=int)

    def vacia (self):
        return self.__cant == 0
    def llena (self):
        return self.__cant == self.__max
    
    def insertar (self, x):
        if self.vacia():
            self.__pri = self.__ul = (self.__ul + 1) % self.__max
            self.__elementos[self.__ul] = x
        else:
            self.__ul = (self.__ul + 1) % self.__max
            self.__elementos[self.__ul] = x
        self.__cant += 1

    def suprimir (self):
        if not self.vacia():
            eliminado = self.__elementos[self.__pri]
            self.__pri = (self.__pri + 1) % self.__max
            self.__cant -= 1
            return eliminado
