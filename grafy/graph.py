import random

class Graph:
    def __init__(self):
        self.n = 0
        self.adj_matrix = []
        self.succ_list = {}
        self.edge_list = []

    def generate_random_dag(self, n):
        """Generuje losowy DAG o n wierzchołkach i nasyceniu 50%."""
        self.n = n
        self.adj_matrix = [[0] * n for _ in range(n)]
        
        possible_edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
        max_edges = len(possible_edges)
        target_edges = int(max_edges * 0.5)
        
        selected_edges = random.sample(possible_edges, target_edges)
        
        for u, v in selected_edges:
            self.adj_matrix[u][v] = 1
            
        self._update_representations()
        return f"Wygenerowano losowy DAG: wierzchołków={n}, krawędzi={target_edges}."

    def load_from_text(self, text_input):
        """Wczytuje macierz sąsiedztwa z podanego tekstu."""
        lines = text_input.strip().split('\n')
        matrix = []
        for line in lines:
            if line.strip():
                try:
                    row = list(map(int, line.strip().split()))
                    matrix.append(row)
                except ValueError:
                    return "Błąd: Wprowadź tylko liczby całkowite oddzielone spacją."
        
        if not matrix or any(len(row) != len(matrix) for row in matrix):
            return "Błąd: Nieprawidłowy format. Macierz musi być kwadratowa (N x N)."
            
        self.n = len(matrix)
        self.adj_matrix = matrix
        self._update_representations()
        return f"Pomyślnie wczytano graf o {self.n} wierzchołkach z pola tekstowego."

    def _update_representations(self):
        """Aktualizuje listę następników i tabelę krawędzi."""
        self.succ_list = {i: [] for i in range(self.n)}
        self.edge_list = []
        for i in range(self.n):
            for j in range(self.n):
                if self.adj_matrix[i][j] == 1:
                    self.succ_list[i].append(j)
                    self.edge_list.append((i, j))

    def get_representations_string(self):
        """Zwraca wszystkie reprezentacje w formie tekstu."""
        if self.n == 0:
            return "Graf jest pusty."
            
        res = "--- Macierz sąsiedztwa ---\n"
        for row in self.adj_matrix:
            res += " ".join(map(str, row)) + "\n"
            
        res += "\n--- Lista następników ---\n"
        for u, neighbors in self.succ_list.items():
            res += f"{u}: {neighbors}\n"
            
        res += "\n--- Tabela krawędzi ---\n"
        for u, v in self.edge_list:
            res += f"({u} -> {v})\n"
            
        return res