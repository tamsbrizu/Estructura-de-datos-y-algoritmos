from colaE import colaE
import random

def insertar (cajeros, x):
    n = 0
    if cajeros[0].vacia() and cajeros[1].vacia():
        n = random.randint(0, 1)
        cajeros[n].insertar(x)
    elif cajeros[0].vacia() and not cajeros[1].vacia():
        cajeros[0].insertar(x)
    elif cajeros[1].vacia() and not cajeros[0].vacia():
        cajeros[1].insertar(x)
    elif cajeros[0].obtener_cant() < cajeros[1].obtener_cant():
        cajeros[0].insertar(x)
    elif cajeros[1].obtener_cant() < cajeros[0].obtener_cant():
        cajeros[1].insertar(x)

def simulacion ():
    c1 = colaE()
    c2 = colaE()

    reloj_simulacion = 360

    cajeros = [c1, c2]
    proceso = [5, 3]
    llegada = 2
    atendido = [False, False]

    tp = [0,0]
    cantA = [0,0]
    reloj = 0

    while reloj <= reloj_simulacion:
        if random.randint(1, llegada) == 1:
            insertar(cajeros, reloj)
        
        for i in range(2):
            if atendido[i]:
                tp[i] -= 1
            if tp[i] == 0:
                atendido[i] = False
            if not atendido[i] and not cajeros[i].vacia():
                tp[i] = proceso[i]
            if tp[i] > 0 and not atendido[i]:
                atendido[i] = True
                actual = cajeros[i].suprimir()
                cantA[i] += 1
            
        reloj += 1

   
    print(f"La cantidad de atendidos para el cajero 1 es de: {cantA[0]}")
    print(f"La cantidad de atendidos para el cajero 2 es de: {cantA[1]}")

simulacion()

            
