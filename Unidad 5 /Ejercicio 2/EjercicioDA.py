## Direcionamiento abierto

import numpy as np

class DA_Hashing:
    __tabla: np.array
    __M: int

    def __init__ (self, m = 10):
        self.__M = self.primo (int(m/0.7))
        self.__tabla = np.empty(self.__M, dtype=object)
    
    def primo (self, m):
        es_primo = None
        while es_primo is None:
            i = 2
            while i < m and m % i != 0:
                i += 1
            if m == i:
                es_primo = m
            else:
                m += 1
        return es_primo
    
    def divisiones (self, clave):
        return clave % self.__M
    
    def secuenciaLineal (self, pos, clave):
        inicio = pos
        while self.__tabla[pos] != clave and self.__tabla[pos] is not None:
            pos = (pos + 1) % self.__M
            if inicio == pos:
                return None
        return pos
        
    def insertar (self, clave):
        pos = self.divisiones(clave)
        if self.__tabla[pos] is None:
            self.__tabla[pos] = clave
        else:
            p = self.secuenciaLineal(pos, clave)
            if p is not None:
                self.__tabla[p] = clave
            else:
                print("No hay posiciones libre o el elemento ya fue insertado")
    
    def buscar (self, clave):
        pos = self.divisiones(clave)
        comparaciones = 1
        if self.__tabla[pos] == clave:
            print(f"La cantidad de comparaciones exitosas es de: {comparaciones}")
        else:
            inicio = pos
            while self.__tabla[pos] != clave and self.__tabla[pos] is not None:
                pos = (pos + 1) % self.__M
                comparaciones += 1
                if inicio == pos:
                    pos = None
            if pos is not None and self.__tabla[pos] == clave:
                print(f"La cantidad de comparaciones exitosas es de: {comparaciones}")
            else:
                print(f"La cantidad de comparaciones no exitosas es de: {comparaciones}")

    def recorrer (self):
        for i in range(self.__M):
            print(self.__tabla[i])


if __name__ == '__main__':
    da = DA_Hashing()

    da.insertar(10)
    da.insertar(99)
    da.insertar(65)
    da.insertar(17)
    da.insertar(67)
    da.insertar(15)
    da.insertar(25)

    da.recorrer()

    da.buscar(15)
    da.buscar(25)
    da.buscar(790)