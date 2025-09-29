'''📌 Ejercicio 3 – Consultorio médico

En un consultorio:

El doctor atiende cada paciente en 8 minutos.

Los pacientes llegan cada 3 minutos en promedio.

👉 Simular durante 30 minutos:

¿Cuántos pacientes lograron atenderse?

¿Cuántos quedaron en espera?

¿En qué minuto la cola llegó a tener más pacientes esperando?'''

from colaE import colaE
import random

def simulacion ():
    c = colaE()
    rsimulacion = 30
    llegada = 3
    proceso = 8

    reloj = 0
    tp = 0
    atendido = False
    cantA = 0
    minu = 0
    m = 0

    while reloj <= rsimulacion:
        if random.randint(1, llegada) == 1:
            c.insertar(reloj)
        
        if c.obtener_cant() > m:
            m = c.obtener_cant()
            minu = reloj

        if atendido:
            tp -= 1
        if tp == 0:
            atendido = False

        if not atendido and not c.vacia():
            tp = proceso
        if tp > 0 and not atendido:
            atendido = True
            actual = c.suprimir()
            cantA += 1
        
        reloj += 1

    print(f"La cantidad de atendidos es: {cantA}")
    print(f"La cantidad de no atendidos es: {c.obtener_cant()}")
    print(F"El minuto con mayor clientes es espera es de: {minu}")


simulacion()