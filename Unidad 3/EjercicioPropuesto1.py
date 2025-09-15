class Nodo:
    __nombre: str
    __telefono: str
    __sig: None

    def __init__ (self, n, t):
        self.__nombre = n
        self.__telefono = t
        self.__sig = None

    def getNombre (self):
        return self.__nombre
    
    def getTelefono (self):
        return self.__telefono
    
    def obtener_sig (self):
        return self.__sig

    def set_sig (self, valor):
        self.__sig = valor

    def mostrarDatos (self):
        return (f"Nombre del contacto: {self.__nombre} - Telefono del contacto: {self.__telefono}")


'''Ejercicio 1: Agenda de Contactos (Lista Secuencial, lista encadenada)
Objetivo: Implementar una agenda de contactos utilizando lista encadenada, de manera que cada se guarde ordenado alfabéticamente por nombre,  cada contacto tiene nombre y teléfono. 
Se pide :
Insertar contacto, deberá validar que el contacto no existe en la agenda
Eliminar contacto.
Dado el nombre de un contacto, mostrar su número de telefono.'''


class le:
    __cant: int
    __cabeza: Nodo

    def __init__ (self):
        self.__cabeza = None
        self.__cant = 0

    def vacia (self):
        return self.__cant == 0
 
    def buscar (self, n):
        i = 0
        ban = False
        aux = self.__cabeza
        while not ban and aux is not None:
            if aux.getNombre() == n:
                ban = True
            else:
                i += 1
                aux = aux.obtener_sig()
            
        if ban:
            return 
        else:
            return -1
        

    def insertar (self, n, t):

        nuevo = Nodo(n, t)

        validar = self.buscar(n)

        if validar == -1:
            if self.vacia() or n < self.__cabeza.getNombre():
                nuevo.set_sig(self.__cabeza)
                self.__cabeza = nuevo
                self.__cant += 1
            else:
                aux = self.__cabeza
                while aux.obtener_sig() is not None and n > aux.obtener_sig().getNombre():
                    aux = aux.obtener_sig()

                nuevo.set_sig(aux.obtener_sig())
                aux.set_sig (nuevo)
                self.__cant += 1
        else:
            print("El contacto ya se encuentar en la lista.")

    def suprimir (self, n):
        if not self.vacia():
           if self.__cabeza.getNombre() == n:
               eliminado = (self.__cabeza.getNombre(), self.__cabeza.getTelefono())
               self.__cabeza = self.__cabeza.obtener_sig()
               self.__cant -= 1
               return eliminado
           else:
                aux = self.__cabeza
                while aux.obtener_sig() is not None:
                    if aux.obtener_sig().getNombre() == n:
                        eliminado = (aux.getNombre(), aux.getTelefono())
                        aux.set_sig(aux.obtener_sig().obtener_sig())
                        self.__cant -= 1
                        return eliminado
                    aux = aux.obtener_sig()

        else:
           print("La lista esta vacia.")

    
    def recorrer (self):
        aux = self.__cabeza
        while aux is not None:
            print(aux.mostrarDatos())
            aux = aux.obtener_sig()

    def localizarTelefono (self, n):
        ban = False
        aux = self.__cabeza
        retorno = None
        while not ban and aux is not None:
            if aux.getNombre() == n:
                ban = True
                retorno = aux.getTelefono()
            else:
                aux = aux.obtener_sig()

        return retorno 
        


if __name__ == "__main__":

    contactos = le()


    print("\nInserando contactos....")
    contactos.insertar("Laura", "26431391")
    contactos.insertar("Abel", "26487391")
    contactos.insertar("Coral", "26431241")
    contactos.insertar("Marcos", "26436791")

    print("\nMostrar Contactos...")
    contactos.recorrer()

    print("\nEliminar contacto...")
    contactos.suprimir("Abel")
    contactos.recorrer()

    r = contactos.localizarTelefono("Laura")
    if r is not None:
        print(f"\nEl contacto se encuentra en la lista de contactos y su numero de telefono es: {r}")
    else:
        print("\nEl contacto no se encuentra en la lista de contactos.")
