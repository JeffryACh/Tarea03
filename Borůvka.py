# 1.c Implementación de Borůvka

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
    Implementación del algoritmo de Borůvka para encontrar el árbol de expansión mínima (MST) de un grafo.
    @param:
        vertices(list): Lista de vértices del grafo.
        edges(list): Lista de aristas del grafo, donde cada arista es una tupla (u, v, peso).
    @return:
        mst(list): Lista de aristas que forman el árbol de expansión mínima.
"""
def boruvka_mst(vertices, edges):
    # Inicializar el MST resultante
    mst = []
    # Cada vértice inicia como su propio padre (conjuntos individuales)
    parent = {v: v for v in vertices}
    # El rango inicia en 0 para todos los vértices
    rank = {v: 0 for v in vertices}
    # Llevamos el control de cuántos componentes (árboles) nos quedan por unir
    num_trees = len(vertices)
    # El algoritmo termina cuando todos los vértices estén en un solo árbol
    while num_trees > 1:
        # Diccionario para guardar la arista más barata de cada componente
        cheapest = {v: None for v in vertices}
        # Iterar sobre todas las aristas para encontrar las más baratas
        for u, v, weight in edges:
            # Encontrar a qué componente pertenece cada vértice
            set1 = find(parent, u)
            set2 = find(parent, v)
            # Si están en diferentes componentes, evaluamos si es la arista más barata
            if set1 != set2:
                # Actualizar si no hay arista registrada o si la actual es más barata para el conjunto 1
                if not cheapest[set1] or cheapest[set1][2] > weight:
                    cheapest[set1] = (u, v, weight)
                # Actualizar si no hay arista registrada o si la actual es más barata para el conjunto 2
                if not cheapest[set2] or cheapest[set2][2] > weight:
                    cheapest[set2] = (u, v, weight)
        # Iterar sobre los vértices para agregar las aristas baratas encontradas al MST
        for node in vertices:
            # Si el componente tiene una arista barata registrada
            if cheapest[node]:
                u, v, weight = cheapest[node]
                # Volvemos a verificar los conjuntos por si se unieron en un paso anterior del mismo ciclo
                set1 = find(parent, u)
                set2 = find(parent, v)
                # Si aún pertenecen a componentes diferentes
                if set1 != set2:
                    # Agregar la arista al árbol de expansión mínima (MST)
                    mst.append((u, v, weight))
                    # Unir los dos conjuntos
                    union(parent, rank, set1, set2)
                    # Reducir la cantidad de árboles independientes
                    num_trees -= 1
    return mst

# Inicializar variables de prueba (Instancia)
vertices = ['A', 'B', 'C', 'D', 'E']
edges = [('A','B',2), ('A','D',1), ('B','D',3), ('B','C',4), ('B','E',5), ('C','E',1), ('D','E',6)]

vertices2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
edges2 = [('A','B',2), ('A','D',1), ('B','D',3), ('B','C',4), ('B','E',5), ('C','E',1), ('D','E',6), 
          ('E','F',7), ('F','G',8), ('G','H',9), ('H','I',10), ('I','J',11)]

# Imprimir resultados
print("Boruvka MST:", boruvka_mst(vertices, edges), '\n')
print("--------------------------------------------------------------------\n")
print("Boruvka MST:", boruvka_mst(vertices2, edges2), '\n')