from ColaEncadenada import cola
import numpy as np

class digrafo_secuencial:
    __matriz: np.array
    __tamanio: int

    def __init__ (self, m):
        self.__tamanio = m
        self.__matriz = np.zeros((m, m), dtype=int)

    def insertar_noPonderado (self, v1, v2):
        u = v1 -1
        v = v2 -1 
        if self.__matriz[u][v] == 1:
            print("Los vertices ya estan ocupados.")
        else:
            self.__matriz[u][v] = 1

    def verificarAdyacente (self, u, v):
        if self.__matriz[u][v] != 0:
            return True
        else:
            return False

    def es_aciclico (self):
        # 0 = no visitado, 1 = visitando, 2 = visitado (ya procesado)
        estado = np.zeros(self.__tamanio, dtype=int)
        for s in range(self.__tamanio):
            if estado[s] == 0:
                if self.ciclo (s, estado): ## si encontramos ciclo
                    return False ## Hay ciclo
        return True ## Es aciclico
        
    def ciclo (self, s, estado):
        estado[s] = 1 ##Ponemos el nodo del cual llegamos en 1
        for v in range(self.__tamanio):
            if estado[v] == 0 and self.verificarAdyacente(s,v): ##Si s y v son adyacentes y v no fue visitado
                if self.ciclo(v,estado): ##Recursion
                    return True
            elif estado[v] == 1 and self.verificarAdyacente(s,v): ## Si el nodo ya fue visitado, entonces encontramos un ciclo
                return True ## ciclo
            
        ## terminamos y no encontramos ciclo. Marcamos el origen s como visitado
        estado[s] = 2
        return False ## no tiene ciclo
    
    def orden_topologico (self, u, visitados = None, resultado = None):
        if self.es_aciclico():
            if visitados is None: 
                visitados = np.full(self.__tamanio, False, dtype= bool)
            if resultado is None:
                resultado = []
            visitados[u] = True
            for w in range(self.__tamanio):
                if self.verificarAdyacente(u,w) and visitados[w] == False:
                    self.orden_topologico(w, visitados, resultado)
            resultado.insert(0, u)  # Insertar al inicio para que quede en orden topológico
        
            for i in range(self.__tamanio):
                if not visitados[i]:
                    self.orden_topologico(i,visitados, resultado)          
            return resultado
        else:
            print("El orden topologico solo se obtiene en digrafos aciclicos.")
    
if __name__ == '__main__':
    materias = ["ED I", "ED II", "ED III", "A-E II", "A-E III", "TRAD-INT"]

    di = digrafo_secuencial(6)  # Cambiado a 6 nodos
    
    di.insertar_noPonderado(1,2)
    di.insertar_noPonderado(1,4)
    di.insertar_noPonderado(2,3)
    di.insertar_noPonderado(3,5)
    di.insertar_noPonderado(4,5)
    di.insertar_noPonderado(6,4)


    resultado = di.orden_topologico(0)
    if resultado:
        print("Orden topológico de materias:")
        for i in resultado:
            print(materias[i])

