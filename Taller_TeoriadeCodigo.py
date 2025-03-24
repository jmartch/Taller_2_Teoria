"""
Miembros:
Vivian Buelvas
Juanangel Martinez
"""
import math
from itertools import product
import numpy as np

def codewords(G, q):
    G = np.array(G)
    k, n = G.shape
    u = list(product(range(q), repeat=k))

    # Genera las codewords aplicando la multiplicación de matrices y el módulo
    codewords = [tuple(map(int, np.dot(c, G) % q)) for c in u]
    return codewords

def parametros(abecedario, filas, M):
    """
    Parametros en formato [n,k,d]
    Formulas usadas:
    n = Numero de filas de la matriz
    k = log(base(q)) de M
    d = n-k+1
    """
    k = math.log(M, abecedario)
    d = filas - k + 1  # Corregido: usar filas en lugar de "n"

    print(f"Parámetros formato [n, M]: [{filas}, {M}]")
    print(f"Formato [n, k, d]: [{filas}, {k:.2f}, {d:.2f}]")

def matriz_H(G, q):
    G = np.array(G)
    k, n = G.shape
    if k >= n:
        raise ValueError("La matriz G no tiene la forma [I_k | P] válida.")

    # Extraer P de G en forma sistemática: G = [I_k | P]
    P = G[:, k:]  # Corregido para tomar todas las columnas desde k en adelante
    P_Tras = P.T

    Identidad_nk = np.eye(n - k, dtype=int)  # Matriz identidad de tamaño (n-k)
    H = np.hstack((P_Tras, Identidad_nk)) % q  # Concatenar y aplicar módulo para campo

    return H.tolist()

# Menú principal
w = False
while not w:
    print("\nBienvenido a DecodeTalker")
    opcion = input("Opciones:\n"
                   "1. G para un código ternario\n"
                   "2. G para un código binario\n"
                   "3. Salir\n")

    if opcion in ["1", "2"]:
        print("Ingrese las dimensiones de la matriz")
        n = int(input("Ingrese n filas: "))
        m = int(input("Ingrese m columnas: "))
        q = 3 if opcion == "1" else 2  # Determinar el campo según la opción
        G = []

        # Armado de la matriz
        for _ in range(n):  # Iterar correctamente para las filas
            fila = [int(input("Ingrese un elemento: ")) for _ in range(m)]
            G.append(fila)

        # Impresión de la matriz
        print("\nMatriz Generadora G:")
        for fila in G:
            print(" ".join(map(str, fila)))

        # Impresión de codewords
        print(f"\nLista de Codewords: L{{{', '.join(map(str, codewords(G, q)))}}}")

        # Cálculo e impresión de parámetros
        parametros(q, n, len(codewords(G, q)))

        # Construcción e impresión de la matriz de control
        print("\nMatriz de Control:")
        try:
            H = matriz_H(G, q)
            for fila in H:
                print(" ".join(map(str, fila)))
        except ValueError as e:
            print("Error:", e)

    elif opcion == "3":
        w = True
        print("Gracias por usar DecodeTalker. ¡Hasta luego!")
    else:
        print("Opción no válida. Intente nuevamente.")
