##Pila Secuencial
import numpy as np

class pila:
    __items: np.array
    __cant: int
    __tope: int

    def __init__ (self, cantx, tope = -1):
        self.__cant = cantx
        self.__tope = tope
        self.__items = np.zeros(self.__cant, dtype=object)

    def vacia (self):
        return self.__tope == -1

    def insertar (self, x):
        if self.__tope < (self.__cant -1):
            self.__tope += 1
            self.__items[self.__tope] = x
            return x
        else:
            return 0
        
    def suprimir (self):
        if self.vacia():
            print ("Pila Vacia")
            return 0
        else:
            x = self.__items[self.__tope]
            self.__tope -= 1
            return x
    
    def mostrar (self):
        for i in range (self.__tope, -1, -1):
            print(self.__items[i])


    def inverso (self):
        inicio = 0
        fin = self.__tope
        while inicio < fin:
            aux = self.__items[inicio]
            self.__items[inicio] = self.__items[fin]
            self.__items[fin] = aux
            inicio += 1
            fin -= 1

    '''def escaleras(self, n):
        # Cada elemento en la pila es una tupla: (restante, camino)
        self.__tope = -1  # vaciar la pila antes de empezar
        self.insertar((n, ""))  # iniciamos con n pasos y camino vacío

        soluciones = []

        while not self.vacia():
            restante, camino = self.suprimir()  # obtenemos el tope

            if restante == 0:
                soluciones.append(camino)  # llegamos al destino
            else:
                if restante >= 1:
                    self.insertar((restante-1, camino + "1"))
                if restante >= 2:
                    self.insertar((restante-2, camino + "2"))

        # mostrar todas las soluciones
        print(f"Soluciones para {n} escalones:")
        for s in soluciones:
            print(s)'''
        
    def escaleras(self, n):
        self.insertar((n, ""))

        while not self.vacia():
            n, sol = self.suprimir()

            if n == 0:
                print("Camino encontrado:", sol)
            if n >= 1:
                self.insertar((n-1, sol + "1"))
            if n >= 2:
                self.insertar((n-2, sol + "2"))



if __name__ == '__main__':
    P = pila(10000)


    print("8 peldaños")
    P.escaleras(8)
    P.mostrar()
    
    print("3 peldaños")
    P.escaleras(3)
    P.mostrar()
