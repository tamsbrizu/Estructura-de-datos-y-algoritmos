from Ejercicio5CSecuencial import cola
import random

class cliente:
    __id: int
    __llegada: int

    def __init__ (self, xid):
        self.__id = xid
        self.__llegada = 0

    def getId (self):
        return self.__id
    def getLlegada (self):
        return self.__llegada
    def setLlegada (self, valor):
        self.__llegada = valor

    def mostrarDatos (self):
        return (f"Cliente {self.__id} con tiempo de llegada de {self.__llegada}")


def obtenerCantidad (cola):
    return cola.cantidad()

def colaAletoria (lista_cajeros, cliente):
    numero = 0
    if lista_cajeros[0].vacia() and lista_cajeros[1].vacia() and lista_cajeros[2].vacia():
        numero = random.randint(0, 2)
        print(f"🆕: Se selecciono el cajero {numero}")
        lista_cajeros[numero].insertar(cliente)
    elif not lista_cajeros[0].vacia() and not lista_cajeros[1].vacia() and not lista_cajeros[2].vacia():
        cantidad = [lista_cajeros[0].cantidad(), lista_cajeros[1].cantidad(), lista_cajeros[2].cantidad()]
        if cantidad[0] == cantidad[1] == cantidad[2]:
            numero = random.randint(0, 2)
            lista_cajeros[numero].insertar(cliente)
        else:
            numero = cantidad.index(min(cantidad))
            lista_cajeros[numero].insertar(cliente)
    return numero

    

    
def simulacion ():
    cajero1 = cola(10000)
    cajero2 = cola(10000)
    cajero3 = cola(10000)

    lista_cajeros = [cajero1, cajero2, cajero3]

    tiempos_cajeros_actual = [0, 0, 0]
    tiempos_cajeros_simulacion = [5, 3, 4]

    tiempo_llegada_cli = 2
    tiempo_simulacion = 120

    tiempo_espera_atendidos = 0
    tiempo_espera_Natendidos = 0
    lista_atendidos = []
    lista_Natendidos = []
    lista_espera = []
    espera_total = 0
    tiempo_total = 0
    id_cliente = 1
    
    reloj_simulacion = 0

    while reloj_simulacion < tiempo_simulacion:

        if random.randint(1, tiempo_llegada_cli) == 1:
            clienteNuevo = cliente(id_cliente)
            clienteNuevo.setLlegada(reloj_simulacion)
            print(f"❗: Cliente {clienteNuevo.getId()} llega en el minuto [{clienteNuevo.getLlegada()}]")
            colaAletoria(lista_cajeros, clienteNuevo)
            id_cliente += 1

        for i in range(3):
            if not lista_cajeros[i].vacia() and tiempos_cajeros_actual[i] == 0:
                clienteO = lista_cajeros[i].suprimir()
                tiempos_cajeros_actual[i] = tiempos_cajeros_simulacion[i]
                tiempo_total += tiempos_cajeros_actual[i]
                espera = reloj_simulacion - clienteO.getLlegada()
                lista_espera.append(espera)
                espera_total += espera
                print(f"✅: Cliente {clienteO.getId()} fue atendido.")
                lista_atendidos.append(clienteO)
                tiempo_max = max(lista_espera)
                tiempo_espera_atendidos = espera_total

        reloj_simulacion += 1
        for i in range(3):
            if tiempos_cajeros_actual[i] > 0:
                tiempos_cajeros_actual[i] -= 1

    for i in range(3):
        while not lista_cajeros[i].vacia():
            clienteNA = lista_cajeros[i].suprimir()
            espera = tiempo_simulacion - clienteNA.getLlegada()
            tiempo_espera_Natendidos += espera
            lista_Natendidos.append(clienteNA)

    print(f"\n🔸Tiempo de espera de clientes Atendidos: {tiempo_espera_atendidos}")
    print("📌 Lista de clientes atendidos.")
    for cli in lista_atendidos:
        print(cli.mostrarDatos())

    print(f"\n🔸Tiempo de espera de clientes no Atendidos: {tiempo_espera_Natendidos}")
    print("📌 Lista de clientes no atendidos.")
    for cli in lista_Natendidos:
        print(cli.mostrarDatos())

    print(f"\n 🔸 Cantidad de clientes atendidos: {len(lista_atendidos)}\n 🔸 Cantidad de clientes no atendidos: {len(lista_Natendidos)}")

    print(f"\n🔸Tiempo maximo de espera: {tiempo_max}")

    print(f"\n🔸Tiempo promedio de espera de los clientes atendidos: {espera_total /len(lista_atendidos)}")
    print(f"\n🔸Tiempo promedio de espera de los clientes no atendidos: {tiempo_espera_Natendidos / len(lista_Natendidos)}")

            


simulacion()
        




            


