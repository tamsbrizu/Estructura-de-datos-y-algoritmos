from CeldaEncadenada import Celda

class pila:
    __cant: int
    __tope: int

    def __init__ (self, cant = 0):
        self.__cant = cant
        self.__tope = None

    def vacia (self):
        return (self.__cant == 0)
    
    def insertar (self, x):
        ps1 = Celda()
        ps1.cargar_item(x)
        ps1.cargar_sig(self.__tope)
        self.__tope = ps1
        self.__cant += 1
        return ps1.obtener_item()
    
    def suprimir (self):
        if self.vacia():
            print ("Pila Vacia")
            return 0
        else:
            aux = self.__tope
            x = aux.obtener_item()
            self.__tope = aux.obtener_sig()
            self.__cant -= 1
            return x
        

    def mostrar (self):
        aux = self.__tope
        while aux is not None:
            print(aux.obtener_item())
            aux = aux.obtener_sig()

    def invertir (self):
        aux = self.__tope
        prev = None
        while aux is not None:
            sig = aux.obtener_sig()
            aux.cargar_sig(prev)
            prev = aux
            aux = sig
        self.__tope = prev


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
    P = pila()


    print("2 peldaños")
    P.escaleras(2)
    P.mostrar()
    
    print("4 peldaños")
    P.escaleras(4)
    P.mostrar()
