from ColaEncadenada import cola

import numpy as np

class grafo_secuencial:
    __matriz: np.array
    __tamanio: int

    def __init__ (self, m):
        self.__tamanio = m
        self.__matriz = np.zeros ([m, m], dtype = int)

    def insertar_mAdyacencia (self, u, v):
        if self.__matriz[u, v] == 1:
            print("Vertices incorrectos, ya estan ocupados.")
        else:
            self.__matriz[u, v] = 1
            self.__matriz[v, u] = 1

    def insertar_mPesos (self, u, v, p):
        if self.__matriz[u, v] != 0:
            print("Vertices incorrectos, ya estan ocupados.")
        else:
            self.__matriz[u, v] = p
            self.__matriz[v, u] = p

    def adyacentes (self, u):
        v = 0
        lista = []
        for v in range(self.__tamanio):
            if self.__matriz[u][v] != 0:
                lista.append(v)
        return lista
    
    def es_adyacente (self, u, v):
        return self.__matriz[u][v] == 1

    
    def eliminar_arista (self, u, v):
        if self.__matriz[u][v] == 0:
            print("No hay arista en los vertices")
        else:
            self.__matriz[u][v] = 0
            self.__matriz[v][u] = 0

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
    
    def camino (self, u, v):
        vertices = np.empty(self.__tamanio, dtype=object)
        colaE = cola()
        encontrado = False
        camino = ""
        for i in range(len(vertices)):
            vertices[i] = "inf"

        vertices[u] = 0
        colaE.insertar(u)

        while not colaE.vacia() and not encontrado:
            x = colaE.suprimir()
            camino += f" -> {x}"
            for i in range(len(vertices)):
                if self.es_adyacente(x, i):
                    if i == v:
                        encontrado = True
                        camino += f" -> {i}"
                    else:
                        if vertices[i] == "inf":
                            vertices[i] = vertices[x] + 1
                            cola.insertar(i)

        if encontrado:
            return camino
        else:
            print(f"No hay camino desde {u} hasta {v}")

    
    def aciclico (self):
        visitados = np.full(self.__tamanio, False)
        for i in range(len(visitados)):
            if visitados[i] == False:
                if self.ciclo (i, visitados, padre = 0):
                    return False
        return True
    
    def ciclo (self, i, visitados, padre):
        visitados[i] = True
        for j in range(len(visitados)):
            if self.es_adyacente(i, j):
                if visitados[j] == False:
                    if self.ciclo(j, visitados, i):
                        return True
                    if j != padre:
                        return True
        return True
    

    def conexo (self):
        visitados = np.full(self.__tamanio, False)

        for i in range(len(visitados)):
            if i + 1 < len(visitados):
                if self.es_adyacente(i, i +1) and self.es_adyacente(i+1, i):
                    visitados[i] = True

        if all(visitados):
            print("Es conexo")
        else:
            print("No es conexo.")



    '''def conexo (self):
        i = 0
        visitados = np.full(self.__tamanio, False)
        colaE = cola()
        visitados[i] = True
        colaE.insertar(i)

        while not colaE.vacia():
            v = colaE.suprimir()
            for i in range(self.__tamanio):
                if self.es_adyacente(v, i) and visitados[i] == False:
                    visitados[i] = True
                    colaE.insertar(i)

        if all(visitados):
            print("Es conexo")
        else:
            print("No es conexo.")'''    



    def mostrar (self):
        for i in range(self.__tamanio):
            for j in range(self.__tamanio):
                print(f"Fila: {i} - Columna: {j} --- > {self.__matriz[i][j]}")

    
                



    