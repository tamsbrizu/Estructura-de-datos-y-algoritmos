from PilaSecuencial import Pila
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
    
    def obtener_tamanio (self):
        return self.__tamanio
    
    def orden_topologico (self, u, visitados = None, p = None):
        if self.es_aciclico():
            if p is None:
                p = Pila(self.__tamanio)
            if visitados is None:
                visitados = np.full(self.__tamanio, False, dtype = bool)
            
            if visitados[u] == False:
                visitados[u] = True
                for i in range(self.__tamanio):
                    if self.verificarAdyacente(u, i) and visitados[i] == False:
                        self.orden_topologico(i, visitados, p)
                p.insertar(u)
                
            for i in range(self.__tamanio):
                if visitados[i] == False:
                    self.orden_topologico(i, visitados, p)

            return p
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


    print("Orden topológico de materias:")
    pi = di.orden_topologico(0)
    while not pi.vacia():
        x = pi.suprimir()
        print(materias[x])
    

'''Notas del ejercicio 4 dadas por el profe
    llevar un grafo a una lista ordenada
    debe ser digrafo y aciclico
    no se pude decir que un nodo esta antes que otro porque se apuntan mutuamente
    empezar por los nodos que no tiene que no tienen ninguna entrada (ED I & A-E II)
    ED I - AE II - AE III - ED II - ED III - TRAD INT
    ¿Como se implementa?
    hay dos manerasa (en el apunte), 1. surgieron modificar la busqueda en profunidad e incorporarlo en una pila, desapilamos y lo imprimimos
    2.  grados de entrada en una tabla. Los nodos vertices que tienen grado cero se añaden en una cola. Al insertarlos en la cola
    vamos a recorrer todos los adyacentes y le vamos a incrementar uno el que tiene 2 y asi
    para marcarlos les ponemos -1
    recorrer con un for  que esta dentro del while para vericiar si un nodo cero
    una vez que termina ese while, todos los nodos deben estar en -1. Si todos estan positivos significa que hay un bucle.

    El orden va a variar dependiendo del orden en que se inicialize el nodo.
'''

