##Encadenada

import numpy as np

class Nodo:
    __elemento: None
    __sig: None

    def __init__ (self, e):
        self.__elemento = e
        self.__sig = None

    def obtener_elemento(self):
        return self.__elemento
    
    def obtener_sig (self):
        return self.__sig
    
    def set_sig (self, valor):
        self.__sig = valor


class encadenada:
    __tabla: np.array
    __cantidadC: int
    __M: int
    __tablaColisiones: np.array

    def __init__ (self, m = 10, c = 4):
        self.__cantidadC = c
        self.__M = self.primo (int(m/c))
        self.__tabla = np.empty (self.__M, dtype=object)
        self.__tablaColisiones = np.zeros(self.__M, dtype = int)

    def primo (self, m):
        es_primo = None
        while es_primo is None:
            i = 2
            while i < m and m % i != 0:
                i+=1
            if m == i:
                es_primo = m
            else:
                m += 1
        return m
    
    def divisones (self, clave):
        return clave % self.__M
    
    def insertar (self, clave):
        pos = self.divisones(clave)
        nuevo = Nodo(clave)
        if self.__tabla[pos] is None:
            self.__tabla[pos] = nuevo
        else:
            if self.__tablaColisiones[pos] < self.__cantidadC:
                nuevo.set_sig(self.__tabla[pos])
                self.__tabla[pos] = nuevo
                self.__tablaColisiones[pos] += 1
            else:
                print(f"No se puede insertar {clave}: se superó la cantidad máxima de colisiones permitidas en la posición {pos}")
            
    def buscar (self, clave):
        comparaciones = 1
        ban = False
        pos = self.divisones(clave)
        aux = self.__tabla[pos]
        while not ban and aux is not None:
            if aux.obtener_elemento() == clave:
                print(f"La cantidad de comparaciones exitosas es de {comparaciones}")
                ban = True
            else:
                aux = aux.obtener_sig()
                comparaciones += 1
        if not ban:
            print(f"La cantidad de comparaciones no exitosas fue de: {comparaciones}")

    ##Este recorrer no lo hice yo
    def recorrer(self):
        print("\n=== TABLA HASH CON ENCADENAMIENTO ===")
        for i in range(self.__M):
            print(f"[{i}] -> ", end="")
            aux = self.__tabla[i]
            if aux is None:
                print("None")
            else:
                while aux is not None:
                    print(f"{aux.obtener_elemento()} -> ", end="")
                    aux = aux.obtener_sig()
                print("None")


if __name__ == '__main__':
    h = encadenada()

    # Insertamos claves
    h.insertar(10)
    h.insertar(99)
    h.insertar(65)
    h.insertar(17)
    h.insertar(67)
    h.insertar(15)
    h.insertar(25)

    # Mostramos la tabla completa
    h.recorrer()

    # Búsquedas
    h.buscar(15)
    h.buscar(99)
    h.buscar(999)


