class Nodo:
    __elemento: str
    __cont: int
    __izq: None
    __der: None

    def __init__(self, e, c):
        self.__elemento = e
        self.__cont = c
        self.__izq = None
        self.__der = None

    def obtener_elemento(self):
        return self.__elemento
    
    def obtener_contador (self):
        return self.__cont
    
    def set_cont (self, valor):
        self.__cont = valor
    
    def obtener_izquierdo (self):
        return self.__izq
    
    def obtener_derecho (self):
        return self.__der

    def set_izq (self, valor):
        self.__izq = valor

    def set_der (self, valor):
        self.__der = valor

    def __lt__ (self, valor):
        return self.__cont < valor.obtener_cont()

class huffman:
    __cab: Nodo

    def __init__(self):
        self.__cab = None

    def insertar(self, texto):
        # 1. Contar apariciones de cada carácter
        letras = []
        apariciones = []
        for c in texto:
            if c in letras:
                idx = letras.index(c)
                apariciones[idx] += 1
            else:
                letras.append(c)
                apariciones.append(1)

        # 2. Crear lista de nodos
        nodosLista = []
        for i in range(len(letras)):
            nodosLista.append(Nodo(letras[i], apariciones[i]))

        # 3. Construir árbol de Huffman
        while len(nodosLista) > 1:
            # Ordenar por frecuencia
            nodosLista.sort(key=lambda x: x.obtener_contador())

            # Tomar los dos nodos con menor frecuencia
            nodo1 = nodosLista.pop(0)
            nodo2 = nodosLista.pop(0)

            # Crear nuevo nodo combinado
            nuevo_nodo = Nodo(None, nodo1.obtener_contador() + nodo2.obtener_contador())
            nuevo_nodo.set_izq(nodo1)
            nuevo_nodo.set_der(nodo2)

            # Agregar nuevo nodo a la lista
            nodosLista.append(nuevo_nodo)

        # 4. Guardar la raíz del árbol
        self.__cab = nodosLista[0]

    # Función para generar códigos de Huffman
    def generar_codigos(self):
        codigos = {}
        def recorrer(nodo, codigo=""):
            if nodo is None:
                return
            if nodo.obtener_elemento() is not None:
                codigos[nodo.obtener_elemento()] = codigo
            recorrer(nodo.obtener_izquierdo(), codigo + "0")
            recorrer(nodo.obtener_derecho(), codigo + "1")
        recorrer(self.__cab)
        return codigos

    # Función para codificar texto
    def codificar(self, texto):
        codigos = self.generar_codigos()
        return ''.join(codigos[c] for c in texto)

    # Función para decodificar texto
    def decodificar(self, texto_codificado):
        resultado = ""
        nodo = self.__cab
        for bit in texto_codificado:
            nodo = nodo.obtener_izquierdo() if bit == "0" else nodo.obtener_derecho()
            if nodo.obtener_elemento() is not None:
                resultado += nodo.obtener_elemento()
                nodo = self.__cab
        return resultado

# --- Ejemplo de uso ---
texto = "esto es un ejemplo de Huffman"
h = huffman()
h.insertar(texto)

codigos = h.generar_codigos()
print("Códigos Huffman:", codigos)

texto_codificado = h.codificar(texto)
print("Texto codificado:", texto_codificado)

texto_decodificado = h.decodificar(texto_codificado)
print("Texto decodificado:", texto_decodificado)
