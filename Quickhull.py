# 2.a Implementación de Quickhull (Envolvente convexa)

"""
    Función auxiliar para determinar de qué lado de la línea formada por p1 y p2 se encuentra el punto p.
    @param:
        p1(tuple): Primer punto de la línea (x, y).
        p2(tuple): Segundo punto de la línea (x, y).
        p(tuple): Punto a evaluar (x, y).
    @return:
        int: 1 si está a un lado, -1 si está al otro, 0 si son colineales.
    """
def get_side(p1, p2, p):
    # Calcular el producto cruzado para determinar la posición relativa
    val = (p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0])
    # Retornar 1, -1 o 0 según el resultado
    if val > 0:
        return 1
    # Si el valor es negativo, el punto está en el otro lado de la línea
    if val < 0:
        return -1
    return 0

"""
    Función auxiliar para calcular la distancia de un punto p a la línea formada por p1 y p2.
    @param:
        p1(tuple): Primer punto de la línea (x, y).
        p2(tuple): Segundo punto de la línea (x, y).
        p(tuple): Punto a evaluar (x, y).
    @return:
        float/int: Valor absoluto proporcional a la distancia del punto a la línea.
    """
def get_distance(p1, p2, p):
    # Se usa el valor absoluto del producto cruzado, proporcional a la distancia real
    return abs((p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0]))

"""
    Función recursiva para encontrar los puntos de la envolvente convexa en un lado de la línea.
    @param:
        points(list): Lista de puntos a evaluar.
        p1(tuple): Primer punto de la línea base.
        p2(tuple): Segundo punto de la línea base.
        hull(set): Conjunto (para evitar duplicados) donde se almacenan los puntos de la envolvente.
    @return:
        None
"""
def build_hull(points, p1, p2, hull):
    # Condición de parada: si no hay puntos en este conjunto, terminar recursión
    if not points:
        return
    # Variables para encontrar el punto más alejado de la línea
    farthest = None
    max_dist = -1
    # Buscar el punto más distante entre los puntos dados
    for p in points:
        dist = get_distance(p1, p2, p)
        if dist > max_dist:
            max_dist = dist
            farthest = p
    # Agregar el punto más alejado al conjunto de la envolvente convexa
    hull.add(farthest)
    # Listas para dividir los puntos restantes
    s1 = []
    s2 = []
    # Asignar los puntos restantes a las áreas fuera de los nuevos segmentos formados
    for p in points:
        # Puntos que están "fuera" del segmento (p1 -> farthest)
        if get_side(p1, farthest, p) == 1:
            s1.append(p)
        # Puntos que están "fuera" del segmento (farthest -> p2)
        elif get_side(farthest, p2, p) == 1:
            s2.append(p)
    # Llamadas recursivas para procesar los nuevos subconjuntos
    build_hull(s1, p1, farthest, hull)
    build_hull(s2, farthest, p2, hull)

"""
    Implementación del algoritmo Divide-y-Vencerás Quickhull para encontrar la envolvente convexa de puntos 2D.
    @param:
        points(list): Lista de puntos (tuplas) en un plano.
    @return:
        list: Lista de puntos que conforman el perímetro o envolvente convexa.
"""
def quickhull(points):
    # Si hay menos de 3 puntos, ellos mismos forman la envolvente
    if len(points) < 3:
        return points
    # Encontrar los puntos con las coordenadas X mínima y máxima (extremos seguros de la envolvente)
    min_x = min(points, key=lambda x: x[0])
    max_x = max(points, key=lambda x: x[0])
    # Inicializar el conjunto de la envolvente convexa con estos dos puntos extremos
    hull = {min_x, max_x}
    # Listas para dividir los puntos iniciales a los dos lados de la línea
    s1 = []
    s2 = []
    # Dividir todos los puntos según el lado de la línea principal (min_x -> max_x)
    for p in points:
        # Puntos a un lado de la línea (hacia "arriba")
        if get_side(min_x, max_x, p) == 1:
            s1.append(p)
        # Al invertir p1 y p2 (max_x, min_x), el "lado opuesto" también se marca como 1
        # Esto reutiliza la lógica para los puntos hacia "abajo"
        elif get_side(max_x, min_x, p) == 1:
            s2.append(p)
    # Llamar recursivamente a la función constructora para ambos lados
    build_hull(s1, min_x, max_x, hull)
    build_hull(s2, max_x, min_x, hull)
    
    # Retornar la envolvente convirtiendo el set en lista
    return list(hull)

# Inicializar variables de prueba (Instancias)
points1 = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
points2 = [(0, 0), (0, 5), (5, 0), (5, 5), (2, 2), (3, 3), (1, 4), (4, 1), (2, 4)]

# Imprimir resultados
print("Quickhull Envolvente 1:", quickhull(points1), '\n')
print("--------------------------------------------------------------------\n")
print("Quickhull Envolvente 2:", quickhull(points2), '\n')