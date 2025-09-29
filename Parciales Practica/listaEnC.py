from claseNodo import Nodo

class listaEC:
    __cab: Nodo
    __cant: int

    def __init__ (self):
        self.__cant = 0
        self.__cab = None

    def vacia (self):
        return self.__cant == 0
    
    def insertar (self, x):
        nuevo = Nodo(x)
        if self.vacia() or self.__cab.obtener_elemento() < x:
            nuevo.set_sig(self.__cab)
            self.__cab =nuevo
            self.__cant += 1
        else:
            aux = self.__cab
            while aux.obtener_sig() is not None and aux.obtener_sig().obtener_elemento() > x:
                aux = aux.obtener_sig()
            nuevo.set_sig(aux.obtener_sig())
            aux.set_sig(nuevo)
            self.__cant += 1

    def buscar (self, x):
        i = 0
        ban = False
        aux = self.__cab
        while not ban and aux is not None:
            if aux.obtener_elemento() == x:
                ban = True
                return i
            else:
                i += 1
                aux = aux.obtener_sig()
        
        if not ban:
            return -1
        
    def suprimir (self, x):
        if not self.vacia():
            p = self.buscar(x)
            if p != -1:
                if p == 0:
                    eliminado = self.__cab.obtener_elemento()
                    self.__cab = self.__cab.obtener_sig()
                    self.__cant -= 1
                    return eliminado
                
                else:
                    i = 1
                    aux = self.__cab
                    while i < p and aux.obtener_sig() is not None:
                        aux = aux.obtener_sig()
                        i += 1
                    
                    eliminado = aux.obtener_sig().obtener_elemento()
                    aux.set_sig(aux.obtener_sig().obtener_sig())
                    self.__cant -= 1
                    return eliminado
                

    def recorrer (self):
        aux = self.__cab
        while aux is not None:
            print(aux.obtener_elemento())
            aux = aux.obtener_sig()

    def obtener_cab (self):
        return self.__cab


def main():
    lista = listaEC()

    print("Insertando elementos...")
    lista.insertar(30)
    lista.insertar(10)
    lista.insertar(20)
    lista.insertar(40)
    lista.insertar(25)

    print("\nElementos en la lista (ordenados):")
    lista.recorrer()

    print("\nBuscando elementos...")
    print("Buscar 20 → posición:", lista.buscar(20))
    print("Buscar 15 → posición:", lista.buscar(15))

    print("\nEliminando elementos...")
    eliminado1 = lista.suprimir(10)   # elimina cabeza
    print("Eliminado:", eliminado1)
    eliminado2 = lista.suprimir(25)   # elimina intermedio
    print("Eliminado:", eliminado2)

    print("\nElementos en la lista después de eliminar:")
    lista.recorrer()

if __name__ == "__main__":
    main()