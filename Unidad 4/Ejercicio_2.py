from Ejercicio_1 import abb

def main():
    # Crear el árbol
    arbol = abb()
    
    # Insertar nodos desde la lista
    valores = [50, 30, 70, 20, 40, 60, 80]
    for v in valores:
        arbol.insertar(arbol.obtener_raiz(), v)
    
    # ------------------------------
    # a) Mostrar padre y hermano
    print("\n--- Inciso a: Padre y Hermano ---")
    nodo = 40  # Nodo a consultar
    if arbol.obtener_raiz() is not None:
        if nodo == arbol.obtener_raiz().obtener_elemento():
            print(f"El nodo {nodo} es la raíz y no tiene padre ni hermano")
        else:
            arbol.padre(arbol.obtener_raiz(), nodo, None, arbol.obtener_raiz())
            arbol.hermano(arbol.obtener_raiz(), nodo, arbol.obtener_raiz())
    
    # ------------------------------
    # b) Mostrar cantidad de nodos
    print("\n--- Inciso b: Cantidad de nodos ---")
    total = arbol.cantidadNodo(arbol.obtener_raiz())
    print(f"La cantidad de nodos del árbol es: {total}")
    
    # ------------------------------
    # c) Mostrar altura del árbol
    print("\n--- Inciso c: Altura del árbol ---")
    alt = arbol.altura(arbol.obtener_raiz())
    print(f"La altura del árbol es: {alt}")
    
    # ------------------------------
    # d) Mostrar sucesor
    print("\n--- Inciso d: Sucesor del nodo ---")
    nodo_suc = 40  # Nodo a consultar
    arbol.sucesor(arbol.obtener_raiz(), nodo_suc, None)


if __name__ == "__main__":
    main()
