import numpy as np

class pilaS:
    __cant: int
    __tope: int
    __max: int
    __elementos: np.array

    def __init__ (self, maxx):
        self.__max = maxx
        self.__cant = 0
        self.__tope = -1
        self.__elementos = np.zeros(self.__max, dtype=int)

    def vacia (self):
        return self.__tope == -1
    def llena (self):
        return self.__cant == self.__max
    

    def insertar (self, x):
        if not self.llena():
            self.__tope += 1
            self.__elementos[self.__tope] = x
            self.__cant += 1
            
    
    def suprimir (self):
        if not self.vacia():
            eliminado = self.__elementos[self.__tope]
            self.__tope -= 1
            self.__cant -= 1
            return eliminado
        
    def invertir (self):
        fin = self.__tope
        inicio = 0
        while inicio < fin:
            self.__elementos[inicio], self.__elementos[fin] = self.__elementos[fin], self.__elementos[inicio]
            inicio += 1
            fin -= 1
        
    def mostrar (self):
        for i in range(self.__tope, -1, -1):
            print(self.__elementos[i])