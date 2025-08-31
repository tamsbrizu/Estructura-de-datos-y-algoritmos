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
            for i in range (self.__cant):
                print(self.__items[i])
                i = (i+1)%self.__max ##movimiento circular
        
    def cantidad (self):
        cont = 0
        if not self.vacia():
            i = self.__pr
            for i in range (self.__cant):
                cont += 1
                i = (i+1)%self.__max ##movimiento circular
        return cont


        

'''if __name__ == '__main__':

    C = cola(5)

    C.insertar(10)
    C.insertar(20)
    C.insertar(30)

    C.recorrer()

    print("\nSuprimir elemento")

    C.suprimir()

    C.recorrer()'''






        


