class Nodo:
    __nombre: str
    __sig: None

    def __init__ (self, n):
        self.__nombre = n
        self.__sig = None

    def obtener_nombre(self):
        return self.__nombre
    
    def obtener_sig (self):
        return self.__sig
    
    def set_sig (self, valor):
        self.__sig = valor
    
    def mostrarDatos (self):
        return (f"Nombre de la cancion: {self.__nombre}")
    
class le:
    ___cant: Nodo
    __cabeza: int

    def __init__ (self):
        self.__cabeza = None
        self.__cant = 0


    def insertarFinal (self, x):
        nuevo = Nodo(x)
        nuevo.set_sig(None)
        if self.__cabeza == None:
            self.__cabeza = nuevo
        else:
            aux = self.__cabeza
            while aux.obtener_sig() is not None:
                aux = aux.obtener_sig()
            aux.set_sig(nuevo)
            self.__cant += 1
        


    def insertar(self, x, p):
        if p>=1 and p <= self.__cant + 1:
            if p == 1:
                nuevo = Nodo(x)
                nuevo.set_sig(self.__cabeza)
                self.__cabeza = nuevo
                self.__cant += 1

            else:
                nuevo = Nodo(x)
                aux = self.__cabeza
                i = 1
                while i < p -1 and aux is not None:
                    aux = aux.obtener_sig()
                    i += 1
                
                nuevo.set_sig(aux.obtener_sig())
                aux.set_sig(nuevo)

                self.__cant += 1

        else:
            print("Posicion invalida para insertar.")

    def suprimir (self, p):
        if p >= 1 and p <= self.__cant:
            aux = self.__cabeza
            i = 0
            if p == 1:
                x = self.__cabeza.obtener_nombre()
                self.__cabeza = self.__cabeza.obtener_sig()
            else:
                aux = self.__cabeza
                i = 1

                while i < p - 2 and aux is not None:
                    aux = aux.obtener_sig()
                    i += 1
                

                x = aux.obtener_sig().obtener_nombre()
                if x is not None:
                    aux.set_sig(aux.obtener_sig().obtener_sig())

            self.__cant -= 1
            return x
        else:
            print("Posicion invalida para suprimir.")

    def recuperar (self, p):
        aux = self.__cabeza
        i = 1
        while i <= p -1:
            aux = aux.obtener_sig()
            i += 1
        return aux.obtener_nombre()

    def recorrer (self):
        aux = self.__cabeza
        while aux is not None:
            print(aux.obtener_nombre())
            aux = aux.obtener_sig()

    def buscar (self, x):
        i = 0
        ban = False
        aux = self.__cabeza
        while not ban and aux is not None:
            if aux.obtener_nombre() == x:
                ban = True
            else:
                i += 1
                aux = aux.obtener_sig()

        if ban:
            return i
        else:
            return -1


if __name__ == "__main__":

    canciones = le()

    canciones.insertar("Seven", 1)
    canciones.insertar("Mine", 2)
    canciones.insertar("Next to you", 3)

    print("\nMostrando canciones")
    canciones.recorrer()

    print("\nInsertar cancion al final...")
    canciones.insertarFinal("Love & Peach")
    canciones.recorrer()

    print("\nInsertando en la posicion 1")
    canciones.insertar("Who", 1)
    canciones.recorrer()

    print("\nEliminando canciones 1 y 3")
    canciones.suprimir(1)
    canciones.recorrer()
    print("\n")
    canciones.suprimir(2)
    canciones.recorrer()

    print("\nObtener el nombre de la cancion en la posicion 2")
    print(canciones.recuperar(2))

    print("\nMostrar la posicion en la que se encuentra la cancion 'Love & Peach'")
    print(canciones.buscar("Love & Peach"))

    print("\nMostrar la lista de reproducion con canciones")
    canciones.recorrer()
    

    
'''Al parcial va pila, cola y lista. Implementaciones vistas: pila (secuencial y encadenada)
cola(secuencial, encadenada, circular) y lista (sec y encadenada por posicion o por contenido y lista con cursores)
Analizamos las principales operaciones
para pila, cola y lista:
insertar 
eliminar
buscar (pila y el cola no esta pero se cambia por recorrer)
recorrer

pilaS = O(1), O(1), O(N)
pilaE = O(1), O(1), O(N)

(!!!!) HACER COLA SECUENCIAL (NO ESTA EN LA TEORIA BUSCAR)

colaS = O(N);O(1), O(1);O(N), O(N)
colaE = O(1), O(1), O(N)
colaC = O(1), O(1), O(N)

listaSPP = O(N) (POR EL SHIPTEO), O(N), O(N), O(N)
listaSPO = O(N), O(N), O(LG(N)), O(N)

LISTAEPP = O(N), O(N), O(N), O(N)
LISTAEPO = O(N), O(N), O(N), O(N)

CURSOR = O(N), O(N), O(N), O(N)

Si la busqueda es binaria LG(N)

al parcial, tipo de dato abstrato, que nos implementen algun metodo (basico o no), simulacion por cola
o algun ejercio donde utilicemos una de las estructuras


'''