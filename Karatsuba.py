# 2.b Implementación de Karatsuba

"""
    Implementación del algoritmo Divide-y-Vencerás Karatsuba para la multiplicación eficiente de dos enteros.
    @param:
        x(int): Primer número entero a multiplicar.
        y(int): Segundo número entero a multiplicar.
    @return:
        resultado(int): El producto de x e y.
"""
def karatsuba(x, y):
    # Condición de parada: si alguno de los números es de un solo dígito, se multiplican normalmente
    if x < 10 or y < 10:
        return x * y
    # Encontrar la longitud máxima entre los dos números (en base a cantidad de dígitos)
    m = max(len(str(x)), len(str(y)))
    # Calcular la mitad de la longitud para hacer la división
    m2 = m // 2
    # Dividir el primer número 'x' en dos partes: alta (high1) y baja (low1)
    high1, low1 = divmod(x, 10**m2)
    # Dividir el segundo número 'y' en dos partes: alta (high2) y baja (low2)
    high2, low2 = divmod(y, 10**m2)
    # Llamada recursiva 1: Multiplicar las partes bajas
    z0 = karatsuba(low1, low2)
    # Llamada recursiva 2: Multiplicar la suma de las partes (alta + baja) de ambos números
    z1 = karatsuba((low1 + high1), (low2 + high2))
    # Llamada recursiva 3: Multiplicar las partes altas
    z2 = karatsuba(high1, high2)
    # Ensamblar el resultado usando la fórmula de Karatsuba: z2*10^(2*m2) + (z1-z2-z0)*10^(m2) + z0
    resultado = (z2 * 10**(2 * m2)) + ((z1 - z2 - z0) * 10**(m2)) + z0
    return resultado

# Inicializar variables de prueba (Instancias)
num1_a = 1234
num1_b = 5678

num2_a = 12345678
num2_b = 87654321

# Imprimir resultados
print("Karatsuba (1234 * 5678):", karatsuba(num1_a, num1_b), '\n')
print("--------------------------------------------------------------------\n")
print("Karatsuba (12345678 * 87654321):", karatsuba(num2_a, num2_b), '\n')