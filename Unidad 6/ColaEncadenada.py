class Celda:
    __item: object
    __sig: object

    def __init__(self, item = None, sig = None):
        self.__item = item
        self.__sig = sig

    def obtener_item(self):
        return self.__item
    
    def cargar_item(self,itemm):
        self.__item = itemm

    def cargar_sig(self,tope):
        self.__sig = tope

    def obtener_sig(self):
        return self.__sig

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
        if self.vacia():
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
