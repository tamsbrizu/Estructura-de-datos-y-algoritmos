import numpy as np

class Elementobucket:
    __bucket: np.array
    __colisiones: int
    __tam: int

    def __init__ (self, t):
        self.__tam = t
        self.__colisiones = 0
        self.__bucket = np.empty (self.__tam, dtype = object)

    def bucket_lleno (self):
        return self.__colisiones == self.__tam
    
    def bucket_insertar (self, clave):
        self.__bucket[self.__colisiones] = clave
        self.__colisiones += 1
     
    def bucket_buscar (self, clave, comparaciones):
        i = 0
        ban = False
        while not ban and i <= self.__tam:
            if self.__bucket[i] == clave:
                ban = True
                return comparaciones
            else:
                i += 1
                comparaciones += 1
        if not ban:
            return comparaciones
        
    def bucket_recorrer (self):
        for i in range(self.__tam):
            print(self.__bucket[i])
        
    
class tablaBucket:
    __tabla: np.array
    __M: int
    __colisionesMax: int

    def __init__ (self, m = 10, coli = 5):
        self.__colisionesMax = coli
        self.__M = self.primo(int(m/coli))
        self.__tabla = np.empty (self.primo(int(self.__M *1.2)), dtype=object)
    
    def inicializar_tabla(self):
        for i in range(self.primo(int(self.__M *1.2))):
            self.__tabla[i] = Elementobucket(self.__colisionesMax)

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
        if not self.__tabla[pos].bucket_lleno():
            self.__tabla[pos].bucket_insertar(clave)
        else:
            pos = self.__M
            while pos < len(self.__tabla) and self.__tabla[pos].bucket_lleno():
                pos = pos + 1
            if not self.__tabla[pos].bucket_lleno():
                self.__tabla[pos].bucket_insertar(clave)


    ##Falta corregir
    def buscar (self, clave):
        ban = False
        comparaciones = 1
        pos = self.divisones(clave)
        resultado = self.__tabla[pos].bucket_buscar (clave, comparaciones)
        if resultado == self.__colisionesMax:
            pos = self.__M
            while pos < len(self.__tabla) and not ban:
                resultado = self.__tabla[pos].bucket_buscar (clave, comparaciones)
                comparaciones += resultado
                if comparaciones < self.__colisionesMax:
                    ban = True
                pos = pos + 1
        else:
            print(F"La cantidad de comparaciones exitosas fue de: {comparaciones}")
