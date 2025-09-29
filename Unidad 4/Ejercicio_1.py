'''Ejercicio Nº1: Defina el objeto de datos árbol binario de búsqueda, e implemente todos los 
métodos vistos en teoría.'''

class Nodo:
    __elemento:None
    __izq: None
    __der: None

    def __init__ (self, ele):
        self.__elemento = ele
        self.__izq = None
        self.__der = None

    def obtener_elemento(self):
        return self.__elemento
    
    def obtener_izquierdo (self):
        return self.__izq
    
    def obtener_derecho (self):
        return self.__der

    def set_izq (self, valor):
        self.__izq = valor

    def set_der (self, valor):
        self.__der = valor

    def grado (self):
        G = None
        if self.__izq is None and self.__der is None:
            G = 0
        elif self.__izq is not None and self.__der is not None:
            G = 2
        elif self.__izq is None and self.__der is not None:
            G = 1
        else:
            G = 1
        return G



class abb:
    __raiz: Nodo

    def __init__ (self):
        self.__raiz = None

    def obtener_raiz (self):
        return self.__raiz
    
    def insertar (self, subarbol, clave):
        nuevo = Nodo(clave)
        if self.__raiz is None:
            self.__raiz = nuevo
        else:
            if clave < subarbol.obtener_elemento():
                if subarbol.obtener_izquierdo() is None:
                    subarbol.set_izq(nuevo)
                else:
                    self.insertar(subarbol.obtener_izquierdo(), clave)
            elif clave > subarbol.obtener_elemento():
                if subarbol.obtener_derecho() is None:
                    subarbol.set_der (nuevo)
                else:
                    self.insertar(subarbol.obtener_derecho(), clave)

    def suprimir (self, subarbol, clave):
        if subarbol is None:
            print ("¡Error!")
        if clave == subarbol.obtener_elemento():
            g = subarbol.grado()
            if g == 0:
                return None
            elif g == 1:
                if subarbol.obtener_izquierdo() is not None:
                    return subarbol.obtener_izquierdo()
                else:
                    return subarbol.obtener_derecho()
            elif g == 2:
                max_izq = subarbol.obtener_izquierdo()
                while max_izq.obtener_derecho() is not None:
                    max_izq = max_izq.obtener_derecho()
                subarbol._Nodo__elemento = max_izq.obtener_elemento()
                subarbol.set_izq(self.suprimir(subarbol.obtener_izquierdo(), max_izq.obtener_elemento()))
                return subarbol
                
        else:
            if clave < subarbol.obtener_elemento():
               subarbol.set_izq(self.suprimir(subarbol.obtener_izquierdo(), clave))
            else:
                subarbol.set_der(self.suprimir(subarbol.obtener_derecho(), clave))
            return subarbol


    def buscar (self, subarbol, clave, posicion = 0):
        if subarbol is None:
            return None
    
        if clave == subarbol.obtener_elemento():
            return posicion
        elif clave < subarbol.obtener_elemento():
            posicion +=1
            return self.buscar(subarbol.obtener_izquierdo(), clave, posicion)
        else:
            posicion += 1
            return self.buscar(subarbol.obtener_derecho(), clave, posicion)


    def nivel (self, subarbol, clave, nivel):
        if subarbol is None:
            print("¡Error!")

        if clave == subarbol.obtener_elemento():
            print(f"¡El nivel es {nivel}!")
        elif clave < subarbol.obtener_elemento():
            nivel += 1
            self.nivel(subarbol.obtener_izquierdo(), clave, nivel)
        else:
            nivel += 1
            self.nivel(subarbol.obtener_derecho(), clave, nivel)
        
    def hoja (self, subarbol, clave):
        if subarbol is None:
            print("¡Error!")


        if clave == subarbol.obtener_elemento():
            g = subarbol.grado()
            if g == 0:
                print(f"¡El elemento {clave} es una hoja!")
            
            elif g == 1 or g == 2:
                print(f"¡El elemento {clave} no es una hoja!")

        elif clave < subarbol.obtener_elemento():
            self.buscar(subarbol.obtener_izquierdo(), clave)
        else:
            self.buscar(subarbol.obtener_derecho(), clave)

                            

    def hijo (self, subarbol, clave, z):
        if subarbol is None:
            print("¡Error!")

        if z == subarbol.obtener_elemento():
            if clave < subarbol.obtener_elemento():
                izq = subarbol.obtener_izquierdo()
                if clave == izq.obtener_elemento():
                    print(f"¡El Nodo {clave} si es hijo del Nodo {z}")
            else:
                der = subarbol.obtener_derecho()
                if clave == der.obtener_elemento():
                    print(f"¡El Nodo {clave} si es hijo del Nodo {z}")
        
        elif z < subarbol.obtener_elemento():
            self.hijo(subarbol.obtener_izquierdo(), clave, z)
        else:
            self.hijo(subarbol.obtener_derecho(), clave, z)


    def padre (self, subarbol, clave, z, aux):
        if subarbol is None:
            print("¡Error!")
        if clave == subarbol.obtener_elemento():
            padre = aux.obtener_elemento()
            if padre == z:
                print(f"¡El hijo Nodo {clave} tiene como padre al Nodo {z}")
        elif clave < subarbol.obtener_elemento():
            aux = subarbol
            self.padre(subarbol.obtener_izquierdo(), clave, z, aux)
        else:
            aux = subarbol
            self.padre(subarbol.obtener_derecho(), clave, z, aux)
        

    def hermano (self, subarbol, clave, aux):
        if subarbol is None:
            print("¡Error!")
        if clave == subarbol.obtener_elemento():
            if clave == aux.obtener_izquierdo().obtener_elemento() and clave < aux.obtener_derecho().obtener_elemento():
                her = aux.obtener_derecho().obtener_elemento()
                print(f"¡El Nodo {clave} tiene como hermano al Nodo {her}")
            elif clave == aux.obtener_derecho().obtener_elemento() and clave > aux.obtener_izquierdo().obtener_elemento():
                her = aux.obtener_izquierdo().obtener_elemento()
                print(f"¡El Nodo {clave} tiene como hermano al Nodo {her}")

        elif clave < subarbol.obtener_elemento():
            aux = subarbol
            self.hermano(subarbol.obtener_izquierdo(), clave, aux)
        else:
            aux = subarbol
            self.hermano(subarbol.obtener_derecho(), clave, aux)



    def camino (self, subarbol, clave, z):
        if subarbol is None:
            print("¡Error!")
        if z == subarbol.obtener_elemento():
            i = self.buscar(subarbol, clave)
            if i is not None:
                print(f"¡El camino que se debe recorrer equivale a {i}!")
            else:
                print("¡Error, el elemento no se encuentra o esta en un nivel superior!")
        elif z < subarbol.obtener_elemento():
            self.camino(subarbol.obtener_izquierdo(), clave, z)
        else:
            self.camino(subarbol.obtener_derecho(), clave, z)
        

    def altura (self, subarbol):
        if subarbol is None:
            return 0
        else: 
            return 1 + max(self.altura(subarbol.obtener_izquierdo()), self.altura(subarbol.obtener_derecho()))
        
            

    # Primero se procesa la raiz y luego sus hijos
    def preorden (self, subarbol):
        if subarbol is not None:
            print(subarbol.obtener_elemento())
            self.preorden(subarbol.obtener_izquierdo())
            self.preorden(subarbol.obtener_derecho())

    #Hijos
    def inorden (self, subarbol):
        if subarbol is not None:
            self.inorden(subarbol.obtener_izquierdo())
            print(subarbol.obtener_elemento())
            self.inorden(subarbol.obtener_derecho())

    # Hijos y luego la raiz
    def postorden (self, subarbol):
        if subarbol is not None:
            self.postorden(subarbol.obtener_izquierdo())
            self.postorden(subarbol.obtener_derecho())
            print(subarbol.obtener_elemento())


    def cantidadNodo (self, subarbol):
        if subarbol is None:
            return 0
        else:
            return 1 + (self.cantidadNodo(subarbol.obtener_izquierdo())) + (self.cantidadNodo(subarbol.obtener_derecho()))
        
    def sucesor (self, subarbol, clave, antecesor):
        if subarbol is None:
            return None
        
        if clave == subarbol.obtener_elemento():
            if subarbol.obtener_derecho() is not None:
                nodo = subarbol.obtener_derecho()
                if nodo.obtener_izquierdo() is not None:
                    print(f"¡El sucesor del Nodo {clave}, es el Nodo {nodo.obtener_elemento()}!")
                else:
                    print(f"¡El sucesor del Nodo {clave}, es el Nodo {subarbol.obtener_derecho().obtener_elemento()}!")
            else:
                if antecesor is not None:
                    print(f"¡El sucesor del Nodo {clave}, es el Nodo {antecesor.obtener_elemento()}!")
                else:
                    print(f"¡El Nodo {clave} no tiene sucesor!")

        else:
            if clave < subarbol.obtener_elemento():
                return self.sucesor(subarbol.obtener_izquierdo(),clave, subarbol)
            else:
                return self.sucesor(subarbol.obtener_derecho(), clave, subarbol)



def main():
    # Crear árbol
    arbol = abb()

    # Insertar nodos
    valores = [50, 30, 70, 20, 40, 60, 80]
    for v in valores:
        arbol.insertar(arbol.obtener_raiz(), v)

    print("=== Árbol Inorden ===")
    arbol.inorden(arbol.obtener_raiz())

    print("\n=== Árbol Preorden ===")
    arbol.preorden(arbol.obtener_raiz())

    print("\n=== Árbol Postorden ===")
    arbol.postorden(arbol.obtener_raiz())

    # Buscar elementos
    print("\n=== Buscar elementos ===")
    for v in [30, 90]:
        pos = arbol.buscar(arbol.obtener_raiz(), v)
        if pos is not None:
            print(f"Elemento {v} encontrado en posición {pos}")
        else:
            print(f"Elemento {v} no encontrado")

    # Nivel de un nodo
    print("\n=== Nivel de un nodo ===")
    arbol.nivel(arbol.obtener_raiz(), 40, 0)

    # Comprobar si un nodo es hoja
    print("\n=== Verificar hojas ===")
    arbol.hoja(arbol.obtener_raiz(), 20)
    arbol.hoja(arbol.obtener_raiz(), 30)

    # Padre e hijo
    print("\n=== Verificar hijo y padre ===")
    arbol.hijo(arbol.obtener_raiz(), 40, 30)
    arbol.padre(arbol.obtener_raiz(), 40, 30, arbol.obtener_raiz())

    # Hermano
    print("\n=== Verificar hermano ===")
    arbol.hermano(arbol.obtener_raiz(), 20, arbol.obtener_raiz())

    # Camino desde un nodo
    print("\n=== Camino desde nodo ===")
    arbol.camino(arbol.obtener_raiz(), 40, 50)

    # Altura del árbol
    print("\n=== Altura del árbol ===")
    print(f"Altura: {arbol.altura(arbol.obtener_raiz())}")

    # Cantidad de nodos
    print("\n=== Cantidad de nodos ===")
    print(f"Nodos totales: {arbol.cantidadNodo(arbol.obtener_raiz())}")

    # Suprimir nodos
    print("\n=== Suprimir nodos ===")
    arbol._abb__raiz = arbol.suprimir(arbol.obtener_raiz(), 20)  # hoja
    arbol._abb__raiz = arbol.suprimir(arbol.obtener_raiz(), 30)  # nodo con un hijo
    arbol._abb__raiz = arbol.suprimir(arbol.obtener_raiz(), 50)  # nodo con dos hijos

    print("Inorden tras supresiones:")
    arbol.inorden(arbol.obtener_raiz())

if __name__ == "__main__":
    main()

