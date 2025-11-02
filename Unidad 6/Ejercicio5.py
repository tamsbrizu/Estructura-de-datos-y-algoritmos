import copy
import numpy as np

class grafo:
    __tamanio: int
    __matriz: np.array

    def __init__ (self, n):
        self.__tamanio = n
        self.__matriz = np.full((n,n), float("inf"))
        for i in range(self.__tamanio):
            self.__matriz[i][i] = 0
        
    ##Insercion para grafo Ponderado
    def insertarPonderado (self, v1, v2, p):
        u = v1 -1
        v = v2 - 1
        if self.__matriz[u][v] != float("inf"):
            print("Los vertices ya estan conectados.")
        else:
            self.__matriz[u][v] = p
            self.__matriz[v][u] = p

    def camino_minimo (self):
        n = self.__tamanio
        Q = self.__matriz.copy()

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    Q[i][j] =  min(Q[i][j], Q[i][k] + Q[k][j])
        return Q

    def sucursal (self):
        q = self.camino_minimo()
        indiceSucu = 0
        mini = 99999
        for i in range(len(q)):
            suma = 0
            for j in range(len(q)):
                suma += q[i][j]

            if suma < mini:
                mini = suma
                indiceSucu = i
        return indiceSucu, mini
    
    def sucursal2 (self, indi):
        q = self.camino_minimo()
        indiceSucu = 0
        mini = 99999
        for i in range(len(q)):
            if i != indi:
                suma = 0
                for j in range(len(q)):
                    suma += q[i][j]

                if suma < mini:
                    mini = suma
                    indiceSucu = i
        return indiceSucu, mini
    
if __name__ == '__main__':
    sucursales = ["A", "B", "C", "D", "E"]
    g = grafo(5)
    g.insertarPonderado(1,2,2)
    g.insertarPonderado(1,5,10)
    g.insertarPonderado(2,5,10)
    g.insertarPonderado(2,3,3)
    g.insertarPonderado(3,5,8)
    g.insertarPonderado(3,4,10)
    g.insertarPonderado(4,5,5)

    indi, mini = g.sucursal()
    s = sucursales[indi]
    indi1, mini1 = g.sucursal2(indi)
    s1 = sucursales[indi1]
    print(f"Sucursal Optima 1: {s} - Distancia Minimina: {mini}")
    print(f"Sucursal Optima 2: {s1} - Distancia Minimina: {mini1}")