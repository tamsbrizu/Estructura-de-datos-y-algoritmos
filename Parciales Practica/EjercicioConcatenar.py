from listaEnC import listaEC

lista1 = listaEC()
lista1.insertar(30)
lista1.insertar(25)

lista2 = listaEC()

lista2.insertar(5)
lista2.insertar(2)
lista2.insertar(40)

def concatenar (l1, l2):
    lista = []
    eL1 = l1.obtener_cab()
    eL2 = l2.obtener_cab()
    while eL1 is not None or eL2 is not None:
        if eL1 is not None and eL2 is not None:
            lista.append(eL1.obtener_elemento())
            lista.append(eL2.obtener_elemento())
            eL1 = eL1.obtener_sig()
            eL2 = eL2.obtener_sig()
        elif eL1 is not None and eL2 is None:
            lista.append(eL1.obtener_elemento())
            eL1 = eL1.obtener_sig()

        elif eL2 is not None and eL1 is None:
            lista.append(eL2.obtener_elemento())
            eL2 = eL2.obtener_sig()

    print("Lista concatenada")
    for ele in lista:
        print(ele)


concatenar(lista1, lista2)