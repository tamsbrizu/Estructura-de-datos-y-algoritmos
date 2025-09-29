'''📌 Ejercicio 2 – Inscripciones en el IP

En el Instituto Politécnico hay 1 secretaria que tarda 5 minutos en inscribir a cada alumno.

Cada alumno llega cada 1 minuto en promedio.

👉 Simular durante 15 minutos:

¿Cuántos alumnos fueron atendidos?

¿Cuántos quedaron esperando?

Representar el estado de la cola al minuto 15.'''

from colaE import colaE
import random

def simulacion ():
    c = colaE()
    reloj_simulacion = 15
    proceso = 5
    llegada = 1

    reloj = 0
    atendido = False 
    tp = 0
    cantA = 0
    lista = []


    while reloj <= reloj_simulacion:
        if random.randint(1, llegada) == 1:
            c.insertar(reloj)

        if atendido:
            tp -= 1
        if tp == 0:
            atendido = False
        if not atendido and not c.vacia():
            tp = proceso
            actual = c.suprimir()
            cantA += 1
            atendido = True
            
        
        '''if reloj == 15:
            lista.append(colaE)'''

    print(f"La cantidad de alumnos atendidos es de: {cantA}")
    print(f"La cantidad de no atendidos es de: {c.obtener_cant()}")
    '''print("El estado de la cola en el minuto 15 es: ")
    for ele in lista:
        print(ele)'''

simulacion()