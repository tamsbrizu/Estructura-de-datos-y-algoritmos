import numpy as np

class Nodo:
    __elemento: None
    __sig: None

    def __init__ (self, e):
        self.__elemento = e
        self.__sig = None

    def obtener_elemento (self):
        return self.__elemento
    
    def obtener_sig (self):
        return self.__sig
    
    def set_sig (self, valor):
        self.__sig = valor

class encadenamiento:
    __M: int
    __tabla: np.array
    __colisiones: np.array ##Arreglo de colsiones de contadores para llevar la cantidad de colisiones que tiene cada posicion
    __tamC: int ## Cantidad de colisiones maximas que puede tener cada posicion en la tabla

    def __init__ (self, m):
        self.__tamC = 4
        self.__M = self.primo(int(m/self.__tamC))
        self.__tabla = np.empty (self.__M, dtype=object)
        self.__colisiones = np.zeros(self.__M, dtype=int)

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


## Metodos de transformacion
    def divisiones (self, clave):
        return clave % self.__M
    
## Operaciones abstractas. Metodo de transformacion: divisiones

    def insertar (self, clave):
        posi = self.divisiones(clave)
        nuevo = Nodo(clave)
        if self.__tabla[posi] is None:
            self.__tabla[posi] = nuevo
        else:
            if self.__colisiones[posi] < self.__tamC:
            ## Forma constante de insercion, cada vez que va ingresando una nueva clave, se convierte en la cabeza del arreglo y apunta al que estaba antes, y el primero
            ## que se inserto se convierte en el ultimo nodo
                nuevo.set_sig(self.__tabla[posi])
                self.__tabla[posi] = nuevo
                self.__colisiones[posi] += 1
            else:
                print("Colision maxima alcanzada.")

    def buscar (self, clave):
        posi = self.divisiones(clave)
        nodo_inicio = self.__tabla[posi]
        ban = False
        nodo_buscado = None
        while not ban and nodo_inicio is not None:
            if nodo_inicio.obtener_elemento() == clave:
                ban = True
                nodo_buscado = nodo_inicio.obtener_elemento()
            else:
                nodo_inicio = nodo_inicio.obtener_sig()
        return nodo_buscado

def main():
    # Crear la tabla hash
    tabla = encadenamiento(m=10)  # tamaño pequeño para probar colisiones

    # Claves a insertar
    claves = [1234, 2345, 3456, 4567, 5678]

    print("=== Inserción de claves ===")
    for clave in claves:
        print(f"Insertando {clave}...")
        tabla.insertar(clave)

    # Mostrar la tabla
    print("\n=== Recorrido de la tabla ===")
    for i in range(tabla._encadenamiento__M):  # accedemos a __M con name mangling
        aux = tabla._encadenamiento__tabla[i]
        lista = []
        while aux is not None:
            lista.append(aux.obtener_elemento())
            aux = aux.obtener_sig()
        print(f"{i}: {lista}")

    # Buscar algunas claves
    print("\n=== Búsqueda de claves ===")
    busquedas = [2345, 5678, 9999]
    for clave in busquedas:
        resultado = tabla.buscar(clave)
        if resultado != None:
            print(f"Clave {clave} encontrada")
        else:
            print(f"Clave {clave} NO encontrada")

if __name__ == "__main__":
    main()


