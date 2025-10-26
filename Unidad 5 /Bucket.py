import numpy as np
import math

class bucket:
    __tam: int
    __cont: int
    __buck: np.array

    def __init__(self, t):
        self.__tam = t
        self.__cont = 0
        self.__buck = np.empty(self.__tam, dtype=object)

    def bucket_lleno (self):
        return self.__cont == self.__tam

    def bucket_insertar (self, clave):
        self.__buck[self.__cont] = clave
        self.__cont += 1
    
    def bucket_buscar (self, clave):
        i = 0
        ban = False
        elemento_encontrado = None
        while not ban and i < self.__cont:
            if self.__buck[i] == clave:
                ban = True
                elemento_encontrado = self.__buck[i]
            else:
                i += 1
        return elemento_encontrado
    
    def bucket_recorrer(self):
        for i in range(self.__cont):
            print(f"Posicion: {i} - Elemento: {self.__buck[i]}")


class hash_buckets:
    __tabla: np.array
    __M: int
    __A: int
    __cantMax: int
    
    def __init__ (self, m, cantMColisiones):
        self.__cantMax = cantMColisiones
        self.__A = round(m/cantMColisiones)
        self.__M = round(self.__A * 1.2)
        self.__tabla = np.empty (self.primo(self.__M), dtype=object)
        

    def inicializar_tablas (self):
        for i in range(self.__M):
            self.__tabla[i] = bucket(self.__cantMax)
        
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
        return clave % self.__A
    
    def insertar (self, clave):
        pos = self.divisiones(clave)
        if not self.__tabla[pos].bucket_lleno():
            self.__tabla[pos].bucket_insertar(clave)
        else:
            pos = self.__A
            while pos < self.__M and self.__tabla[pos].bucket_lleno():
                pos += 1

            if pos < self.__M:
                self.__tabla[pos].bucket_insertar(clave)
            else:
                print(f"No se puede insertar {clave}: todos los buckets están llenos")

    def buscar (self, clave):
        pos = self.divisiones(clave)
        resultado = self.__tabla[pos].bucket_buscar(clave)
        if resultado is not None:
            return resultado
        else:
            pos = self.__A
            while pos < self.__M and self.__tabla[pos] is not None:
                resultado = self.__tabla[pos].bucket_buscar(clave)
                if resultado is not None:
                    return resultado
                pos += 1
            return None
            

    def recorrer (self):
        for i in range(self.__M):
            print(f"Lugar/posicion en la tabla: {i}")
            self.__tabla[i].bucket_recorrer()

def main():
    # Crear la tabla hash con 20 posiciones y buckets de tamaño 3
    tabla = hash_buckets(20, 3)
    tabla.inicializar_tablas()

    # Insertar elementos
    elementos = [10, 30, 50, 70, 15, 25, 35, 45, 55]
    print("Insertando elementos:")
    for e in elementos:
        print(f"Inserto: {e}")
        tabla.insertar(e)

    print("\nRecorrido de la tabla hash:")
    tabla.recorrer()  # Imprime todos los elementos en los buckets

    # Buscar elementos existentes
    busquedas = [30, 55, 99]  # 99 no existe
    print("\nResultados de búsqueda:")
    for b in busquedas:
        res = tabla.buscar(b)
        if res is not None:
            print(f"Elemento {b} encontrado en la tabla.")
        else:
            print(f"Elemento {b} NO encontrado en la tabla.")

if __name__ == "__main__":
    main()


