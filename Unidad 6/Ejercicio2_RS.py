##Implementacion de digrafo ponderado y no ponderado

from ColaEncadenada import cola
import numpy as np
import copy

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
            print("Insercion exitosa.")


    ##Insertar DiGrafos Ponderados
    def insertar_ponderado (self, v1, v2, p):
        u = v1 -1
        v = v2 -1 
        if self.__matriz[u][v] != 0:
            print("Los vertices ya estan ocupados.")
        else:
            self.__matriz[u][v] = p
            print("Insercion exitosa.")

    def obtenerAdyacentes (self, v1):
        u = v1 - 1
        listaAdyacentes = []
        for i in range(self.__tamanio):
            if self.__matriz[u][i] != 0:
                listaAdyacentes.append(i)
        print(listaAdyacentes)
    
    def verificarAdyacente (self, u, v):
        if self.__matriz[u][v] != 0:
            return True
        else:
            return False


    ## Se utiliza el REA para conexo    
    def fuertemente_conexo (self):
        s = 0
        visitados = np.full(self.__tamanio, False, dtype=bool)
        colaE = cola()
        colaE.insertar(s)
        while not colaE.vacia():
            v = colaE.suprimir()
            for u in range(self.__tamanio):
                if (self.verificarAdyacente(v,u) and self.verificarAdyacente(u,v)) and visitados[u] == False:
                    visitados[u] = True
                    colaE.insertar(u)
        if all(visitados):
            return True
        else:
            return False
        
    def simple_conexo (self):
        s = 0
        visitados = np.full(self.__tamanio, False, dtype=bool)
        colaE = cola()
        colaE.insertar(s)
        while not colaE.vacia():
            v = colaE.suprimir()
            for u in range(self.__tamanio):
                if (self.verificarAdyacente(v,u) or self.verificarAdyacente(u,v)) and visitados[u] == False:
                    visitados[u] = True
                    colaE.insertar(u)
        if all(visitados):
            return True
        else:
            return False
        
    ## Busqueda en anchura para camino y verificar si es conexo
    ## Camino de un grafo NO PONDERADO
    def camino (self, v1, v2):
        s = v1 -1
        x = v2 -1
        d = np.empty(self.__tamanio, dtype=object)
        padres = np.full(self.__tamanio, -1)
        camino = []
        colaE = cola()
        for v in range(self.__tamanio):
            d[v] = float("inf")
        d[s] = 0
        colaE.insertar(s)
        encontrado = False
        while not colaE.vacia() and not encontrado:
            v = colaE.suprimir()
            if v == x:
                encontrado = True
            else:
                for u in range(self.__tamanio):
                    if self.verificarAdyacente(v, u) and d[u] == float("inf"):
                            d[u] = d[v] + 1
                            padres[u] = v ## Guardamos el u, ya que este obtuvismo para llegar a v
                            colaE.insertar(u)
            
        actual = x ## Reconstruccion del camino desde el destino
        while actual != -1:
            camino.insert(0, actual +1)
            actual = padres[actual]
        
        for i in range(len(camino)):
            print(f"Camino de {v1} a {v2}: {camino[i]}")

    ##Dijkstra para grafos ponderados de caminos minimos

    def dijkstra (self):
        pass


    ##Busqueda en profundidad nos permite detectar si tiene ciclos
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
        
    ## Los recorridos nos permiten detectar Ciclos, si un grafo es conexo, orden topologico, etc.

    ## Recorrido en anchura. Codigo de la teoria
    def REA (self, v1):
        s = v1 -1
        d = np.empty(self.__tamanio, dtype=object)
        colaE = cola()
        for v in range(self.__tamanio):
            d[v] = float("inf")
        d[s] = 0
        colaE.insertar(s)
        while not colaE.vacia():
            v = colaE.suprimir()
            for u in range(self.__tamanio):
                if self.verificarAdyacente(v, u) and d[u] == float("inf"):
                        d[u] = d[v] + 1
                        colaE.insertar(u)
        return d


    ## Recorrido en profundidad. Codigo de la teoria
    def REP (self):
        d = np.zeros(self.__tamanio, dtype=int)
        f = np.zeros(self.__tamanio, dtype=int)
        tiempo = [0] ## Nos permite modificar la variable tanto afuera de esta funcion como adentro
        for s in range(self.__tamanio):
            if d[s] == 0:
                self.REP_visita (s, tiempo, d, f)

        print(d)
        print(f)

    def REP_visita (self, s, tiempo, d, f):
        tiempo[0] += 1
        d[s] = tiempo[0]
        for u in range(self.__tamanio):
            if self.verificarAdyacente(s,u) and d[u] == 0:
                self.REP_visita(u, tiempo, d, f)

        tiempo[0] += 1
        f[s] = tiempo[0]


    def grado_salida (self, v1):
        u = v1 -1
        cont = 0
        for j in range(self.__tamanio):
            if self.__matriz[u][j] != 0:
                cont += 1
        return cont
    
    def grado_entrada (self, v1):
        u = v1 -1
        cont = 0
        for i in range(self.__tamanio):
            if self.__matriz[i][u] != 0:
                cont += 1
        return cont
    
    def nodo_fuente (self, v1):
        return self.grado_entrada(v1) == 0 and self.grado_salida(v1) > 0
    
    def nodo_sumidero (self, v1):
        return self.grado_entrada(v1) > 0 and self.grado_salida(v1) == 0
    
if __name__ == "__main__":
    # Creamos un dígrafo de 5 nodos
    g = digrafo_secuencial(5)

    # Insertamos aristas no ponderadas
    g.insertar_noPonderado(1, 2)
    g.insertar_noPonderado(2, 3)
    g.insertar_noPonderado(3, 4)
    g.insertar_noPonderado(4, 5)
    g.insertar_noPonderado(5, 1)  # Esto genera un ciclo

    print("\nMatriz de adyacencia:")
    print(g._digrafo_secuencial__matriz)

    # Verificar caminos
    print("\nCamino de 1 a 4:")
    g.camino(1, 4)

    # Verificar si es acíclico
    print("\nEs acíclico?")
    print(g.es_aciclico())

    # Verificar conectividad
    print("\nSimplemente conexo?")
    print(g.simple_conexo())

    print("\nNodo fuente y sumidero:")
    for i in range(1, 6):
        print(f"Nodo {i} fuente? {g.nodo_fuente(i)}, sumidero? {g.nodo_sumidero(i)}")

