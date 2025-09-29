from pilaS import pilaS

pila = pilaS(100)


def binario (n, p):
    while n > 0:
        r = n % 2
        p.insertar(r)
        n = n // 2

    p.invertir()

    print("Mostrando pila con numero binarios. ")
    p.mostrar()

binario(25, pila)
