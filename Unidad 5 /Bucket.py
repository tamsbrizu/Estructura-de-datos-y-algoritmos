##Faltan arreglos. Aun no terminado


import numpy as np

class bucket:
    __tam: int
    __cont: int
    __buck: np.array

    def __init__(self, t):
        self.__tam = t
        self.__cont = 0
        self.__buck = np.empty(self.__tam, dtype=object)

    def bucket_insertar (self, clave):
        if self.__cont < self.__tam:
            ### tambien puede ser if len(self.__buck) <= self.__tam:
            self.__buck[self.__cont] = clave
            self.__cont += 1
            return True
        else:
            return False
    
    def bucket_buscar (self, clave):
        i = 0
        ban = False
        elemento_encontrado = None
        while not ban and i <= self.__cont:
            if self.__buck[i] == clave:
                ban = True
                elemento_encontrado = self.__buck[i]
            else:
                i += 1
        return elemento_encontrado
    
    def bucket_recorrer (self):
        for i in range (self.__tam):
            print(self.__buck[i])

class hash_buckets:
    __tabla: np.array
    __tablaOverflow: np.array
    __M: int
    __MOverflow: int
    __cantMax: int
    
    def __init__ (self, m, cantMColisiones):
        self.__cantMax = cantMColisiones
        self.__M = self.primo(int(m/cantMColisiones))
        self.__MOverflow = self.primo(int(self.__M * 0.2))
        self.__tabla = np.empty(self.__M, dtype=bucket)
        self.__tablaOverflow = np.empty(self.__MOverflow, dtype=bucket)

    def inicializar_tablas (self):
        for i in range(self.__M):
            self.__tabla[i] = bucket(self.__cantMax)
        for i in range(self.__MOverflow):
            self.__tablaOverflow[i] = bucket(self.__cantMax)
        
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
    
    def insertar (self, clave):
        pos = self.divisiones(clave)
        resultado = self.__tabla[pos].bucket_insertar(clave)
        if resultado:
            print(f"La clave {clave} se encuentra en la tabla.")
        else:
            ban = False
            while not ban:
                for i in range(self.__MOverflow):
                    if self.__tablaOverflow[i].bucket_insertar(clave):
                        ban= True


    def buscar (self, clave):
        pos = self.divisiones(clave)
        resultado = self.__tabla[pos].bucket_buscar(clave)
        if resultado is not None:
            print(f"La clave {resultado} se encuentra la tabla en la posicion {pos}")
        else:
            for i in range(self.__MOverflow):
                resultado = self.__tablaOverflow[i].bucket_buscar(clave)
                if resultado is not None:
                    print(f"La clave {resultado} se encuentra la tabla en la posicion {pos}")

    def recorrer (self):
        for i in range(self.__M):
            print(self.__tabla[i].bucket_recorrer())
        print("Tabla de overflow")
        for i in range(self.__MOverflow):
            print(self.__tablaOverflow[i].bucket_recorrer())

tabla = hash_buckets(20, 3)
tabla.inicializar_tablas()

tabla.insertar(10)
tabla.insertar(30)
tabla.insertar(50)
tabla.insertar(70)

tabla.recorrer()

tabla.buscar(30)
tabla.buscar(99)

