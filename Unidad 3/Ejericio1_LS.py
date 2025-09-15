import numpy as np

class ls:
    __cant: int
    __ul: int
    __elementos: np.array

    def __init__(self, maxx=100):
        self.__cant = 0
        self.__ul = -1
        self.__elementos = np.empty(maxx, dtype=int)


    def vacia (self):
        return self.__cant == 0
    
    def llena (self):
        return self.__cant == len(self.__elementos)

    def primer_elemento (self):
        if not self.vacia():
            return self.__elementos[0]
        else:
            print("La lista esta vacia")
    
    def ultimo_elemento (self):
        if not self.vacia():
            return self.__elementos[self.__ul]
        else:
            print("La lista esta vacia")


    # Siguiente posicicon regresa un elemetno
    '''def siguiente_posicion (self, p):
        if p >= 1 and p <= self.__cant:
            if p + 1 <= self.__cant:
                x = self.__elementos[p]
            return x
        else:
            print("Posicion invalida para obtener siguiente")'''
    
    def siguiente_posicion (self, p):
        if p >= 1 and p <= self.__cant:
            if p + 1 <= self.__cant:
                p = p +1
            return p
        else:
            print("Posicion invalida para obtener siguiente")

    
    def anterior_posicion (self, p):
        if p >= 1 and p <= self.__cant:
            if p - 1 >= 0:
                p = p -1
            return p
        else:
            print("Posicion invalida para obtener anterior")
    


    # Anterior posicion regresa un elemento
    '''def anterior_posicion (self, p):
        if p >= 1 and p <= self.__cant:
            if p - 2 >= 0:
                x = self.__elementos[p-2]
            return x
        else:
            print("Posicion invalida para obtener anterior")'''
        

    # Insertar con for
    '''def insertar (self, x, p):
        if p >= 1 and p <= self.__cant + 1: ##Se puede insertar en el primero, en el ultimo, o en medio
            if p == 1:
                self.__elementos[p-1] = x
                self.__cant += 1
                self.__ul = self.__cant -1
            else:
                for i in range(self.__cant, p-1, -1): ##Inicio, fin, paso. Va restando -1
                    self.__elementos[i] = self.__elementos[i-1] ##Signfica que lo que esta en la posicion i se va a encontrar en la posicion i-1

                self.__elementos[p-1] = x
                self.__cant += 1
                self.__ul = self.__cant - 1
        else:
            print("Posicion no valida")''' 
    
    def insertar (self, x, p):
        if p >= 1 and p <= self.__cant+1:

                i = self.__cant-1
                while i >= p-1:
                    # mientras la cantidad sea mayor a la posicion
                    self.__elementos[i+1] = self.__elementos[i] # Se corren los elementos a la derecha
                    i -= 1

                self.__elementos[p-1] = x
                self.__cant += 1
                self.__ul += 1
        else:
            print("Posicion invalida para insertar")
                
    # Suprimir con for
    '''def suprimir (self, p):
        if p >= 1 and p <= self.__cant:
            x = self.__elementos[p-1]

            for i in range(p-1, self.__cant-1, 1):
                self.__elementos[i] = self.__elementos[i+1]
            
            self.__cant -= 1
            self.__ul = self.__cant -1

            return x'''
    
    def suprimir (self, p):
        if p >= 1 and p <= self.__cant:
            eliminado = self.__elementos[p-1]
            i = p-1
            while i < self.__cant-1:
                self.__elementos[i] = self.__elementos[i+1]
                i += 1

            self.__cant -= 1
            self.__ul = self.__cant - 1
            return eliminado
        else:
            print("Posicion invalida para suprimir")
        
    def buscar (self, x):
        ban = False
        i = 0
        while not ban and not self.vacia():
            if self.__elementos[i] == x:
                ban = True
            else:
                i+= 1
        if ban:
            return i
        else:
            return -1
    
    def recuperar (self, p):
        if p >= 1 and p <= self.__cant:
            x = self.__elementos[p-1]
            return x
        else:
            print("Posicion invalida para recuperar.")


    def recorrer (self):
        for i in range(self.__cant):
            print(self.__elementos[i])


if __name__ == '__main__':
    LS = ls()

    LS.insertar(20, 1)
    LS.insertar(10, 2)
    LS.insertar(30, 3)
    LS.recorrer()

    print("\nSuprimiendo elemento 10")
    LS.suprimir(2)
    LS.recorrer()

    print("\nInserción del 40")
    LS.insertar(40, 2)
    LS.recorrer()

    print("\nPrimer elemento")
    print(LS.primer_elemento())

    print("\nÚltimo elemento")
    print(LS.ultimo_elemento())

    print("\nSiguiente elemento del 1")
    print(LS.siguiente_posicion(1))

    print("\nAnterior elemento del 2")
    print(LS.anterior_posicion(2))

    print("\nRecuperar en la posición 2")
    print(LS.recuperar(2))