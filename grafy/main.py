import tkinter as tk
from tkinter import scrolledtext, messagebox
from graph import Graph
import traversals
import topological_sort

class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generator i Algorytmy DAG")
        self.root.geometry("700x600")
        
        self.graph = Graph()
        self.create_widgets()

    def create_widgets(self):
        # Panel górny - sterowanie
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=10, fill=tk.X, padx=10)

        tk.Label(control_frame, text="Liczba wierzchołków (n):").grid(row=0, column=0, padx=5, pady=5)
        self.entry_n = tk.Entry(control_frame, width=10)
        self.entry_n.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(control_frame, text="Generuj losowy DAG (50%)", command=self.generate_graph).grid(row=0, column=2, padx=5, pady=5)
        tk.Button(control_frame, text="Wczytaj macierz z pola tekstowego", command=self.load_graph).grid(row=0, column=3, padx=5, pady=5)

        # Panel środkowy - algorytmy i wyświetlanie
        algo_frame = tk.Frame(self.root)
        algo_frame.pack(pady=5, fill=tk.X, padx=10)

        tk.Button(algo_frame, text="Pokaż Reprezentacje", command=self.show_reps).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(algo_frame, text="BFS", command=self.run_bfs).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(algo_frame, text="DFS", command=self.run_dfs).grid(row=0, column=2, padx=5, pady=5)
        tk.Button(algo_frame, text="Tarjan Sort", command=self.run_tarjan).grid(row=0, column=3, padx=5, pady=5)
        tk.Button(algo_frame, text="Kahn Sort", command=self.run_kahn).grid(row=0, column=4, padx=5, pady=5)

        # Panel dolny - pole tekstowe (wejście/wyjście)
        tk.Label(self.root, text="Konsola wyników / Wprowadzanie macierzy:").pack(anchor=tk.W, padx=10)
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=80, height=25)
        self.text_area.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

    def log(self, message):
        """Pomocnicza metoda do wypisywania tekstu do głównego okna."""
        self.text_area.insert(tk.END, message + "\n\n")
        self.text_area.see(tk.END)

    def generate_graph(self):
        try:
            n = int(self.entry_n.get())
            if n <= 0: raise ValueError
            msg = self.graph.generate_random_dag(n)
            self.text_area.delete(1.0, tk.END) # Czyszczenie ekranu
            self.log(msg)
            self.show_reps()
        except ValueError:
            messagebox.showerror("Błąd", "Podaj prawidłową, dodatnią liczbę całkowitą n.")

    def load_graph(self):
        content = self.text_area.get(1.0, tk.END)
        msg = self.graph.load_from_text(content)
        self.text_area.delete(1.0, tk.END)
        self.log(msg)
        if "Pomyślnie" in msg:
            self.show_reps()

    def show_reps(self):
        self.log(self.graph.get_representations_string())

    def run_bfs(self):
        self.log("--- Wynik BFS ---\n" + traversals.bfs(self.graph))

    def run_dfs(self):
        self.log("--- Wynik DFS ---\n" + traversals.dfs(self.graph))

    def run_tarjan(self):
        self.log("--- Sortowanie Tarjana ---\n" + topological_sort.tarjan_sort(self.graph))

    def run_kahn(self):
        self.log("--- Sortowanie Kahna ---\n" + topological_sort.kahn_sort(self.graph))

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()