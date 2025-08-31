from CeldaEncadenada import Celda

class cola:
    __cant: int
    __pr: None
    __ul: None

    def __init__ (self, xcant = 0):
        self.__pr = None
        self.__ul = None
        self.__cant = xcant

    def vacia (self):
        return self.__cant == 0
    
    def insertar (self, x):
        ps1 = Celda()
        ps1.cargar_item(x)
        ps1.cargar_sig(None)
        if (self.__ul == None):
            self.__pr = ps1
        else:
            self.__ul.cargar_sig(ps1)
        self.__ul = ps1
        self.__cant += 1
        return (self.__ul.obtener_item())
    
    def suprimir (self):
        if self.vacia():
            print("La cola esta vacia.")
            return 0
        else:
            aux = self.__pr
            x = aux.obtener_item() 
            self.__pr = aux.obtener_sig()   
            self.__cant -= 1
            if self.__pr is None:
                self.__ul = None
            return x
        
    def recorrer (self):
        aux = self.__pr
        while aux is not None:
            print(aux.obtener_item())
            aux = aux.obtener_sig()


if __name__ == '__main__':
    C = cola()

    C.insertar(10)
    C.insertar(20)
    C.insertar(30)

    C.recorrer()

    print("\nSuprimir elemento")
    C.suprimir()
    C.recorrer()