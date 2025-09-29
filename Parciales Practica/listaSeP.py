import numpy as np

class listaSP:
    __cant: int
    __ul: int
    __max: int
    __elementos: np.array

    def __init__ (self, maxx):
        self.__max = maxx
        self.__cant = 0
        self.__ul = -1
        self.__elementos = np.empty (self.__max, dtype=int)

    def vacia (self):
        return self.__ul == -1
    
    def llena (self):
        return self.__cant == self.__max
    
    def primer_elemento(self):
        return self.__elementos[0]
    
    def ultimo_elemento(self):
        return self.__elementos[self.__ul]
    
    def siguiente_posicion (self, p):
        if p >= 1 and p <= self.__cant:
            e = self.__elementos[p]
            return e
        
        
    def anterior_posicion (self, p):
        if p >= 1 and p <= self.__cant:
            e = self.__elementos[p-2]
            return e
        
    def buscar (self, p):
        i = 0
        ban = False
        while not ban and i < self.__cant:
            if i == p:
                ban = True
            else:
                i += 1
        
        if ban:
            return self.__elementos[i]
        else:
            return None

    def insertar (self, x, p):
        if p >= 1 and p <= self.__cant + 1:
            if not self.llena():
                i = self.__cant -1
                while i >= p -1:
                    self.__elementos[i+1] = self.__elementos[i]
                    i -= 1
                self.__elementos [p-1] = x
                self.__cant += 1
                self.__ul += 1

    def suprimir (self, p):
        if p >= 1 and p <= self.__cant:
            if not self.vacia():
                eliminado = self.__elementos[p-1]
                i = p -1
                while i < self.__cant -1:
                    self.__elementos[i] = self.__elementos[i+1]
                    i += 1
                self.__cant -= 1
                self.__ul -= 1
                return eliminado
            
    def recuperar (self, p):
        if p >= 1 and p <= self.__cant:
            return self.__elementos[p-1]
        
            
    def recorrer (self):
        for i in range(self.__cant):
            print(self.__elementos[i])


def main():
    # Crear una lista secuencial con capacidad máxima de 5 elementos
    lista = listaSP(5)

    print("¿La lista está vacía?:", lista.vacia())

    # Insertar algunos elementos
    lista.insertar(10, 1)   # Inserta 10 en la posición 1
    lista.insertar(20, 2)   # Inserta 20 en la posición 2
    lista.insertar(30, 3)   # Inserta 30 en la posición 3
    lista.insertar(15, 2)   # Inserta 15 en la posición 2 (desplaza a los demás)

    print("\nElementos después de inserciones:")
    lista.recorrer()

    # Suprimir un elemento
    eliminado = lista.suprimir(3)   # Elimina el elemento en la posición 3
    print(f"\nSe eliminó el elemento: {eliminado}")

    print("\nElementos después de la supresión:")
    lista.recorrer()

    eliminado = lista.suprimir(3)   # Elimina el elemento en la posición 3
    print(f"\nSe eliminó el elemento: {eliminado}")

    print("\nElementos después de la supresión:")
    lista.recorrer()

    print("\n¿La lista está llena?:", lista.llena())

if __name__ == "__main__":
    main()
