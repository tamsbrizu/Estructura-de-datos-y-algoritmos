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

    
    '''def camino_minimo(self, origen):
        """Algoritmo de Dijkstra desde un vértice origen"""
        n = self.__tamanio
        o = origen - 1  # Convertir a índice 0
        
        # Inicializar tabla T: [distancia, camino, conocido]
        distancia = [float('inf')] * n
        conocido = [False] * n
        distancia[o] = 0
        
        # Para i desde 1 hasta |V| hacer
        for _ in range(n):
            # v ← vertice con distancia minima y desconocido
            min_dist = float('inf')
            v = -1
            for i in range(n):
                if not conocido[i] and distancia[i] < min_dist:
                    min_dist = distancia[i]
                    v = i
            
            if v == -1:
                break
            
            # T[v].conocido ← True
            conocido[v] = True
            
            # Para cada w adyacente a v hacer
            for w in range(n):
                if self.__matriz[v][w] != float('inf'):  # Si es adyacente
                    # Si T[w].conocido = False
                    if not conocido[w]:
                        # Si T[v].distancia + w(v,w) < T[w].distancia
                        nueva = distancia[v] + self.__matriz[v][w]
                        if nueva < distancia[w]:
                            distancia[w] = nueva
        
        return distancia'''
    
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

    o = 6
    destino = 5
    distancias = d.camino_minimo()
    
    print(f"El costo minimo de SMS de {nombre[o-1]} a {nombre[destino-1]} es de: {distancias[o-1][destino-1]}")