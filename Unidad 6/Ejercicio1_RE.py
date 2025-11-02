from ColaEncadenada import cola
from ClaseNodo import Nodo
from ClaseNodoPonderado import NodoP
import numpy as np

class grafo_encadenado:
    __tabla: np.array
    __tamanio: int

    def __init__ (self, n):
        self.__tamanio = n
        self.__tabla = np.empty (self.__tamanio, dtype = object)

    def insertar(self, v1, v2):
        u = v1-1
        v = v2-1
        
        nuevoNodo1 = Nodo(v)
        nuevoNodo1.set_sig(self.__tabla[u])
        self.__tabla[u] = nuevoNodo1

        nuevoNodo2 = Nodo(u)
        nuevoNodo2.set_sig(self.__tabla[v])
        self.__tabla[v] = nuevoNodo2

    def insertarPonderado (self, v1,v2,p):
        u = v1-1
        v = v2-1

        nuevoNodo1 = NodoP(v, p)
        nuevoNodo1.set_sig(self.__tabla[u])
        self.__tabla[u] = nuevoNodo1

        nuevoNodo2 = NodoP(u,p)
        nuevoNodo2.set_sig(self.__tabla[v])
        self.__tabla[v] = nuevoNodo2

    def obtenerAdyacentes (self, v1):
        u = v1-1
        listaAdya = []
        aux = self.__tabla[u]
        while aux is not None:
            listaAdya.append(aux.obtener_elemento()+1)
            aux = aux.obtener_sig()
        return listaAdya
    
    
    def verificarAdyacente (self, u, v):
        aux = self.__tabla[u]
        ban = False
        while not ban and aux is not None:
            if aux.obtener_elemento() == v:
                ban = True
            else:
                aux = aux.obtener_sig()
        return ban
    

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
            camino.insert(0, actual +1) ##Coloca los elementos al inicio de la lista. Ya que estan en orden inverso
            actual = padres[actual]
        
        for i in range(len(camino)):
            print(f"Camino de {v1} a {v2}: {camino[i]}")
    
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
        d = np.zeros(self.__tamanio, dtype=int) ## INICIO
        f = np.zeros(self.__tamanio, dtype=int) ## FIN
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


if __name__ == "__main__":
    g = grafo_encadenado(5)

    # Insertamos aristas
    g.insertar(1, 2)
    g.insertar(1, 3)
    g.insertar(2, 4)
    g.insertar(3, 5)

    print("¿Es conexo?:", g.conexo())
    print("\nCamino de 1 a 4:")
    g.camino(1,4)

    print("\nCamino de 5 a 2:")
    g.camino(5,2)

    print("\nAdyacentes de 1:", g.obtenerAdyacentes(1))

    print("\nDFS (REP):")
    g.REP()

    print("\n¿Es acíclico?:", g.es_aciclico())

    
    

    