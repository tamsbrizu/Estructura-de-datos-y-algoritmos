'''Ejercicio 2 – Cajeros de supermercado con compras

Descripción:

Hay 3 cajeros y una cola única.

Cada cliente tiene: nombre, cantidad de artículos.

El tiempo de atención depende de la cantidad de artículos (1 minuto por artículo).

Clientes llegan cada 1-3 minutos aleatoriamente.

Objetivos:

Simular 60 minutos.

Cuántos clientes atendió cada cajero.

Qué cliente pasó más tiempo esperando.

Estado de la cola al final de la simulación (mostrar nombre y cantidad de artículos).

Datos a guardar por cliente: nombre, cantidad de artículos, minuto de llegada, cajero asignado.'''

from colaE import colaE
import random


class cliente:
     
    def __init__ (self, n, c, m):
        self.nombre = n
        self.cant = c
        self.min = m


    
def simulacion (n, c):
    c = colaE()
    rs = 60
    reloj = 0
    llegada = 3
    cantA = [0,0]
    atendido = [False, False, False]
    tp = [0,0,0]
    
    while reloj <= rs:
        if random.randint(1, llegada) == 1:
            cli = cliente(n, c, reloj)
            c.insertar(cli)

        for i in range(3):
            if atendido[i]:
                tp[i] -= 1
            if tp[i] == 0:
                atendido[i] = False
            if not atendido[i] and not c.vacia():
                actual = c.suprimir()
                tp[i] = actual.cant
                atendido[i] = True
                cantA[i] += 1
        
        reloj += 1

    print(f"La cantidad de atendidos para el cajero 1 es de: {cantA[0]}")
    print(f"La cantidad de atendidos para el cajero 2 es de: {cantA[1]}")
    print(f"La cantidad de atendidos para el cajero 3 es de: {cantA[2]}")

