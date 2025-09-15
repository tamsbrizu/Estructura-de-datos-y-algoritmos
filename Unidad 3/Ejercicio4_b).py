def suma(m1,m2):
    matrizSuma = [[0 for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            suma = m1[i][j] + m2[i][j]
            matrizSuma[i][j] = suma

    recorrer(matrizSuma)

def recorrer (m):
    for i in range(2):
        for j in range(2):
            print(f"Fila: {i} - Columna: {j} ---> {m[i][j]}")


m1 = [[0 for _ in range(2)] for _ in range(2)]
m2 = [[0 for _ in range(2)] for _ in range(2)]

m1[0][1] = 1
m1[1][1] = 1

m2[1][1] = 1

print("\nMostrar Matriz 1")
recorrer(m1)

print("\nMostrar Matriz 2")
recorrer(m2)

print("\nSuma de matrices")
suma(m1,m2)


'''Inicos c)

Podemos ver que en el ejercicio 2, el nivel de complejidad del algoritmo es de O(N/2), debido que para poder insertar los elementos en el matriz de suma de debe 
recorrer dos veces con un for (en nuestro caso. La complejidad depenede el algoritmo que se realice) y en el inciso a) acerca de la listas enlazadas el nivel
de compelidad del algoritmo es de O(N + M) pues se recorrer las listas simulteanamente.'''





