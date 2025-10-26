import numpy as np

class Pila:
    __items: np.array
    __cant: int
    __tope: int

    def __init__ (self, cantx, tope = -1):
        self.__cant = cantx
        self.__tope = tope
        self.__items = np.zeros(self.__cant, dtype=int)

    def vacia (self):
        return self.__tope == -1

    def insertar (self, x):
        if self.__tope < (self.__cant -1):
            self.__tope += 1
            self.__items[self.__tope] = x
            return x
        else:
            return 0
        
    def suprimir (self):
        if self.vacia():
            print ("Pila Vacia")
            return 0
        else:
            x = self.__items[self.__tope]
            self.__tope -= 1
            return x
    
    def mostrar (self):
        for i in range (self.__tope, -1, -1):
            print(self.__items[i])

    def obtener_items(self):
        return self.__items
