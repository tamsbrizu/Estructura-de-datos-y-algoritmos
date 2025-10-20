##Aun no esta terminado. Faltan metodos y verificar que funcionen.

class Nodo:
    __elemento: int
    __der: None
    __izq: None

    def __init__ (self, e):
        self.__elemento = e
        self.__der = None
        self.__izq = None

    def obtener_elemento (self):
        return self.__elemento
    def obtener_izq (self):
        return self.__izq
    def obtener_der (self):
        return self.__der
    
    def set_izq (self, valor):
        self.__izq = valor
    def set_der (self, valor):
        self.__der = valor

##grado en el nodo
    def grado (self):
        g = 0
        if self.__der is not None:
            g += 1
        elif self.__izq is not None:
            g += 1
        return g
    
class arbolbb:
    __raiz: Nodo

    def __init__ (self):
        self.__raiz = None
    
    def insertar (self, subarbol, clave):
        nuevo = Nodo(clave)
        if self.__raiz is None:
            self.__raiz = nuevo
        else:
            if clave < subarbol.obtener_elemento():
                if subarbol.obtener_izq is None:
                    subarbol.set_izq(nuevo)
                else:
                    return self.insertar(subarbol.obtener_izq(), clave)
            else:
                if subarbol.obtener_der() is None:
                    subarbol.set_der(nuevo)
                else:
                    return self.insertar(subarbol.obtener_der(), clave)
    
    def buscar (self, subarbol, clave):
        if subarbol is None:
            print("ERROR. El arbol esta vacio")
        else:
            nodo = None
            if clave == subarbol.obtener_elemento():
                nodo = subarbol
            elif clave < subarbol.obtener_elemento():
                self.buscar(subarbol.obtener_izq(), clave)
            else:
                self.buscar(subarbol.obtener_der(), clave)
            return nodo

    def suprimir (self, subarbol, clave):
        if subarbol is None:
            print("ERROR. El arbol esta vacio")
        else:
            if clave == subarbol.obtener_elemento():
                g = subarbol.grado()
                if g == 0:
                    return None
                elif g == 1:
                    if subarbol.obtener_izq() is not None:
                        return subarbol.obtener_izq()
                    else:
                        return subarbol.obtener_der()
                else:
                    max_izq = subarbol.obtener_izq()
                    while max_izq.obtener_derecho() is not None:
                        max_izq = subarbol.obtener_der()
                    subarbol.set_valor(max_izq.obtener_elemento())
                    subarbol.set_izq(self.suprimir(subarbol.obtener_izquierdo), max_izq.obtener_elemento())
            elif clave < subarbol.obtener_elemento():
                subarbol.set_izq(self.suprimir(subarbol.obtener_izq(), clave))
            else:
                subarbol.set_der(self.suprimir(subarbol.obtener_der(), clave))

    def inOrden (self, subarbol):
        if subarbol is not None:
            self.inOrden(subarbol.obtener_izq())
            print(subarbol.obtener_elemento())
            self.inOrden(subarbol.obtener_der())
    
    def preOrden (self, subarbol):
        if subarbol is not None:
            print(subarbol.obtener_elemento())
            self.preOrden(subarbol.obtener_izq())
            self.preOrden(subarbol.obtener_der())

    def postOrden (self, subarbol):
            if subarbol is not None:
                self.postOrden(subarbol.obtener_izq())
                self.postOrden(subarbol.obtener_der())
                print(subarbol.obtener_elemento())

    def padre (self, subarbol, hijo, padre):
        pad= self.buscar(subarbol, padre)
        if pad is not None:
            izq = pad.obtener_izq()
            der = pad.obtener_der()
            if izq is not None:
                if hijo == izq.obtener_elemento():
                    print(f"El nodo hijo {hijo} si tiene como padre a {padre}")
            elif der is not None:
                if hijo == der.obtener_elemento():
                    print(f"El nodo hijo {hijo} si tiene como padre a {padre}")
            else:
                print(F"El nodo hijo {hijo} no tiene como padre al nodo {padre}")

    def hijo (self, subarbol, hijo, padre):
        pad= self.buscar(subarbol, padre)
        if pad is not None:
            izq = pad.obtener_izq()
            der = pad.obtener_der()
            if izq is not None:
                if hijo == izq.obtener_elemento():
                    print(f"El nodo padre {padre} si tiene como hijo al nodo {hijo}")
            elif der is not None:
                if hijo == der.obtener_elemento():
                    print(f"El nodo padre {padre} si tiene como hijo al nodo {hijo}")
            else:
                print(F"El nodo padre {padre} no tiene como hijo al nodo {hijo}")

    def hermano (self, subarbol, clave, padre = None):
        if clave == subarbol.obtener_elemento():
            if padre is None:
                print(f"El nodo {clave} es la raiz. No tiene hermanos")
            else:
                der = padre.obtener_der()
                izq = padre.obtener_izq()
                if der.obtener_elemento() != clave and der is not None:
                    print(f"El nodo {clave} tiene como hijo al nodo {der.obtener_elemento()}")
                else:
                    if izq is not None and izq.obtener_elemento() != clave:
                        print(f"El nodo {clave} tiene como hijo al nodo {izq.obtener_elemento()}")
