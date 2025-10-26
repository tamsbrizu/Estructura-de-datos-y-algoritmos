from ColaEncadenada import cola

import numpy as np

class Nodo:
    __elemento: None
    __sig: None

    def __init__ (self, e):
        self.__elemento = e
        self.__sig = None

    def obtener_elemento (self):
        return self.__elemento
    
    def obtener_sig (self):
        return self.__sig
    
    def set_sig (self, valor):
        self.__sig = valor

class grafo_encadenado:
    __arreglo: np.array
    __tamanio: int

    def __init__ (self, m):
        self.__tamanio = m
        self.__arreglo = np.empty (self.__tamanio, dtype=object)

    def insertar_lAdyacencia (self, u, v):
        if self.__arreglo[u] is not None and self.__arreglo[v] is not None:
            print("Los vertices colocados ya estan ocupados.")
        else:
            nuevo1 = Nodo(u)
            nuevo2 = Nodo(v)

            nuevo1.set_sig(self.__arreglo[u])
            self.__arreglo[u] = nuevo1

            nuevo2.set_sig(self.__arreglo[v])
            self.__arreglo[v] = nuevo2

    ## Lista con los pesos
    def insertar_lPesos (self, u, v, p):
        if self.__arreglo[u] is not None and self.__arreglo[v] is not None:
            print("Los vertices colocados ya estan ocupados.")
        else:
            nuevo = Nodo(p)

            nuevo.set_sig(self.__arreglo[u])
            self.__arreglo[u] = nuevo

            nuevo.set_sig(self.__arreglo[v])
            self.__arreglo[v] = nuevo

    def eliminar_arista (self, u, v):
        if self.__arreglo[u] is None and self.__arreglo[v] is None:
            print("Los vertices colocados no tiene una arista a eliminar.")
        else:
            self.__arreglo[u] = None
            self.__arreglo[v] = None

    def adyacente (self, u):
        lista = []
        aux = self.__arreglo[u]
        while aux is not None:
            lista.append(aux.obtener_elemento())
            aux = aux.obtener_sig()

        return lista
    
    def BEA (self, s):
        vertices = np.empty(self.__tamanio, dtype=int)
        colaE = cola()
        for i in range(self.__tamanio):
            vertices[i] = 0

        vertices[s] = 0
        colaE.insertar(vertices[s])
        while not colaE.vacia():
            x = colaE.suprimir()
            lista = self.adyacentes(x)
            for v in lista:
                if vertices[v] == 0:
                    vertices[v] = vertices[x] + 1
                    cola.insertar(v)

    def BEP (self):
        tiempo = 0
        comienzo = np.zeros(self.__tamanio, dtype=int)
        fin = np.zeros (self.__tamanio, dtype=int)
        
        for v in comienzo:
            if comienzo[v] == 0:
                self.BEP_visita(v, tiempo, comienzo, fin)

    def BEF_visita (self, v, tiempo, comienzo, fin):
        tiempo += 1
        comienzo[v] = tiempo
        lista = self.adyacentes(v)
        for u in lista:
            if comienzo[u] == 0:
                tiempo = self.BEF_visita(u, tiempo, comienzo, fin)
        tiempo += 1
        fin[v] = tiempo
        return tiempo
    
    def camino_lAdyacente (self, u):
        pass



    