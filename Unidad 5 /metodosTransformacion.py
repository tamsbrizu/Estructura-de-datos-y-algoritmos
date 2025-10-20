## Debo arreglar estos metodos. Los metodos que estan totalmente bien son divisiones y alfanumericos, los demas faltan detalles



## Metodos de transformacion
## Ejemplo: abcdef, clave[1:4], toma desde el caracter 1 (sin incluirlo) hasta 4 (sin incluirlo), es decir; "bc". Cuando utilizamos clave[..] devuelve una cadena
import numpy as np

class direccionamientoA:
    __M: int
    __tabla: np.array

    def __init__ (self, m):
        self.__M = self.primo(int(m/0.7))
        self.__tabla = np.empty(self.__M, dtype=object)
    
##Primo para manejar mejor el espacio
    def primo (self, m):
        es_p = None
        while es_p == None:
            i = 2
            while i < m and m%i != 0:
                i += 1
            if i == m:
                es_p = m
            else:
                m += 1
        return es_p
    
    def divisiones (self, clave):
        return clave % self.__M
    
    def extraccion (self, clave):
        str_c = str(clave)
        if len(str_c) > 3:
            return int(str_c[-3:]) % self.__M
        else:
            return clave % self.__M
    
    def plegado (self, clave):
        suma = 0
        for i in range (0, len(clave), 2): ##Significa que avanza de dos en dos, es decir, empieza 0 hasta la longitud de la clave y luego avanza dos
            bloque = int(clave[i:i+2])
            suma += bloque
        return suma % self.__M
    
    def cuadradoMedio (self, clave):
        c = str(clave ** 2)
        if len(c) >= 4:
            ind = len(c) // 2 ## Nos da el centro, o sea el indice del medio
            return int(c[ind-1: ind+2])%self.__M ##ind-1 tomamos del indice -1 hasta el indice +1
        else:
            return int(c) % self.__M
        
    def alfanumerico (self, clave, base = 31, i = 0):
        suma = 0
        for char in str(clave):
            i += 1
            suma += (ord(char) * ((base) ** i))
        return suma % self.__M
