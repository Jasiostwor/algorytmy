from collections import deque

def tarjan_sort(graph):
    if graph.n == 0: 
        return "Graf jest pusty."

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

    res_matrix = tarjan_matrix()
    res_list = tarjan_list()
    res_edges = tarjan_edges()

    return (f"Z macierzy sąsiedztwa: {res_matrix}\n"
            f"Z listy następników:   {res_list}\n"
            f"Z tabeli krawędzi:     {res_edges}")

def kahn_sort(graph):
    if graph.n == 0: 
        return "Graf jest pusty."

    def kahn_matrix():
        in_degree = [0] * graph.n
        for i in range(graph.n):
            for j in range(graph.n):
                if graph.adj_matrix[i][j] == 1:
                    in_degree[j] += 1
        
        queue = deque([i for i in range(graph.n) if in_degree[i] == 0])
        result = []
        
        while queue:
            u = queue.popleft()
            result.append(u)
            for v in range(graph.n):
                if graph.adj_matrix[u][v] == 1:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        queue.append(v)
                        
        return "Wykryto cykl!" if len(result) != graph.n else result

    def kahn_list():
        in_degree = [0] * graph.n
        for u in range(graph.n):
            for v in graph.succ_list[u]:
                in_degree[v] += 1
        
        queue = deque([i for i in range(graph.n) if in_degree[i] == 0])
        result = []
        
        while queue:
            u = queue.popleft()
            result.append(u)
            for v in graph.succ_list[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
                    
        return "Wykryto cykl!" if len(result) != graph.n else result

    def kahn_edges():
        in_degree = [0] * graph.n
        for _, v in graph.edge_list:
            in_degree[v] += 1
            
        queue = deque([i for i in range(graph.n) if in_degree[i] == 0])
        result = []
        
        while queue:
            u = queue.popleft()
            result.append(u)
            for edge_u, edge_v in graph.edge_list:
                if edge_u == u:
                    in_degree[edge_v] -= 1
                    if in_degree[edge_v] == 0:
                        queue.append(edge_v)
                        
        return "Wykryto cykl!" if len(result) != graph.n else result

    res_matrix = kahn_matrix()
    res_list = kahn_list()
    res_edges = kahn_edges()

    return (f"Z macierzy sąsiedztwa: {res_matrix}\n"
            f"Z listy następników:   {res_list}\n"
            f"Z tabeli krawędzi:     {res_edges}")