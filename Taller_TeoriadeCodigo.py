"""
Miembros:
Vivian Buelvas
Juanangel Martinez
"""


def extension_b():

def parametros_b():
    """
    Parametros en formato [n,k,d]
    Donde d = d+1 si d, solo si d es impar
    Sino de d<=d'<=d+1
    En binario [n+1 , k , d']
    """

def matriz_Hb():

def reduccion_b():

def perforacion_b():


# Menú principal
# Variables ciclo iterativo
w = False
while not w:
        print("\nBienvenido a DecodeTalker")
        opcion = input("Opciones:\n"
                       "1. G para un codigo ternario\n"
                       "2. G para un codigo binario\n"
                       "3. Salir\n")

        if opcion == "1":
            print("Ingrese las dimensiones de la matriz")
            n = int(input("Ingrese n filas "))
            m = int(input("Ingrese las m columnas: "))
            G= []
            #Armado matriz
            for n in range(n):
                a=[]
                for m in range(m):
                    a.append(int(input("Ingrese un elemento ")))
                G.append(a)

            #Impresion matriz
            for n in range(len(G)):
                for m in range(range(m)):
                    print(G[n][m],end=" ")
                    print()


        elif opcion == "2":
            print("Ingrese las dimensiones de la matriz")
            n = int(input("Ingrese n filas "))
            m = int(input("Ingrese las m columnas: "))
            G = []
            # Armado matriz
            for n in range(n):
                a = []
                for m in range(m):
                    a.append(int(input("Ingrese un elemento ")))
                G.append(a)

            # Impresion matriz
            for n in range(len(G)):
                for m in range(range(m)):
                    print(G[n][m], end=" ")
                    print()
        elif opcion == "3":
            w = True
            print("Gracias por usar DecodeTalker. ¡Hasta luego!")
        else:
            print("Opción no válida. Intente nuevamente.")