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

    # Extraer P de G en forma sistemática: G = [I_k | P]
    P = G[:, k:]  # Corregido para tomar todas las columnas desde k en adelante
    P_Tras = P.T

    Identidad_nk = np.eye(n - k, dtype=int)  # Matriz identidad de tamaño (n-k)
    H = np.hstack((P_Tras, Identidad_nk)) % q  # Concatenar y aplicar módulo para campo

    return H.tolist()

def perforacion(G, q, col):
    G_perforada = np.delete(G, col, axis=1)  # Elimina la columna indicada

    # Validación: asegurar que los valores siguen perteneciendo al campo F_q
    if not all(0 <= elem < q for row in G_perforada for elem in row):
        raise ValueError(f"Los valores en la matriz perforada deben estar en F_{q}")

    return G_perforada.tolist()

def reduccion(G, q, col):
    G_reducida = np.delete(G, col, axis=1)  # Elimina la columna indicada

    # Validación: asegurar que los valores siguen perteneciendo al campo F_q
    if not all(0 <= elem < q for row in G_reducida for elem in row):
        raise ValueError(f"Los valores en la matriz reducida deben estar en F_{q}")

    return G_reducida.tolist()

# Menú principal
w = False
while not w:
    print("\nBienvenido a DecodeTalker")
    opcion = input("Opciones:\n"
                   "1. G para un código ternario\n"
                   "2. G para un código binario\n"
                   "33. Salir\n")

    if opcion in ["1", "2"]:
        """
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
        """
        G = np.array([[1, 1, 0, 1, 0, 0, 0],
              [1, 0, 1, 0, 1, 0, 0],
              [0, 1, 1, 0, 0, 1, 0],
              [1, 1, 1,0,0,0,1]])
        q=2
        n=7
        # Impresión de codewords
        print(f"\nLista de Codewords: L{{{', '.join(map(str, codewords(G, q)))}}}")

        # Cálculo e impresión de parámetros
        parametros(q, n, len(codewords(G, q)))
        
        #Perforaciones y reduccion
        col = int(input("Ingrese la columna a perforar (0-indexada): "))
        try:
            G = perforacion(G, q, col)
            print("\nMatriz Generadora después de Perforación:")
            for fila in G:
                print(" ".join(map(str, fila)))
        except ValueError as e:
            print("Error:", e)
            
        col = int(input("Ingrese la columna a reducir (0-indexada): "))
        try:
            G = reduccion(G, q, col)
            print("\nMatriz Generadora después de Reducción:")
            for fila in G:
                print(" ".join(map(str, fila)))
        except ValueError as e:
            print("Error:", e)
            
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
