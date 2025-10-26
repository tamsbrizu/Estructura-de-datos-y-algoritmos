##Implementacion de digrafo ponderado y no ponderado

from ColaEncadenada import cola
import numpy as np

class digrafo_secuencial:
    __matriz: np.array
    __tamanio: int

    def __init__ (self, m):
        self.__tamanio = m
        self.__matriz = np.empty((m, m), dtype=int)

    def insertar_noPonderado (self, u, v):
        if self.__matriz[u][v] == 1:
            print("Los vertices ya estan ocupados.")
        else:
            self.__matriz[u][v] = 1
            print("Insercion exitosa.")

    def insertar_ponderado (self, u, v, p):
        if self.__matriz[u][v] != 0:
            print("Los vertices ya estan ocupados.")
        else:
            self.__matriz[u][v] = p
            print("Insercion exitosa.")

    def eliminar_arista (self, u,v):
        if self.__matriz[u][v] != 1:
            print("Los vertices no tienen un arista.")
        else:
            self.__matriz[u][v] = 0

    def adyacentes (self, u):
        v = 0
        lista = []
        for v in range(self.__tamanio):
            if self.__matriz[u][v] != 0:
                lista.append(v)
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
    
    def mostrar (self):
        for i in range(self.__tamanio):
            for j in range(self.__tamanio):
                print(f"Fila: {i} - Columna: {j} --- > {self.__matriz[i][j]}")

