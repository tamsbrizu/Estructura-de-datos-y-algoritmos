##Pila Secuencial
import numpy as np

class pila:
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


    def inverso (self):
        inicio = 0
        fin = self.__tope
        while inicio < fin:
            aux = self.__items[inicio]
            self.__items[inicio] = self.__items[fin]
            self.__items[fin] = aux
            inicio += 1
            fin -= 1


if __name__ == '__main__':

    P = pila(5)

    P.insertar(67)
    P.insertar(10)
    P.insertar(100)

    P.mostrar()

    P.inverso()

    print("Mostramos la lista en orden inverso")
    P.mostrar()

    print("Suprimimos elemento")
    P.suprimir()

    P.mostrar()