import numpy as np

class ls:
    __cant: int
    __ul: int
    __elementos: np.array

    def __init__ (self, maxx= 1000):
        self.__cant =  0
        self.__ul = -1
        self.__elementos = np.empty(maxx, dtype=int)

    def vacia (self):
        return self.__cant == 0
    
    def llena (self):
        return self.__cant == len (self.__elementos)

    def primer_elemento (self):
        if not self.vacia():
            return self.__elementos[0]
    
    def ultimo_elemento (self):
        if not self.vacia():
            return self.__elementos[self.__ul]
    
    def insertar (self, x):
        if not self.llena():

            p = 0

            # Se busca la posicion en donde se deberia insertar
            while p < self.__cant and self.__elementos[p] < x:
                p += 1

            i = self.__cant -1 # Se empieza desde atras (ultimo elemento)
            while i >= p:
                self.__elementos[i+1] = self.__elementos[i] # Se corren los elementos hacia la derecha
                i -= 1
            
            self.__elementos[p] = x
            self.__cant += 1
            self.__ul = self.__cant -1
        else:
            print("La lista esta llena. No se pueden insertar elementos.")

    def buscar(self, x):
        inicio = 0
        fin = self.__cant - 1
        while inicio <= fin:
            medio = (inicio + fin) // 2
            if self.__elementos[medio] == x:
                return medio
            elif self.__elementos[medio] < x:
                inicio = medio + 1
            else:
                fin = medio - 1
        return None

        
    def suprimir (self, x):
        if not self.vacia():
            p = self.buscar(x)
            #Se busca la posicion
            if p is not None:
                eliminado = self.__elementos[p]

                i = p

                while i < self.__cant -1:
                    # mientras la posicion sea menor a la cantidad
                    self.__elementos[i] = self.__elementos[i+1] # Se corren los elementos a la izquierda
                    i += 1
                
                self.__cant -= 1
                self.__ul = self.__cant - 1
                return eliminado
            else:
                print("Elemento no encontrado.")
        else:
            print("La lista esta vacia. No se puede suprimir elementos.")

    def siguiente_posicion (self, x):
        p = self.buscar(x)
        if p is not None and p <self.__cant -1:
            ele = self.__elementos[p+1]
            return ele
        else:
            print("Elemento no encontrado")

    def anterior_posicion (self, x):
        p = self.buscar(x)
        if p is not None and p > 0:
            ele = self.__elementos[p-1]
            return ele
        else:
            print("Elemento no encontrado")


    def recuperar (self, p):
        if p >= 0 and p > 0:
            ele = self.__elementos[p-1]
            return ele
        else:
            print("Posicion invalida.")


    def recorrer (self):
        for i in range(self.__cant):
            print(self.__elementos[i])

# --- Ejemplo de uso ---
if __name__ == '__main__':
    LS = ls()

    LS.insertar(20)
    LS.insertar(10)

    LS.recorrer()

    print("\nSuprimiendo elemento 20")
    LS.suprimir(20)
    LS.recorrer()

    print("\nInserción del 30")
    LS.insertar(30)
    LS.recorrer()

    print("\nPrimer elemento")
    print(LS.primer_elemento())

    print("\nÚltimo elemento")
    print(LS.ultimo_elemento())

    print("\nSiguiente elemento del 10")
    print(LS.siguiente_posicion(10))

    print("\nAnterior elemento del 30")
    print(LS.anterior_posicion(30))

    print("\nRecuperar en la posición 1")
    print(LS.recuperar(1))