from collections import deque

def tarjan_sort(graph):
    """Algorytm Tarjana (przeszukiwanie w głąb - DFS) zrealizowany dla 3 reprezentacji."""
    if graph.n == 0: 
        return "Graf jest pusty."

    # 1. Implementacja dla Macierzy sąsiedztwa
    def tarjan_matrix():
        visited = [False] * graph.n
        rec_stack = [False] * graph.n
        stack = []
        has_cycle = [False]

        def dfs(u):
            visited[u] = True
            rec_stack[u] = True
            for v in range(graph.n):
                if graph.adj_matrix[u][v] == 1:
                    if not visited[v]:
                        dfs(v)
                    elif rec_stack[v]:
                        has_cycle[0] = True
            rec_stack[u] = False
            stack.append(u)

        for i in range(graph.n):
            if not visited[i] and not has_cycle[0]:
                dfs(i)
        return "Wykryto cykl!" if has_cycle[0] else stack[::-1]

    # 2. Implementacja dla Listy następników
    def tarjan_list():
        visited = [False] * graph.n
        rec_stack = [False] * graph.n
        stack = []
        has_cycle = [False]

        def dfs(u):
            visited[u] = True
            rec_stack[u] = True
            for v in graph.succ_list[u]:
                if not visited[v]:
                    dfs(v)
                elif rec_stack[v]:
                    has_cycle[0] = True
            rec_stack[u] = False
            stack.append(u)

        for i in range(graph.n):
            if not visited[i] and not has_cycle[0]:
                dfs(i)
        return "Wykryto cykl!" if has_cycle[0] else stack[::-1]

    # 3. Implementacja dla Tabeli krawędzi
    def tarjan_edges():
        visited = [False] * graph.n
        rec_stack = [False] * graph.n
        stack = []
        has_cycle = [False]

        def dfs(u):
            visited[u] = True
            rec_stack[u] = True
            for edge_u, edge_v in graph.edge_list:
                if edge_u == u:
                    if not visited[edge_v]:
                        dfs(edge_v)
                    elif rec_stack[edge_v]:
                        has_cycle[0] = True
            rec_stack[u] = False
            stack.append(u)

        for i in range(graph.n):
            if not visited[i] and not has_cycle[0]:
                dfs(i)
        return "Wykryto cykl!" if has_cycle[0] else stack[::-1]

    # Pobranie wyników ze wszystkich 3 reprezentacji
    res_matrix = tarjan_matrix()
    res_list = tarjan_list()
    res_edges = tarjan_edges()

    return (f"Z macierzy sąsiedztwa: {res_matrix}\n"
            f"Z listy następników:   {res_list}\n"
            f"Z tabeli krawędzi:     {res_edges}")


def kahn_sort(graph):
    """Algorytm Kahna (przeszukiwanie wszerz i stopnie wejściowe) zrealizowany dla 3 reprezentacji."""
    if graph.n == 0: 
        return "Graf jest pusty."

    # 1. Implementacja dla Macierzy sąsiedztwa
    def kahn_matrix():
        in_degree = [0] * graph.n
        # Obliczanie stopni wejściowych
        for i in range(graph.n):
            for j in range(graph.n):
                if graph.adj_matrix[i][j] == 1:
                    in_degree[j] += 1
        
        queue = deque([i for i in range(graph.n) if in_degree[i] == 0])
        result = []
        
        while queue:
            u = queue.popleft()
            result.append(u)
            # Zmniejszanie stopni wejściowych dla sąsiadów
            for v in range(graph.n):
                if graph.adj_matrix[u][v] == 1:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        queue.append(v)
                        
        return "Wykryto cykl!" if len(result) != graph.n else result

    # 2. Implementacja dla Listy następników
    def kahn_list():
        in_degree = [0] * graph.n
        # Obliczanie stopni wejściowych
        for u in range(graph.n):
            for v in graph.succ_list[u]:
                in_degree[v] += 1
        
        queue = deque([i for i in range(graph.n) if in_degree[i] == 0])
        result = []
        
        while queue:
            u = queue.popleft()
            result.append(u)
            # Zmniejszanie stopni wejściowych dla sąsiadów
            for v in graph.succ_list[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
                    
        return "Wykryto cykl!" if len(result) != graph.n else result

    # 3. Implementacja dla Tabeli krawędzi
    def kahn_edges():
        in_degree = [0] * graph.n
        # Obliczanie stopni wejściowych
        for _, v in graph.edge_list:
            in_degree[v] += 1
            
        queue = deque([i for i in range(graph.n) if in_degree[i] == 0])
        result = []
        
        while queue:
            u = queue.popleft()
            result.append(u)
            # Zmniejszanie stopni wejściowych dla sąsiadów
            for edge_u, edge_v in graph.edge_list:
                if edge_u == u:
                    in_degree[edge_v] -= 1
                    if in_degree[edge_v] == 0:
                        queue.append(edge_v)
                        
        return "Wykryto cykl!" if len(result) != graph.n else result

    # Pobranie wyników ze wszystkich 3 reprezentacji
    res_matrix = kahn_matrix()
    res_list = kahn_list()
    res_edges = kahn_edges()

    return (f"Z macierzy sąsiedztwa: {res_matrix}\n"
            f"Z listy następników:   {res_list}\n"
            f"Z tabeli krawędzi:     {res_edges}")