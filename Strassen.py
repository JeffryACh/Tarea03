# 2.c Implementación de Strassen

"""
    Función auxiliar para sumar dos matrices.
    @param:
        A(list): Primera matriz (lista de listas).
        B(list): Segunda matriz (lista de listas).
    @return:
        list: Matriz resultante de la suma.
    """
def add_matrix(A, B):
    # Sumar elemento por elemento usando comprensión de listas
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

"""
    Función auxiliar para restar dos matrices.
    @param:
        A(list): Primera matriz (lista de listas).
        B(list): Segunda matriz (lista de listas).
    @return:
        list: Matriz resultante de la resta.
"""
def sub_matrix(A, B):
    # Restar elemento por elemento usando comprensión de listas
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

"""
    Función auxiliar para dividir una matriz en 4 sub-matrices de igual tamaño (cuadrantes).
    @param:
        matrix(list): Matriz cuadrada de tamaño N x N (donde N es par).
    @return:
        tuple: Cuatro sub-matrices (a, b, c, d).
"""
def split_matrix(matrix):
    # Calcular el punto medio
    mid = len(matrix) // 2
    # Extraer los 4 cuadrantes usando particionado de listas nativo de Python
    a = [row[:mid] for row in matrix[:mid]]
    b = [row[mid:] for row in matrix[:mid]]
    c = [row[:mid] for row in matrix[mid:]]
    d = [row[mid:] for row in matrix[mid:]]
    return a, b, c, d

"""
    Función auxiliar para combinar 4 cuadrantes en una sola matriz.
    @param:
        c11, c12, c21, c22 (list): Las cuatro sub-matrices a combinar.
    @return:
        list: La matriz combinada final.
"""
def combine_matrix(c11, c12, c21, c22):
    # Unir horizontalmente la mitad superior
    top_half = [c11[i] + c12[i] for i in range(len(c11))]
    # Unir horizontalmente la mitad inferior
    bottom_half = [c21[i] + c22[i] for i in range(len(c21))]
    # Unir verticalmente ambas mitades
    return top_half + bottom_half

"""
    Implementación del algoritmo Divide-y-Vencerás de Strassen para multiplicación de matrices sin numpy.
    Nota: Se asume que las dimensiones de las matrices son potencias de 2 (Ej. 2x2, 4x4).
    @param:
        x(list): Primera matriz a multiplicar (lista de listas).
        y(list): Segunda matriz a multiplicar (lista de listas).
    @return:
        list: Matriz resultante del producto.
"""
def strassen(x, y):
    # Condición de parada: si la matriz es de 1x1, multiplicar y retornar como lista 2D
    if len(x) == 1:
        return [[x[0][0] * y[0][0]]]
    # Dividir la matriz 'x' en 4 sub-matrices
    a, b, c, d = split_matrix(x)
    # Dividir la matriz 'y' en 4 sub-matrices
    e, f, g, h = split_matrix(y)
    # Calcular los 7 productos recursivos de Strassen (p1 a p7) utilizando las funciones de suma y resta
    p1 = strassen(a, sub_matrix(f, h)) 
    p2 = strassen(add_matrix(a, b), h)        
    p3 = strassen(add_matrix(c, d), e)        
    p4 = strassen(d, sub_matrix(g, e))        
    p5 = strassen(add_matrix(a, d), add_matrix(e, h))        
    p6 = strassen(sub_matrix(b, d), add_matrix(g, h))        
    p7 = strassen(sub_matrix(a, c), add_matrix(e, f))  
    # Combinar los productos para formar los 4 cuadrantes de la matriz resultado (C)
    c11 = add_matrix(sub_matrix(add_matrix(p5, p4), p2), p6)
    c12 = add_matrix(p1, p2)           
    c21 = add_matrix(p3, p4)            
    c22 = sub_matrix(sub_matrix(add_matrix(p1, p5), p3), p7) 
    # Retornar la matriz uniendo los 4 cuadrantes
    return combine_matrix(c11, c12, c21, c22)

# Inicializar variables de prueba (Instancias) en formato de lista estándar
matriz1_A = [[1, 2], [3, 4]]
matriz1_B = [[5, 6], [7, 8]]

matriz2_A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
matriz2_B = [
    [16, 15, 14, 13],
    [12, 11, 10, 9],
    [8, 7, 6, 5],
    [4, 3, 2, 1]
]

# Helper visual para imprimir matrices de forma legible
def print_matrix(mat):
    for row in mat:
        print(row)

# Imprimir resultados
print("Strassen (Matriz 2x2):")
print_matrix(strassen(matriz1_A, matriz1_B))
print("\n--------------------------------------------------------------------\n")
print("Strassen (Matriz 4x4):")
print_matrix(strassen(matriz2_A, matriz2_B))