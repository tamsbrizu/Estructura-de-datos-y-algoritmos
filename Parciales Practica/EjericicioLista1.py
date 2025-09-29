'''Intersección única
Dadas dos listas, devolver una lista con los elementos que aparezcan en ambas, sin repetición.

Entrada: lista1 = [4, 5, 6], lista2 = [5, 6, 7]

Salida: [5, 6]'''

from listaEnC import listaEC

lista1 = listaEC()
lista1.insertar(4)
lista1.insertar(6)
lista1.insertar(5)

lista2 = listaEC()

lista2.insertar(5)
lista2.insertar(7)
lista2.insertar(6)


def listaAmbas (l1, l2):
    lista = []
    e1 = l1.obtener_cab()
    e2 = l2.obtener_cab()

    while e1 is not None and e2 is not None:
        if e1.obtener_elemento() == e2.obtener_elemento():
            lista.append(e1.obtener_elemento())
            e1 = e1.obtener_sig()
            e2 = e2.obtener_sig()
        elif e1.obtener_elemento() < e2.obtener_elemento():
            e1 = e1.obtener_sig()
        else:
            e2 = e2.obtener_sig()

    print("Mostrando lista")
    for ele in lista:
        print(ele)


listaAmbas(lista1, lista2)
