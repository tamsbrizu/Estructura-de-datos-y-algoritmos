'''Ejercicio 2: Reproductor de Música (Lista Secuencial, lista encadenada)
Objetivo: Administrar una lista de canciones permitiendo agregar, insertar y eliminar .
Se pide:
-	Agregar una canción al final de la lista
-	Insertar una canción en una posición especifica
-	Dada una posición mostrar el titulo de la cancion almacenada en esa posición
-	Dado el nombre de una canción mostrar la posición de la lista en la que se encuentra
-	Dada una posición eliminar la canción que en ella se encuentra
-	Mostrar la lista de Reproducion'''

import numpy as np

class ls:
    __cant: int
    __max: int
    __ul: int
    __elementos: np.array

    def __init__(self, maxx):
        self.__cant = 0
        self.__max = maxx
        self.__ul = -1
        self.__elementos = np.empty(self.__max, dtype= "U100")


    def vacia (self):
        return self.__cant == 0
    
    def llena (self):
        return self.__cant == len(self.__elementos)
    
    def obtener_ul (self):
        return self.__ul
    
    def insertarFinal (self, x):
        self.__ul += 1
        self.__elementos[self.__ul] = x
        self.__cant += 1

    def insertar (self, x, p):
        if p >= 1 and p <= self.__cant + 1:
                i = self.__cant - 1

                while i >= p-1:
                    self.__elementos[i+1] = self.__elementos[i]
                    i -= 1

                self.__elementos[p-1] = x
                self.__ul += 1
                self.__cant += 1

        else:
            print("Posicion invalida para insertar.")

    def obtener_titulo (self, p):
        return self.__elementos[p-1]
    
    def busqueda (self, x):
        i = 0
        ban = False
        while not ban and i < self.__cant:
            if self.__elementos[i] == x:
                ban = True
            else:
                i += 1

        if ban:
            return i
        else:
            return -1
        

    def suprimir (self, p):
        if p >= 1 and p <= self.__cant:
            eliminado = self.__elementos[p-1]
            i = p-1
            while i < self.__cant-1:
                self.__elementos[i] = self.__elementos[i+1]
                i += 1

            self.__cant -= 1
            self.__ul = self.__cant - 1
            return eliminado
        else:
            print("Posicion invalida para suprimir")
        

    def recorrer (self):
        for i in range(self.__cant):
            print(self.__elementos[i])


if __name__ == "__main__":

    canciones = ls(100)

    print("\nInsertando elementos...")
    canciones.insertar("Outside", 1)
    canciones.insertar("Work", 2)
    canciones.insertar("Bad desire", 3)

    print("\nMostrando las canciones en la lista")
    canciones.recorrer()

    print("\nInsertar Elemento al final...")
    canciones.insertarFinal("Love & Peach")

    print("\nRecorriendo la lista con el nuevo elemento al final...")
    canciones.recorrer()

    print("\nInsertando elemento en la posicion especifica 1")
    canciones.insertar("Sweet Venom", 1)

    print("\nMostrando la lista con el elemento en la posicion especifica.")
    canciones.recorrer()

    print("\nMostrando una cancion en posicion especifica....")
    can = canciones.obtener_titulo(2)
    print(f"La cancion en la posicion especifica es: {can}")

    print("\nBuscando titulo y obtener posicion...")
    c = canciones.busqueda("Sweet Venom")
    print(f"La posicion de la cancion buscada es: {c}")


    print("\nEliminando en posicion indicada")
    canciones.suprimir(2)

    print("\nMostrando la lista una vez que se elimina el elemento...")
    canciones.recorrer()