'''bucle itera cada minuto, la impresora toma un trabajo (si la impresora esta libre), el trabajo 
tiempo de llegada - tiempo actual (tiempo que estuvo) si se completa y se cuenta el trabajo como completado
en un mismo minuto una impresora puede imprimir otra fotocopia'''

##Ejercicio 7 con Cola Secuencial

from Ejercicio5CSecuencial import cola
import random

##Definimos una clase trabajo para guardar los procesos que debemos imprimir

class trabajo:
    __id: int ##Numero de trabajo ingresado
    __paginas: int ##Cantidad de paginas
    __llegada: int ##Tiempo en que llega el trabajo

    def __init__ (self, xid, paginas):
        self.__id = xid
        self.__paginas = paginas
        self.__llegada = 0

    def getId (self):
        return self.__id
    
    def getPaginas(self):
        return self.__paginas
    
    def getLlegada (self):
        return self.__llegada
    
    def setPaginas(self, paginas):
        self.__paginas = paginas

    def setLlegada (self, reloj):
        self.__llegada = reloj
    
    def mostrarDatos (self):
        return (f"Id: {self.__id} - Paginas: {self.__paginas}")
    

##Llamamos a un metodo "simulacion" para realizar la simulacion de la impresora con numero aletorios en el tiempo de llegada y la cantidad de paginas


def simulacion ():
    
    ##Definimos variables con los datos proporcionados del enunciado

    velocidad_impresion = 10
    tiempo_de_impresora = 3
    tiempo_de_llegada_pro = 5
    tiempo_simulacion = 60
    max_paginas = 100

    impresora_disponible = 0
    contador_trabajos_com = 0
    lista_trabajos_comp = []
    reloj_simulacion = 0
    tiempo_espera = 0
    espera = 0
    tiempo_total = 0
    id_trabajo = 1

    C = cola(100000000)

    while reloj_simulacion <= tiempo_simulacion:

        if random.randint(1, tiempo_de_llegada_pro) == 1: ##Se genera un nuevo trabajo
            paginas = random.randint(1, max_paginas)
            nuevo = trabajo(id_trabajo, paginas)
            nuevo.setLlegada(reloj_simulacion) ##Se guarda en el momento que llega
            print(f"❗: Trabajo {nuevo.getId()} con {nuevo.getPaginas()} paginas, llega en el minuto [{reloj_simulacion}].")
            C.insertar(nuevo)
            id_trabajo += 1

        if impresora_disponible == 0 and not C.vacia():
            actual = C.suprimir() ##Obtiene el trabajo actual
            impresora_disponible = tiempo_de_impresora
            tiempo_total += impresora_disponible ##Se suma el tiempo total

            paginas_a_imprimir = min(actual.getPaginas(), velocidad_impresion * impresora_disponible) ##Obtiene las paginas que se pueden imprimir con la velocidad de la impresora con respecto del tiempo
            tiempo_de_impresion = paginas_a_imprimir / velocidad_impresion ##El tiempo que llevara imprimir las paginas
            paginas_restantes = actual.getPaginas() - paginas_a_imprimir
            actual.setPaginas(paginas_restantes)

                
            if actual.getPaginas() == 0:
                tiempo_espera = reloj_simulacion - actual.getLlegada() ##Se calcula el tiempo de espera que le tomo al trabajo
                espera += tiempo_espera ##Tiempo total de espera
                contador_trabajos_com += 1
                lista_trabajos_comp.append(actual)
                print(f"✅: El trabajo {actual.getId()} fue completado.")
            else:
                print(f"❌: El trabajo {actual.getId()} tiene paginas restantes {actual.getPaginas()}. Regresa a la Cola.")
                C.insertar(actual)

        reloj_simulacion += 1
        if impresora_disponible > 0:
            impresora_disponible -= 1

    print(f"🔸La cantidad de trabajos completados es de: {contador_trabajos_com}")
    
    print(f"🔸La cantidad de trabajos restantes es de: {C.cantidad()}")
    print(f"🔸Tiempo de espera total: {espera}")
    print(f"🔸El tiempo promedio es de: {espera / len(lista_trabajos_comp)}")



simulacion()
            



            
    







