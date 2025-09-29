class Nodo:
    __elemento: str
    __cont: int
    __izq: None
    __der: None

    def __init__(self, e, c):
        self.__elemento = e
        self.__cont = c
        self.__izq = None
        self.__der = None

    def obtener_elemento(self):
        return self.__elemento
    
    def obtener_contador (self):
        return self.__cont
    
    def set_cont (self, valor):
        self.__cont = valor
    
    def obtener_izquierdo (self):
        return self.__izq
    
    def obtener_derecho (self):
        return self.__der

    def set_izq (self, valor):
        self.__izq = valor

    def set_der (self, valor):
        self.__der = valor

    def __lt__ (self, valor):
        return self.__cont < valor.obtener_cont()

class huffman:
    __cab: Nodo

    def __init__(self):
        self.__cab = None

    def insertar(self, texto):
        letras = []
        apariciones = []
        for c in texto:
            if c in letras:
                idx = letras.index(c)
                apariciones[idx] += 1
            else:
                letras.append(c)
                apariciones.append(1)

        
        nodosLista = []
        for i in range(len(letras)):
            nodosLista.append(Nodo(letras[i], apariciones[i]))

        while len(nodosLista) > 1:
            nodosLista.sort(key=lambda x: x.obtener_contador())

            nodo1 = nodosLista.pop(0)
            nodo2 = nodosLista.pop(0)

            nuevo = Nodo(nodo1.obtener_elemento() + nodo2.obtener_elemento(), nodo1.obtener_contador() + nodo2.obtener_contador())
            nuevo.set_izq(nodo1)
            nuevo.set_der(nodo2)
        
            nodosLista.append(nuevo)

        self.__cab = nodosLista[0]

    def mostrar_codigos(self):
        self.diccionarioDeCodigos()


    def diccionarioDeCodigos (self, nodo=None,  c = ""):
        if nodo is None:
            nodo = self.__cab
        
        if nodo is None:
            return None

        if nodo.obtener_elemento() is not None and len(nodo.obtener_elemento()) == 1:
            print(f"Letra: {nodo.obtener_elemento()} -> Camino: {c or '0'}")
        
        if nodo.obtener_izquierdo() is not None:
            self.diccionarioDeCodigos(nodo.obtener_izquierdo(), c + "0")
        if nodo.obtener_derecho() is not None:
            self.diccionarioDeCodigos(nodo.obtener_derecho(), c + "1")
        
        

h = huffman()
t = "banana"
h.insertar(t)
h.mostrar_codigos()
print(f"Texto decodificado: {t}")
        



        



        
            
            

