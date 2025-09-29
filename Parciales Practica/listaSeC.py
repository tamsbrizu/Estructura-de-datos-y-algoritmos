import numpy as np

class listaSC:
    __max: int
    __cant: int
    __ul: int
    __elementos: np.array

    def __init__ (self, maxx):
        self.__max = maxx
        self.__cant = 0
        self.__ul = -1
        self.__elementos = np.empty(self.__max, dtype=int)


    def vacia (self):
        return self.__ul == -1
    
    def llena (self):
        return self.__cant == self.__max
    
    def buscar (self, x):
        inicio = 0
        fin = self.__cant -1
        while inicio <= fin:
            medio = (inicio + fin) // 2
            if self.__elementos[medio] == x:
                return medio
            elif self.__elementos[medio] > x:
                inicio = medio + 1
            else:
                fin = medio -1 
        return None
    
    def primer_elemento(self):
        return self.__elementos[0]
    
    def ultimo_elemento(self):
        return self.__elementos[self.__ul]
    
    def siguiente_elemento(self, x):
        p = self.buscar(x)
        if p is not None:
            if p + 1 <= self.__cant:
                return self.__elementos[p+1]
            
    def anterior_elemento(self, x):
        p = self.buscar(x)
        if p is not None:
            if p -1 != -1:
                return self.__elementos[p-1]

    
    def insertar (self, x):
        if not self.llena():

            p = 0
            while p < self.__cant and self.__elementos[p] > x:
                p += 1

            i = self.__cant -1
            while i >= p:
                self.__elementos[i+1] = self.__elementos[i]
                i -= 1
            self.__elementos[p] = x
            self.__cant += 1
            self.__ul += 1

    def suprimir (self, x):
        if not self.vacia():
            p = self.buscar(x)
            if p is not None:
                eliminado = self.__elementos[p]
                i = p
                while i < self.__cant - 1:
                    self.__elementos[i] = self.__elementos[i+1]
                    i += 1
                self.__cant -= 1
                self.__ul -= 1
                return eliminado
            
    def recuperar (self, x):
        p = self.buscar(x)
        if p is not None:
            return self.__elementos[p]

    def recorrer (self):
        for i in range(self.__cant):
            print(self.__elementos[i])



def main():
    lista = listaSC(10)

    print("Insertando elementos en orden...")
    lista.insertar(30)
    lista.insertar(10)
    lista.insertar(20)
    lista.insertar(40)
    lista.insertar(25)

    print("\nElementos después de insertar:")
    lista.recorrer()

    print("\nBuscando elementos:")
    print("Buscar 40 → posición:", lista.buscar(40))
    print("Buscar 15 → posición:", lista.buscar(15))

    print("\nEliminando elementos...")
    lista.suprimir(10)
    lista.suprimir(40)

    print("\nElementos después de eliminar:")
    lista.recorrer()


if __name__ == "__main__":
    main()
