# 1.a Implementación de Prim

"""
    Implementación del algoritmo de Prim para encontrar el árbol de expansión mínima (MST) de un grafo.
    Esta versión no utiliza librerías externas como heapq.
    @param:
        vertices(list): Lista de vértices del grafo.
        edges(list): Lista de aristas del grafo, donde cada arista es una tupla (u, v, peso).
        start(str): Vértice inicial para comenzar el algoritmo.
    @return:
        mst(list): Lista de aristas que forman el árbol de expansión mínima.
"""
def prim_mst(vertices, edges, start):
    # Crear lista de adyacencia
    adj = {v: [] for v in vertices}
    # Agregar aristas a la lista de adyacencia en ambas direcciones (grafo no dirigido)
    for u, v, weight in edges:
        adj[u].append((weight, v))
        adj[v].append((weight, u))
    # Inicializar el MST y el conjunto de vértices visitados
    mst = []
    visited = set([start])
    # Lista estándar para guardar las aristas disponibles en lugar de un heap
    available_edges = [(weight, start, to) for weight, to in adj[start]]
    # Mientras haya aristas disponibles y no se hayan visitado todos los vértices
    while available_edges and len(visited) < len(vertices):
        # Buscar manualmente la arista con el menor peso
        min_index = 0
        for i in range(1, len(available_edges)):
            if available_edges[i][0] < available_edges[min_index][0]:
                min_index = i
        # Extraer la arista con el menor peso de la lista
        weight, frm, to = available_edges.pop(min_index)
        # Si el vértice de destino no ha sido visitado, lo agregamos al MST y a los visitados
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))
            # Agregar las nuevas aristas incidentes a la lista de disponibles
            for next_weight, next_to in adj[to]:
                # Solo agregamos las que se dirigen a vértices no visitados
                if next_to not in visited:
                    available_edges.append((next_weight, to, next_to))
    return mst

# Inicializar variables de prueba (Instancia)
vertices = ['A', 'B', 'C', 'D', 'E']
edges = [('A','B',2), ('A','D',1), ('B','D',3), ('B','C',4), ('B','E',5), ('C','E',1), ('D','E',6)]

vertices2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
edges2 = [('A','B',2), ('A','D',1), ('B','D',3), ('B','C',4), ('B','E',5), ('C','E',1), ('D','E',6), 
          ('E','F',7), ('F','G',8), ('G','H',9), ('H','I',10), ('I','J',11)]
# Imprimir resultados
print("Prim MST (Grafo 1):", prim_mst(vertices, edges, 'A'), '\n')
print("--------------------------------------------------------------------\n")
print("Prim MST (Grafo 2):", prim_mst(vertices2, edges2, 'A'), '\n')