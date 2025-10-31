from ColaEncadenada import cola
import numpy as np


class digrafo_secuencial:
    __matriz: np.array
    __tamanio: int

    def __init__ (self, m):
        self.__tamanio = m
        self.__matriz = np.full((m, m), float("inf"))

    ##Insertar DiGrafos Ponderados
    def insertar_ponderado (self, v1, v2, p):
        u = v1 -1
        v = v2 -1 
        if self.__matriz[u][v] != float("inf"):
            print("Los vertices ya estan ocupados.")
        else:
            self.__matriz[u][v] = p

    
    def camino_minimo (self):
        n = self.__tamanio
        Q = self.__matriz.copy()

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    Q[i][j] =  min(Q[i][j], Q[i][k] + Q[k][j])
        return Q
    
if __name__ == '__main__':
    nombre = ["Ana", "Belen", "Cecilia", "Daniel", "Ezequiel", "Federico"]

    d = digrafo_secuencial(6)
    d.insertar_ponderado(1,2,3)
    d.insertar_ponderado(1,4,6)
    d.insertar_ponderado(2,3,1)
    d.insertar_ponderado(2,5,2)
    d.insertar_ponderado(2,6,1)
    d.insertar_ponderado(3,4,2)
    d.insertar_ponderado(4,2,3)
    d.insertar_ponderado(5,4,3)
    d.insertar_ponderado(5,6,2)
    d.insertar_ponderado(6,4,1)
    d.insertar_ponderado(5,1,3)

    costMin = d.camino_minimo()
    o = 1
    d = 4
    print(f"El costo minimo de SMS de {nombre [o-1]} a {nombre[d-1]} es de: {costMin[o-1][d-1]}")