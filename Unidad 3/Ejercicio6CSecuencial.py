import numpy as np

class cola:
    __items: np.array
    __max: int
    __pr: int
    __ul: int
    __cant: int


    def __init__ (self, xmax = 0):
        self.__max = xmax
        self.__pr = 0
        self.__ul = 0
        self.__cant = 0
        self.__items = np.zeros(xmax, dtype=object)

    def vacia (self):
        return (self.__cant == 0)

    def insertar (self, x):
        if self.__cant < self.__max:
            self.__items[self.__ul] = x
            self.__ul = (self.__ul +1)%self.__max ##Movimiento circular del ul
            self.__cant += 1
            return x
        else:
            return 0
        
    def suprimir (self):
        if self.vacia():
            print("El arreglo esta vacio")
            return 0
        else:
            x = self.__items[self.__pr]
            self.__pr = (self.__pr + 1) % self.__max
            self.__cant -= 1
            return x
        

    def recorrer (self):
        if not self.vacia():
            i = self.__pr
            for j in range (self.__cant):
                print((self.__items[i], ""))
                i = (i+1)%self.__max ##movimiento circular

    def escaleras (self, n):
        self.insertar((n, ""))

        while not self.vacia():
            n, sol = self.suprimir()

            if n == 0:
                print("Se llego al camino", sol)
            if n >= 1:
                self.insertar((n-1, sol + "1"))
            if n >= 2:
                self.insertar((n-2, sol + "2"))


if __name__ == '__main__':

    C = cola(110000)

    print("3 peldaños")
    C.escaleras(3)

    print("2 peldaños")
    C.escaleras(2)
