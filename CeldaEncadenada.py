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