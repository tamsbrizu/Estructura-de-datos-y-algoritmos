class Nodo:
    __elemento: None
    __sig: None

    def __init__ (self, e):
        self.__elemento = e
        self.__sig = None

    def obtener_elemento(self):
        return self.__elemento
    def obtener_sig(self):
        return self.__sig
    
    def set_sig(self, valor):
        self.__sig = valor