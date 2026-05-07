from collections import deque

def bfs(graph):
    """Przechodzenie wszerz (BFS)."""
    if graph.n == 0: 
        return "Graf jest pusty."
    
    visited = [False] * graph.n
    result = []
    
    for start_node in range(graph.n):
        if not visited[start_node]:
            queue = deque([start_node])
            visited[start_node] = True
            
            while queue:
                u = queue.popleft()
                result.append(str(u))
                
                for v in graph.succ_list[u]:
                    if not visited[v]:
                        visited[v] = True
                        queue.append(v)
                        
    return " ".join(result)

def dfs(graph):
    """Przechodzenie w głąb (DFS)."""
    if graph.n == 0: 
        return "Graf jest pusty."
    
    visited = [False] * graph.n
    result = []
    
    def dfs_visit(u):
        visited[u] = True
        result.append(str(u))
        
        for v in graph.succ_list[u]:
            if not visited[v]:
                dfs_visit(v)
                
    for start_node in range(graph.n):
        if not visited[start_node]:
            dfs_visit(start_node)
            
    return " ".join(result)