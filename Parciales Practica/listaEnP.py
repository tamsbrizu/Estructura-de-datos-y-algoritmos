from claseNodo import Nodo

class listaEP:
    __cab: Nodo
    __cant: int

    def __init__ (self):
        self.__cant = 0
        self.__cab = None

    def vacia (self):
        return self.__cant == 0
    
    def primer_elemento (self):
        return self.__cab.obtener_elemento()
    
    def ultimo_elemento(self):
    
    def insertar (self, x, p):
        if p >= 1 and p <= self.__cant + 1:
            nuevo = Nodo(x)
            if p == 1:
                nuevo.set_sig(self.__cab)
                self.__cab = nuevo
                self.__cant += 1
            else:
                i = 1
                aux = self.__cab
                while i < p - 1 and aux is not None:
                    aux = aux.obtener_sig()
                    i += 1
                nuevo.set_sig(aux.obtener_sig())
                aux.set_sig(nuevo)
                self.__cant += 1

    def suprimir (self, p):
        if not self.vacia():
            if p >= 1 and p <= self.__cant:
                if p == 1:
                    eliminado = self.__cab.obtener_elemento()
                    self.__cab = self.__cab.obtener_sig()
                    self.__cant -= 1
                    return eliminado
                else:
                    i = 1
                    aux = self.__cab
                    while i < p - 1 and aux is not None:
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



def main():
    lista = listaEP()

    print("Insertando elementos...")
    lista.insertar(10, 1)   # Inserta en la cabeza
    lista.insertar(20, 2)   # Inserta en posición 2
    lista.insertar(30, 3)   # Inserta en posición 3
    lista.insertar(15, 2)   # Inserta en posición 2

    print("\nElementos en la lista después de insertar:")
    lista.recorrer()

    print("\nEliminando elementos...")
    eliminado = lista.suprimir(1)   # Elimina el primero
    print("Eliminado:", eliminado)

    eliminado = lista.suprimir(3)   # Elimina en posición 2
    print("Eliminado:", eliminado)

    print("\nElementos en la lista después de eliminar:")
    lista.recorrer()

if __name__ == "__main__":
    main()