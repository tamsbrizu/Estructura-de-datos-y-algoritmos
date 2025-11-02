class NodoP:
    __elemento: None
    __peso: None
    __sig: None

    def __init__ (self, e, p):
        self.__elemento = e
        self.__peso = p
        self.__sig = None

    def obtener_elemento(self):
        return self.__elemento
    def obtener_peso (self):
        return self.__peso
    def obtener_sig(self):
        return self.__sig
    
    def set_sig(self, valor):
        self.__sig = valor