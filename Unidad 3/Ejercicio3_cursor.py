class Nodo:
    __elemento: None
    __sig: None

    def __init__ (self, ele):
        self.__elemento = ele
        self.__sig

    def obtener_elemento(self):
        return self.__elemento
    
    def obtener_sig (self):
        return self.__sig
    
    def set_elemento (self, valor):
        self.__elemento = valor

    def set_sig (self, valor):
        self.__sig = valor


import numpy as np

class lc:
    __cabeza: int
    __cant: int
    __maximo: int
    __elementos: np.array
    __libre: int

    def __init__(self, maxx):
        self.__maximo = maxx
        self.__cabeza = -1
        self.__cant = 0
        self.__libre = 0
        self.__elementos = np.empty(self.__maximo, dtype= Nodo)

    def obtener_libre(self):
        return self.__libre
    
    def vacia (self):
        return self.__cant == 0
    
    def llena (self):
        return self.__cant == self.__maximo
    

    ## Por posicion
    def insertar (self, x, p):
        if not self.llena():
            if p >= 1 and p <= self.__cant + 1:



    
        
        