##Se ultiza un ultimo (si es opcional). En buscar primero se debe buscar la posicion y es valida se inserta
##insertar, suprimir, recuperar, buscar, primero, ultimo, siguiente, anterior, recorrer, vacia

class Nodo:
    __elemento: None
    __fila: int
    __columna: int
    __sig: None

    def __init__ (self, elem, f, c):
        self.__elemento = elem
        self.__fila = f
        self.__columna = c
        self.__sig = None

    def obtener_fila (self):
        return self.__fila
    
    def obtener_columna (self):
        return self.__columna

    def obtener_elemento (self):
        return self.__elemento
    
    def obtener_sig (self):
        return self.__sig
    
    def set_elemento (self, valor):
        self.__elemento = valor

    def set_sig (self, valor):
        self.__sig = valor


class le:
    __cant: int
    __filas: int
    __columnas: int
    __cabeza: int

    def __init__ (self, fila, columna):
        self.__cabeza = None
        self.__filas = fila
        self.__columnas = columna
        self.__cant = 0

    def vacia (self):
        return self.__cant == 0
    
    def primero_elemento (self):
        return self.__cabeza
    
    def ultimo_elemento (self):
        aux = self.__cabeza
        while aux.obtener_sig() is not None:
            aux = aux.obtener_sig()
        return aux
    
    def insertar (self, x, f, c):
        nuevo = Nodo(x, f ,c)

        if self.vacia() or x < self.__cabeza.obtener_elemento():
            nuevo.set_sig(self.__cabeza)
            self.__cabeza = nuevo
            self.__cant += 1
                
        elif not self.vacia():

            aux = self.__cabeza
            
            while aux.obtener_sig() is not None and aux.obtener_sig().obtener_fila() < f:
                0
                aux = aux.obtener_sig()

            nuevo.set_sig(aux.obtener_sig())
            aux.set_sig(nuevo)
            self.__cant += 1


    def buscar (self, x):
        i = 0
        ban = False
        aux = self.__cabeza
        while not ban and aux is not None:
            if aux.obtener_elemento() == x:
                ban = True
            else:
                aux = aux.obtener_sig()
                i += 1
        
        if ban:
            return i
        else:
            return -1
    
    def suprimir (self, x):
        if not self.vacia():
           p = self.buscar(x)
           if p == 0:
               eliminado = self.__cabeza.obtener_elemento()
               self.__cabeza = self.__cabeza.obtener_sig()
               self.__cant -= 1
               return eliminado
           else:
                aux = self.__cabeza
                while aux.obtener_sig() is not None:
                    if aux.obtener_sig().obtener_elemento() == x:
                        eliminado = aux.obtener_sig().obtener_elemento()
                        aux.set_sig(aux.obtener_sig().obtener_sig())
                        self.__cant -= 1
                        return eliminado
                    aux = aux.obtener_sig()

        else:
           print("La lista esta vacia.")

    def getFilas (self):
        return self.__filas
    
    def getColumnas (self):
        return self.__columnas
                       

    def recorrer (self):
        aux = self.__cabeza
        while aux is not None:
            print(f"Fila: {aux.obtener_fila()} - Columna: {aux.obtener_columna()} ---> {aux.obtener_elemento()}")
            aux = aux.obtener_sig()

    def buscar_f_c (self, f, c):
        aux = self.__cabeza
        ban = False
        while aux is not None and not ban:
            if aux.obtener_fila() == f and aux.obtener_columna() == c:
                ban = True
                return aux.obtener_elemento()
            else:
                aux = aux.obtener_sig()
        
        if not ban:
            return None
            

    


'''Ejercicio Nº 4: 
Una  matriz  rala  puede  representarse  como  una  Lista  enlazada,  en  la  cual  cada  celda 
contiene el valor del componente, su fila y columna.  
a)  Construir  un  algoritmo  que  realice  la  operación  suma  de  dos  matrices  así 
representadas'''

def suma(m1,m2):
    if m1.getFilas() == m2.getFilas() and m1.getColumnas() == m2.getColumnas():
        matrizSuma = le(m1.getFilas(), m1.getColumnas())

        e1 = m1.primero_elemento()
        e2 = m2.primero_elemento()

        while e1 is not None or e2 is not None:
            if e1 is not None and e2 is not None:
                if e1.obtener_fila() == e2.obtener_fila() and e1.obtener_columna() == e2.obtener_columna():
                    suma = e1.obtener_elemento() + e2.obtener_elemento()
                    matrizSuma.insertar(suma, e1.obtener_fila(), e1.obtener_columna())
                if e1.obtener_fila() != e2.obtener_fila() or e1.obtener_columna() != e2.obtener_columna():
                    if e1.obtener_fila() < e2.obtener_fila():
                        matrizSuma.insertar(e1.obtener_elemento(), e1.obtener_fila(), e1.obtener_columna())
                    elif e2.obtener_fila() < e1.obtener_fila():
                        matrizSuma.insertar(e2.obtener_elemento(),  e2.obtener_fila(), e1.obtener_columna())
                e1 = e1.obtener_sig()
                e2 = e2.obtener_sig()
            elif e2 is None and e1 is not None:
                matrizSuma.insertar(e1.obtener_elemento(),  e1.obtener_fila(), e1.obtener_columna())
                e1 = e1.obtener_sig()
            elif e1 is None and e2 is not None:
                matrizSuma.insertar(e2.obtener_elemento(),  e2.obtener_fila(), e1.obtener_columna())
                e2 = e2.obtener_sig()

        print("\nMostrando matriz de suma.")
        matrizSuma.recorrer()
    else:
        print("El numero de filas y columnas de la primera matriz no es igual al numero de filas y columnas de la segunda matriz.")


   
if __name__ == '__main__':
    m1 = le(2,2)
    m2 = le (2,2)


    print("Insertado elementos...")
    print("\nRecorriendo elementos matriz 1")
    m1.insertar(1,1,1)
    m1.insertar(1,2,1)
    m1.insertar(1,1,2)
    m1.insertar(1,2,2)
    m1.recorrer()

    print("\nInsertando elementos...")
    print("Recorriendo elementos matriz 2")
    m2.insertar(1,1,1)
    m2.recorrer()

    suma(m1,m2)



