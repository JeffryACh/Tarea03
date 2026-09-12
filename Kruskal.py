# 1.b Implementación de Kruskal

"""
    Función auxiliar para encontrar la raíz (jefe) del conjunto al que pertenece un elemento.
    @param:
        parent(dict): Diccionario que representa el padre de cada elemento.
        item(str): Elemento del cual se quiere encontrar la raíz.
    @return:
        La raíz del conjunto al que pertenece el elemento.
"""
def find(parent, item):
    # Si el elemento es su propio padre, es la raíz
    if parent[item] == item:
        return item
    # Compresión de caminos: se actualiza el padre directamente a la raíz
    parent[item] = find(parent, parent[item])
    return parent[item]

"""
    Función auxiliar para unir dos conjuntos disjuntos basados en su rango (altura).
    @param:
        parent(dict): Diccionario que representa el padre de cada elemento.
        rank(dict): Diccionario que representa el rango de cada elemento.
        set1(str): Primer conjunto a unir.
        set2(str): Segundo conjunto a unir.
    @return:
        None
"""
def union(parent, rank, set1, set2):
    root1 = find(parent, set1)
    root2 = find(parent, set2)
    # Solo unimos si están en conjuntos diferentes
    if root1 != root2:
        # El árbol más pequeño se une debajo de la raíz del árbol más grande
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            # Si tienen el mismo rango, uno se vuelve padre y su rango aumenta
            parent[root1] = root2
            rank[root2] += 1

"""
    Implementación del algoritmo de Kruskal para encontrar el árbol de expansión mínima (MST) de un grafo.
    @param:
        vertices(list): Lista de vértices del grafo.
        edges(list): Lista de aristas del grafo, donde cada arista es una tupla (u, v, peso).
    @return:
        mst(list): Lista de aristas que forman el árbol de expansión mínima.
"""
def kruskal_mst(vertices, edges):
    # Inicializar el MST resultante
    mst = []
    # Cada vértice inicia como su propio padre (conjuntos individuales)
    parent = {v: v for v in vertices}
    # El rango inicia en 0 para todos los vértices
    rank = {v: 0 for v in vertices}
    # Ordenar todas las aristas del grafo de menor a mayor peso
    edges.sort(key=lambda x: x[2])
    # Iterar sobre las aristas ya ordenadas
    for u, v, weight in edges:
        # Encontrar las raíces de los conjuntos a los que pertenecen 'u' y 'v'
        root_u = find(parent, u)
        root_v = find(parent, v)
        # Si no pertenecen al mismo conjunto, significa que unirlos no forma un ciclo
        if root_u != root_v:
            # Agregar la arista al árbol de expansión mínima (MST)
            mst.append((u, v, weight))
            # Unir ambos conjuntos para futuras iteraciones
            union(parent, rank, root_u, root_v)
    return mst

# Inicializar variables de prueba (Instancia)
vertices = ['A', 'B', 'C', 'D', 'E']
edges = [('A','B',2), ('A','D',1), ('B','D',3), ('B','C',4), ('B','E',5), ('C','E',1), ('D','E',6)]

vertices2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
edges2 = [('A','B',2), ('A','D',1), ('B','D',3), ('B','C',4), ('B','E',5), ('C','E',1), ('D','E',6), 
          ('E','F',7), ('F','G',8), ('G','H',9), ('H','I',10), ('I','J',11)]

# Imprimir resultado
print("Kruskal MST:", kruskal_mst(vertices, edges), '\n')
print("--------------------------------------------------------------------\n")
print("Kruskal MST:", kruskal_mst(vertices2, edges2), '\n')