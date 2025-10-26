##Direccinamiento abierto

##Metodos de transformacion: division, extraccion, plegado, cuadradoMedio

import numpy as np
import math

class direccionamientoA:
    __M: int
    __tabla: np.array

    def __init__ (self, m):
        self.__M = self.primo(round(m/0.7))
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
    
##Metodo para obtener el numero primo mas cercano al tamaño del arreglo
    
## Metodos de transformacion
## Ejemplo: abcdef, clave[1:4], toma desde el caracter 1 (sin incluirlo) hasta 4 (sin incluirlo), es decir; "bc". Cuando utilizamos clave[..] devuelve una cadena
    def divisiones (self, clave):
        return clave % self.__M
    
## Secuencia de prueba lineal

## Si manejamos claves unicas, no volvemos a insertar el mismo numero por eso es importante verificar que no se vuelva a repetir
    def secuenciaPrueba (self, clave, pos):
        inicio = pos
        while self.__tabla[pos] != clave and self.__tabla[pos] is not None:
            pos = (pos+1) % self.__M
            if pos == inicio:
                return None
        return pos


##Operaciones de abstractas. Metodo de transformacion: divisiones

    def insertar (self, clave):
            posi = self.divisiones(clave)
            if self.__tabla[posi] is None:
                self.__tabla[posi] = clave
            else:
                pos = self.secuenciaPrueba(clave, posi)
                if pos is not None:
                    self.__tabla[pos] = clave
                else:
                    print("No hay posiciones vacias o la clave ingresa no es valida, ya que es unica.")

    def buscar (self, clave):
        posi = self.divisiones(clave)
        if self.__tabla[posi] == clave:
            return self.__tabla[posi]
            ##print("La clave a buscar si se encuentra en la tabla")
           ## print(f"La clave se encuentra en la posicion {posi + 1}")
        else:
            posi = self.secuenciaPrueba(clave, posi)
            if posi is not None and self.__tabla[posi] == clave:
                return self.__tabla[posi]
                ##print("La clave ingresad si se encuentra en la tabla")
                ##print(f"La clave se encuentra en la posicion {posi + 1}")
            else:
                return None
                ##print("La clave a buscar no se encuentra en la tabla")
           
            
    def recorrer (self):
        for i in range(self.__M):
            print(self.__tabla[i])


tabla = direccionamientoA(10)

tabla.insertar(15)
tabla.insertar(35)
tabla.insertar(8)
tabla.insertar(5)
tabla.insertar(5)

tabla.recorrer()

tabla.buscar(35)
tabla.buscar(15)
tabla.buscar(99)


