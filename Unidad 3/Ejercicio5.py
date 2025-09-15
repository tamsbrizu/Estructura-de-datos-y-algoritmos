class Nodo:
    __coeficiente: None
    __exponente: None
    __sig: None

    def __init__ (self, c, e):
        self.__coeficiente = c
        self.__exponente = e
        self.__sig = None

    def obtener_coeficiente (self):
        return self.__coeficiente
    
    def obtener_exponente(self):
        return self.__exponente
    
    def obtener_sig (self):
        return self.__sig
    

    def set_sig (self, valor):
        self.__sig = valor


class le:
    __cant: int
    __cabeza: int

    def __init__ (self):
        self.__cabeza = None
        self.__cant = 0

    def vacia (self):
        return self.__cant == 0
    
    
    def insertar (self, c, e):
        nuevo = Nodo(c, e)

        if self.vacia() or e < self.__cabeza.obtener_exponente():
            nuevo.set_sig(self.__cabeza)
            self.__cabeza = nuevo
            self.__cant += 1
                
        elif not self.vacia():

            aux = self.__cabeza
            
            while aux.obtener_sig() is not None and  aux.obtener_sig().obtener_exponente() < e:
                aux = aux.obtener_sig()

            nuevo.set_sig(aux.obtener_sig())
            aux.set_sig(nuevo)
            self.__cant += 1


    def recorrer (self):
        aux = self.__cabeza
        while aux is not None:
            print(f"Coeficiente: {aux.obtener_coeficiente()} - Exponente: {aux.obtener_exponente()}")
            aux = aux.obtener_sig()

    def obtener_cant(self):
        return self.__cant
    
    def primero (self):
        return self.__cabeza
    
    
    def suma (self, poli2):

        p3Suma = le()

        p2 = poli2.primero()

        p1 = self.__cabeza

        while p1 is not None or p2 is not None:
            if p1 is not None and p2 is not None:
                if p2.obtener_exponente() == p1.obtener_exponente():
                    suma = p1.obtener_coeficiente() + p2.obtener_coeficiente()
                    p3Suma.insertar(suma, p1.obtener_exponente())
                elif p1.obtener_exponente() > p2.obtener_exponente():
                    p3Suma.insertar(p1.obtener_coeficiente(), p1.obtener_exponente())
                elif p2.obtener_exponente()  >  p1.obtener_exponente():
                    p3Suma.insertar(p2.obtener_coeficiente(), p2.obtener_exponente())
                
                p1 = p1.obtener_sig()
                p2 = p2.obtener_sig()

            elif p1 is not None and p2 is None:
                p3Suma.insertar(p1.obtener_coeficiente(), p1.obtener_exponente())
                p1 = p1.obtener_sig()

            elif p2 is not None and p1 is None:
                p3Suma.insertar(p2.obtener_coeficiente(), p2.obtener_exponente())
                p2 = p2.obtener_sig()

        print("\nMostrando polinomio de suma....")
        p3Suma.recorrer()

    def resta (self, poli2):

        p3Resta = le()

        p2 = poli2.primero()

        p1 = self.__cabeza

        while p1 is not None or p2 is not None:
            if p1 is not None and p2 is not None:
                if p2.obtener_exponente() == p1.obtener_exponente():
                    resta = p1.obtener_coeficiente() - p2.obtener_coeficiente()
                    p3Resta.insertar(resta, p1.obtener_exponente())
                elif p1.obtener_exponente() > p2.obtener_exponente():
                    p3Resta.insertar(p1.obtener_coeficiente(), p1.obtener_exponente())
                elif p2.obtener_exponente()  >  p1.obtener_exponente():
                    p3Resta.insertar(p2.obtener_coeficiente(), p2.obtener_exponente())
                
                p1 = p1.obtener_sig()
                p2 = p2.obtener_sig()

            elif p1 is not None and p2 is None:
                p3Resta.insertar(p1.obtener_coeficiente(), p1.obtener_exponente())
                p1 = p1.obtener_sig()

            elif p2 is not None and p1 is None:
                p3Resta.insertar(p2.obtener_coeficiente(), p2.obtener_exponente())
                p2 = p2.obtener_sig()

        print("\nMostrando polinomio de resta....")
        p3Resta.recorrer()

    def escalar (self, n):

        p3Escalar = le()

        aux = self.__cabeza
        while aux is not None:
            e = aux.obtener_coeficiente() * n
            p3Escalar.insertar(e, aux.obtener_exponente())
            aux = aux.obtener_sig()

        print("\nMostrando polinomio escalar...")
        p3Escalar.recorrer()



'''Ejercicio Nº 5:  
Un polinomio puede implementarse como una Lista, en la cual cada celda representa el 
término de ese polinomio (coeficiente y exponente).  
 
Diseñar el TAD Polinomio teniendo en cuenta las siguientes operaciones más comunes:  
_ Suma de polinomios  
_ Resta de polinomios  
_ Multiplicación de un escalar por un polinomio.'''


'''Complejidad del algoritmo O(N+M)'''


if __name__ == '__main__':

    P1 = le()
    P2 = le()

    print("Insertando elementos...")
    P1.insertar(3, 4)
    P1.insertar(5,2)
    P1.insertar(4,6)

    print("\nRecorriendo lista")
    P1.recorrer()

    print("Insertando elementos...")
    P2.insertar(6, 4)
    P2.insertar(2,2)

    print("\nRecorriendo lista")
    P2.recorrer()

    P1.suma(P2)

    P1.resta(P2)

    P1.escalar(4)
