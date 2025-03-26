"""
Miembros:
Vivian Buelvas
Juanangel Martinez
Ronald Arrieta
"""
import math
from itertools import product
import numpy as np

def codewords(G, q):
    G = np.array(G)
    k, n = G.shape
    u = list(product(range(q), repeat = k))
    C = [tuple(map(int, np.dot(np.array(c), G) % q)) for c in u]
    return C

def extencion(C, q):
  C_ext = []
  for cw in C:
    suma = sum(cw)
    c_e = (-suma)%q
    cw_e = cw + (c_e,)
    C_ext.append(cw_e)
  return C_ext


def parametros(abecedario, filas, M):
    k = math.log(M, abecedario)
    d = filas - k + 1  

    print(f"Parámetros formato [n, M]: [{filas}, {M}]")
    print(f"Formato [n, k, d]: [{filas}, {k:.2f}, {d:.2f}]")

def parametros_ext(n, k, d):
    n_ext = n + 1
    k_ext = k
    if d % 2 == 1:
        d_ext = d + 1
    else:
        d_ext = d
    print(f"Parámetros Código Extendido [n', k', d']: [{n_ext}, {k_ext:.2f}, {d_ext:.2f}]")
    return n_ext, k_ext, d_ext
    
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
        
        print("Ingrese las dimensiones de la matriz")
        n = int(input("Ingrese n filas: "))
        m = int(input("Ingrese m columnas: "))
        q = int(input("Ingrese el valor de q: "))

        if q < 2 or q > 3:
          print("El valor de q debe estar entre 2 y 3")
          while q < 2 or q > 3:
            q = int(input("Ingrese el valor de q: "))

        G = []

        # Armado de la matriz
        if q == 2:
          for _ in range(n):  # Iterar correctamente para las filas
            while True:
              fila = [int(input(f"Ingrese el elemento {_+1}: ")) for _ in range(m)]
              if all(elemento >= 0 and elemento < 2 for elemento in fila):
                break
              print("El valor debe ser 0 o 1")
            G.append(fila)

        
        elif q == 3:
          for _ in range(n):  # Iterar correctamente para las filas
            while True:
              fila = [int(input(f"Ingrese el elemento {_+1}: ")) for _ in range(m)]
              if all(elemento >= 0 and elemento < 3 for elemento in fila):
                break
              print("El valor debe ser 0, 1 o 2")
            G.append(fila)

        # Impresión de la matriz
        print("\nMatriz Generadora G:")
        for fila in G:
          print(" ".join(map(str, fila)))

        print("\nParámetros del código original")
        parametros(q, n, len(codewords(G, q)))

        C = codewords(G, q)
        print("\nCodewords del código:")
        for cw in C:
            print(cw)

        C_ext = extencion(C, q)
        print("\nCodewords del código extendido:")
        for cw in C_ext:
            print(cw)

        n, k, d = parametros(q, len(C[0]), len(C)) 
        print("\nParámetros del código extendido")
        parametros_ext(n, k, d)
      
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
