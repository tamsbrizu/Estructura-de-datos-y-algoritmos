from ColaEncadenada import cola
import numpy as np

class grafo:
    __tamanio: int
    __matriz: np.array

    def __init__ (self, n):
        self.__tamanio = n
        self.__matriz = np.zeros((n,n), dtype=int)

    def insertar (self, v1, v2):
        u = v1 -1
        v = v2 - 1
        if self.__matriz[u][v] != 0:
            print("Los vertices ya estan conectados.")
        else:
            self.__matriz[u][v] = 1
            self.__matriz[v][u] = 1
        
    ##Insercion para grafo Ponderado
    def insertarPonderado (self, v1, v2, p):
        u = v1 -1
        v = v2 - 1
        if self.__matriz[u][v] != 0:
            print("Los vertices ya estan conectados.")
        else:
            self.__matriz[u][v] = p
            self.__matriz[v][u] = p
        

    ## Regresa una lista con los adyacentes
    def verticesAdyacentes (self, v1):
        listaAdyacentes = []
        u = v1 -1
        for i in range(self.__tamanio):
            if self.__matriz[u][i] != 0:
                listaAdyacentes.append(i+1)
        return listaAdyacentes
    

    ## Regresa True o False si los elementos pasados por parametros son adyacentes
    def verificarAdyacente (self, u, v):
        if self.__matriz[u][v] != 0:
            return True
        else:
            return False
        
    
    ## Se utiliza el REA para conexo    
    def conexo (self):
        s = 0
        visitados = np.full(self.__tamanio, False, dtype=bool)
        colaE = cola()
        visitados[s] = True
        colaE.insertar(s)
        while not colaE.vacia():
            v = colaE.suprimir()
            for u in range(self.__tamanio):
                if self.verificarAdyacente(v,u) and visitados[u] == False:
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

        if d[x] == float("inf"): ## Si desde donde iniciamos sigue siendo infinito entonces no existe camino desde v1 a v2
            print(f"No existe camino de {v1} a  {v2}")
            return                   
            
        actual = x ## Reconstruccion del camino desde el destino
        while actual != -1:
            camino.insert(0, actual +1)
            actual = padres[actual]
        
        for i in range(len(camino)):
            print(f"Camino de {v1} a {v2}: {camino[i]}")

    ##Dijkstra para grafos ponderados de caminos minimos


    ##Busqueda en profundidad nos permite detectar si tiene ciclos
    def es_aciclico (self):
        visitados = np.full(self.__tamanio, False, dtype=bool)
        for s in range(self.__tamanio):
            if visitados[s] == False:
                if self.ciclo (s, visitados, -1): ## -1 es el padre del primer nodo, ya que este no tiene padre
                    return False ## Hay ciclo
        return True ## Es aciclico
        
    def ciclo (self, s, visitados, p):
        visitados[s] = True ##Ponemos el nodo del cual llegamos en verderadero
        for v in range(self.__tamanio):
            if visitados[v] == False and self.verificarAdyacente(s,v): ##Si s y v son adyacentes y v no fue visitado
                if self.ciclo(v,visitados, p=s): ##Recursion
                    return True
            elif v != p and self.verificarAdyacente(s,v): ## Si v ya fue visitado y v no es mi padre. Es decir verifica si el nodo anterior no es padre
                ## como es un grafo no dirigido, va a suceder que regresemos por el nodo padre pero eso no significa que tiene un ciclo
                return True ## ciclo
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

def main():
    # Creamos un grafo con 5 nodos
    g = grafo(5)

    # Insertamos aristas (grafo no ponderado)
    g.insertar(1, 2)
    g.insertar(1, 3)
    g.insertar(2, 4)
    g.insertar(3, 5)
    g.insertar(4, 5)  # Esto crea un ciclo

    # Mostrar camino entre dos nodos
    print("Camino de 1 a 5:")
    g.camino(1, 5)

    # Verificar si el grafo es acíclico
    if g.es_aciclico():
        print("El grafo es acíclico")
    else:
        print("El grafo tiene ciclos")

    # Recorrido en anchura desde el nodo 1
    print("Recorrido en anchura (REA) desde 1:")
    distancias = g.REA(1)
    print(distancias)

    # Recorrido en profundidad (REP)
    print("Recorrido en profundidad (REP):")
    g.REP()

    # Lista de adyacentes de un nodo
    print("Vértices adyacentes a 1:", g.verticesAdyacentes(1))

    # Verificar si dos nodos son adyacentes
    print("¿1 y 2 son adyacentes?", g.verificarAdyacente(1-1, 2-1))
    print("¿1 y 4 son adyacentes?", g.verificarAdyacente(1-1, 4-1))

    # Verificar si el grafo es conexo
    if g.conexo():
        print("El grafo es conexo")
    else:
        print("El grafo no es conexo")

if __name__ == "__main__":
    main()












    