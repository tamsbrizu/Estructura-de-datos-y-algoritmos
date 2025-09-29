from colaE import colaE
import random

def simulacion():
    c = colaE()
    relojS = 300
    proceso = [6, 4]
    llegada = 3
    atendido = [False, False]

    tp = [0,0]
    cantA = [0,0]
    reloj = 0

    while reloj <= relojS:
        if random.randint(1, llegada) == 1:
            c.insertar(reloj)
        
        for i in range(2):
            if atendido[i]:
                tp[i] -= 1
            if tp[i] == 0:
                atendido[i] = False
            if not atendido[i] and not c.vacia():
                tp[i] = proceso[i]
                actual = c.suprimir()
                atendido[i] = True
                cantA[i] += 1
            
        reloj += 1

    print(f"La cantidad de atendidos para el cajero 1 es de: {cantA[0]}")
    print(f"La cantidad de atendidos para el cajero 2 es de: {cantA[1]}")

simulacion()
