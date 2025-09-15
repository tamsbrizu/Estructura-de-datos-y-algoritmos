## Al parcial va simulacion de cola y alguna otra funcion
## Practicar el que mando el profe
## Si en el parcial nos piden un metodo de sig y ese metodo sig depende del buscar, hay que implementar tambien el buscar porque depende de este para que funcione.

'''Ejercicio Nº 6: 
La memoria Heap puede administrarse considerando los espacios libres como bloques de 
longitud variable. Uno de los métodos para su manejo es el del primer ajuste, que consiste 
en lo siguiente: Si necesita almacenarse un dato que tiene cierto tamaño, se toma de los 
espacios libres el primero que se ajusta al tamaño deseado o un tamaño superior, en este 
último  caso,  se  utiliza  lo  requerido  y  lo  que  resta  vuelve  a  la  lista  de  espacios  libres. 
Realizar una aplicación que simule tal realidad. '''

##Clase bloque, hace referencia a cada bloque que va a estar en el heap. Contiene tamaño

class bloque:
    __t: int

    def __init__ (self, t):
        self.__t = t

    def getTam (self):
        return self.__t
    
    def mostrarDatos (self):
        return (f"Tamaño del bloque: {self.__t}")
    

class heap:
    __ocupados: list
    __libres: list
    __tamax: int

    def __init__ (self, xmax):
        self.__tamax = xmax
        self.__libres = [bloque(self.__tamax)]
        self.__ocupados = []

    def insertar (self, t):
        for i in range (len(self.__libres)):
            blo = self.__libres[i]
            tam = blo.getTam()
            if tam == t:
                nuevo = bloque(t)
                self.__ocupados.append(nuevo)
                self.__libres.pop(i)
            elif tam >= t:
                tamActual = blo.getTam() - t
                nuevo = bloque(t)
                self.__ocupados.append(nuevo)
                self.__libres.pop(i)
                self.__libres.append(bloque(tamActual))

    def estadoBloqueL (self):
        for blo in self.__libres:
            print(blo.mostrarDatos())

    def estadoBloquesO (self):
        for blo in self.__ocupados:
            print(blo.mostrarDatos())


if __name__ == '__main__':
    H = heap(50)
    print("\nMostrar estado incial de los bloques libres.")
    H.estadoBloqueL()

    print("\nInsertando bloques nuevos.")
    H.insertar(10)
    H.insertar(5)
    H.insertar(20)
    
    print("\nMostrando el estado final de los bloques ocupados.")
    H.estadoBloquesO()

    print("\nMostrando el estado final de los bloques libres.")
    H.estadoBloqueL()
