'''utilizando dos listas, colocar elementos que son similares sin ninguna repeticion'''

from listaEnC import listaEC

lista1 = listaEC()
lista1.insertar(7)
lista1.insertar(5)
lista1.insertar(10)
lista1.insertar(15)

lista2 = listaEC()

lista2.insertar(5)
lista2.insertar(2)
lista2.insertar(7)

def listanorepetida (l1, l2):
    lista = []
    e1 = l1.obtener_cab()
    e2 = l2.obtener_cab()

    while e1 is not None:
        if e1.obtener_elemento() not in lista:
            lista.append(e1.obtener_elemento())
        e1 = e1.obtener_sig()

    while e2 is not None:
        if e2.obtener_elemento() not in lista:
            lista.append(e2.obtener_elemento())
        e2 = e2.obtener_sig()

    print("Mostrando lista")
    for ele in lista:
        print(ele)


listanorepetida(lista1, lista2)