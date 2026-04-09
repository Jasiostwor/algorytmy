import tkinter as tk
from tkinter import messagebox, scrolledtext, Canvas, Toplevel # NOWY IMPORT
import random
import time
import sys
import math # NOWY IMPORT

from node import Node
from avl import create_avl
from bst import build_degenerate_bst
from search import get_min_path, get_max_path
from traversal import get_inorder, get_preorder
from delete import delete_node, delete_tree_postorder
from dsw import dsw_balance
from printer import print_tree

sys.setrecursionlimit(25000)

class TreeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drzewa AVL i BST - Panel Sterowania")
        self.root.geometry("850x700")
        
        self.current_data = []
        self.avl_root = None
        self.avl_height = None
        self.bst_root = None
        self.bst_height = None

        self.setup_ui()

    def setup_ui(self):
        control_frame = tk.Frame(self.root, width=350, padx=10, pady=10)
        control_frame.pack(side=tk.LEFT, fill=tk.Y)
        
        # 1. Dane wejściowe
        tk.Label(control_frame, text="Dane wejściowe (n <= 1000)", font=("Arial", 10, "bold")).pack(anchor=tk.W, pady=(0, 5))
        tk.Label(control_frame, text="Podaj liczby (np. 1, 3, 5):").pack(anchor=tk.W)
        self.manual_input = tk.Entry(control_frame, width=30)
        self.manual_input.pack(fill=tk.X, pady=(0, 5))
        tk.Button(control_frame, text="Zbuduj z wpisanych", command=self.build_from_manual).pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(control_frame, text="Albo wygeneruj losowe n-elementów:").pack(anchor=tk.W)
        self.n_input = tk.Entry(control_frame, width=10)
        self.n_input.insert(0, "10")
        self.n_input.pack(anchor=tk.W, pady=(0, 5))
        tk.Button(control_frame, text="Generuj i Zbuduj", command=self.build_from_generator).pack(fill=tk.X, pady=(0, 10))
        
        tk.Frame(control_frame, height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, pady=10)
        
        # 2. Operacje
        tk.Label(control_frame, text="Operacje na drzewach", font=("Arial", 10, "bold")).pack(anchor=tk.W, pady=(0, 5))
        tk.Button(control_frame, text="1. Min/Max i ścieżka", command=self.find_min_max).pack(fill=tk.X, pady=2)
        tk.Button(control_frame, text="2. Wypisz In-order i Pre-order", command=self.print_orders).pack(fill=tk.X, pady=2)
        
        # NOWE PRZYCISKI:
        tk.Button(control_frame, text="2.5. Pokaż strukturę drzew (ASCII - Konsola)", command=self.show_trees_ascii).pack(fill=tk.X, pady=2)
        tk.Button(control_frame, text="2.6. Pokaż strukturę drzew (GRAFICZNA - Nowe okno)", bg="lightgreen", command=self.show_trees_graph).pack(fill=tk.X, pady=2)
        
        tk.Button(control_frame, text="3. Usuń całe drzewo (Post-order)", command=self.delete_whole_trees).pack(fill=tk.X, pady=2)
        tk.Button(control_frame, text="4. Równoważenie BST (DSW)", command=self.balance_dsw).pack(fill=tk.X, pady=2)
        
        delete_frame = tk.Frame(control_frame)
        delete_frame.pack(fill=tk.X, pady=10)
        tk.Label(delete_frame, text="Klucze do usunięcia (po przecinku):").pack(anchor=tk.W)
        self.delete_input = tk.Entry(delete_frame, width=30)
        self.delete_input.pack(fill=tk.X, pady=(0, 5))
        tk.Button(delete_frame, text="Usuń podane węzły", command=self.delete_nodes).pack(fill=tk.X)

        tk.Frame(control_frame, height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, pady=10)

        # 3. Testy
        tk.Label(control_frame, text="Pomiary i testy", font=("Arial", 10, "bold")).pack(anchor=tk.W, pady=(0, 5))
        tk.Button(control_frame, text="Uruchom testy wydajnościowe", bg="lightblue", command=self.run_tests).pack(fill=tk.X)

        # 4. Konsola
        output_frame = tk.Frame(self.root, padx=10, pady=10)
        output_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        tk.Label(output_frame, text="Wyniki operacji:", font=("Arial", 10, "bold")).pack(anchor=tk.W)
        
        # WAŻNE: Tu ustawiamy monospaced font dla konsoli w GUI
        self.console = scrolledtext.ScrolledText(output_frame, wrap=tk.NONE, font=("Consolas", 10))
        self.console.pack(fill=tk.BOTH, expand=True)

    def log(self, message):
        self.console.insert(tk.END, message + "\n")
        self.console.see(tk.END)

    def clear_log(self):
        self.console.delete('1.0', tk.END)

    def build_from_manual(self):
        self.clear_log()
        raw_data = self.manual_input.get()
        try:
            elements = [int(x.strip()) for x in raw_data.split(',')]
            if len(elements) > 1000:
                messagebox.showerror("Błąd", "Max 1000 elementów.")
                return
            self.current_data = sorted(list(set(elements)))
            self.log(f"Wczytano i posortowano dane: {self.current_data}")
            self.construct_trees()
        except ValueError:
            messagebox.showerror("Błąd", "Wprowadź poprawne liczby oddzielone przecinkami.")

    def build_from_generator(self):
        self.clear_log()
        try:
            n = int(self.n_input.get())
            if n > 1000 or n <= 0:
                messagebox.showerror("Błąd", "Wartość n z przedziału 1 do 1000.")
                return
            self.current_data = sorted(random.sample(range(1, 100), n))
            self.log(f"Wygenerowano dane: {self.current_data}")
            self.construct_trees()
        except ValueError:
            messagebox.showerror("Błąd", "Wprowadź poprawną liczbę dla n.")

    def construct_trees(self):
        self.log("\n--- Budowanie drzew ---")
        self.avl_root, tmp = create_avl(self.current_data.copy())
        self.log("Stworzono drzewo AVL (metodą połowienia binarnego). Wysokość AVL: " + str(tmp))
        
        self.bst_root, self.bst_height = build_degenerate_bst(self.current_data)
        self.log(f"Drzewo BST (zdegenerowane) gotowe. Wysokość: {self.bst_height}")

    def find_min_max(self):
        if not self.avl_root or not self.bst_root:
            messagebox.showwarning("Uwaga", "Brak drzew.")
            return
        self.log("\n--- Ścieżki Min/Max ---")
        min_path_avl = get_min_path(self.avl_root)
        max_path_avl = get_max_path(self.avl_root)
        self.log(f"AVL Min: {min_path_avl[-1]} | Ścieżka: {' -> '.join(min_path_avl)}")
        self.log(f"AVL Max: {max_path_avl[-1]} | Ścieżka: {' -> '.join(max_path_avl)}")
        
        min_path_bst = get_min_path(self.bst_root)
        max_path_bst = get_max_path(self.bst_root)
        self.log(f"BST (zdeg.) Min: {min_path_bst[-1]} | Ścieżka: {' -> '.join(min_path_bst)}")
        self.log(f"BST (zdeg.) Max: {max_path_bst[-1]} | Ścieżka: {' -> '.join(max_path_bst)}")

    def print_orders(self):
        if not self.avl_root: return
        self.log("\n--- Wypisywanie In-order i Pre-order ---")
        
        in_res_avl, pre_res_avl = [], []
        get_inorder(self.avl_root, in_res_avl)
        get_preorder(self.avl_root, pre_res_avl)
        self.log(f"AVL In-order:  {' '.join(in_res_avl)}")
        self.log(f"AVL Pre-order: {' '.join(pre_res_avl)}")

        if self.bst_root:
            in_res_bst, pre_res_bst = [], []
            get_inorder(self.bst_root, in_res_bst)
            get_preorder(self.bst_root, pre_res_bst)
            self.log(f"BST In-order:  {' '.join(in_res_bst)}")
            self.log(f"BST Pre-order: {' '.join(pre_res_bst)}")

    def show_trees_ascii(self):
        """Metoda wywołująca ulepszony ASCII printer w konsoli."""
        if not self.avl_root and not self.bst_root:
            messagebox.showwarning("Uwaga", "Brak drzew.")
            return
            
        self.log("\n" + "="*50)
        self.log("STRUKTURA DRZEW (ASCII - Konsola, monospaced font)")
        self.log("="*50)
        
        # Blokada dla n > 50 dla konsoli, żeby jej nie zapchać
        if len(self.current_data) > 50:
             messagebox.showinfo("Informacja", "Dla n > 50 ASCII w konsoli jest nieczytelny. Polecam widok graficzny.")
             return

        if self.avl_root:
            self.log("\n--- DRZEWO AVL (Top-down view) ---")
            lines = print_tree(self.avl_root)
            for line in lines:
                self.log(line)
        
        if self.bst_root:
            self.log("\n--- DRZEWO BST (Zdegenerowane) ---")
            lines = print_tree(self.bst_root)
            for line in lines:
                self.log(line)

    def show_trees_graph(self):
        """NOWA METODA: Graficzny widok drzew w nowym oknie."""
        if not self.avl_root and not self.bst_root:
            messagebox.showwarning("Uwaga", "Brak drzew.")
            return
            
        # Blokada dla n > 200 dla grafiki, żeby uniknąć zacięcia
        if len(self.current_data) > 200:
             messagebox.showinfo("Informacja", "Graficzny widok wyłączony dla n > 200 dla zachowania płynności.")
             return

        # Tworzymy nowe okno
        tree_window = Toplevel(self.root)
        tree_window.title("Graficzna struktura drzew")
        tree_window.geometry("1000x800")
        
        # Kanwa do rysowania
        canvas = Canvas(tree_window, bg="white")
        canvas.pack(fill=tk.BOTH, expand=True)
        
        frame = tk.Frame(canvas)
        canvas.create_window((0,0), window=frame, anchor="nw")
        
        frame_width = 1800 if len(self.current_data) > 50 else 1000
        frame_height = 1000 if len(self.current_data) > 50 else 800
        canvas.config(scrollregion=(0, 0, frame_width, frame_height))
        
        hbar = tk.Scrollbar(tree_window, orient=tk.HORIZONTAL, command=canvas.xview)
        hbar.pack(side=tk.BOTTOM, fill=tk.X)
        canvas.config(xscrollcommand=hbar.set)
        
        vbar = tk.Scrollbar(tree_window, orient=tk.VERTICAL, command=canvas.yview)
        vbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.config(yscrollcommand=vbar.set)

        if self.avl_root:
            self.log("\n--- Rysowanie widoku graficznego (AVL) ---")
            tk.Label(canvas, text="DRZEWO AVL", font=("Arial", 12, "bold"), bg="white", fg="blue").pack(pady=10)
            self._draw_node(canvas, self.avl_root, x=frame_width//2, y=60, dx=frame_width//4, color="lightblue")
            
        if self.bst_root:
             self.log("--- Rysowanie widoku graficznego (BST) ---")
             tk.Label(canvas, text="DRZEWO BST (zdegenerowane/DSW)", font=("Arial", 12, "bold"), bg="white", fg="red").pack(pady=10)
             # Rysujemy niżej
             offset_y = 600
             self._draw_node(canvas, self.bst_root, x=frame_width//2, y=offset_y, dx=frame_width//4, color="salmon")

    def _draw_node(self, canvas, node, x, y, dx, color, level=1):
        """Pomocnicza funkcja rysująca węzeł i jego dzieci graficznie."""
        if node is None: return
        
        r = 20 # promień koła
        
        # Prawa linia (idzie do góry w widoku graficznym) -> Nie, to jest top-down view.
        # Prawa strona graficznie rysowana na prawo
        if node.right:
             line_color = "gray"
             canvas.create_line(x, y, x + dx, y + 100, fill=line_color, width=2)
             self._draw_node(canvas, node.right, x + dx, y + 100, dx//2, color, level+1)
        
        # Lewa linia graficznie rysowana na lewo
        if node.left:
             line_color = "gray"
             canvas.create_line(x, y, x - dx, y + 100, fill=line_color, width=2)
             self._draw_node(canvas, node.left, x - dx, y + 100, dx//2, color, level+1)
             
        # Sam węzeł (kółko) - rysujemy na wierzchu linii
        canvas.create_oval(x-r, y-r, x+r, y+r, fill=color, outline="black", width=2)
        canvas.create_text(x, y, text=str(node.value), font=("Arial", 10, "bold"), fill="black")

    def delete_nodes(self):
        if not self.avl_root: return
        raw_keys = self.delete_input.get()
        try:
            keys = [int(x.strip()) for x in raw_keys.split(',')]
            self.log(f"\n--- Usuwanie węzłów: {keys} ---")
            for key in keys:
                self.avl_root = delete_node(self.avl_root, key)
                self.bst_root = delete_node(self.bst_root, key)
                self.log(f"Usunięto klucz: {key}")
        except ValueError:
             messagebox.showerror("Błąd", "Błędne klucze.")

    def delete_whole_trees(self):
        if not self.avl_root: return
        self.log("\n--- Usuwanie metodą Post-order ---")
        self.avl_root = delete_tree_postorder(self.avl_root)
        self.bst_root = delete_tree_postorder(self.bst_root)
        self.log("Zakończono. Obiekty drzew ustawiono na None.")

    def balance_dsw(self):
        if not self.bst_root: return
        from bst import get_height_after
        self.log("\n--- Równoważenie algorytmem DSW (Drzewo zdegenerowane) ---")
        self.bst_root = dsw_balance(self.bst_root)
        self.bst_height = get_height_after(self.bst_root)
        self.log(f"Drzewo zrównoważone pomyślnie. Nowa wysokość: {self.bst_height}")

    def run_tests(self):
        self.clear_log()
        self.log("--- TESTY WYDAJNOŚCIOWE ---")
        n_values = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
        
        for n in n_values:
            test_data = sorted(random.sample(range(1, n * 10), n))
            self.log(f"\n[ n = {n} ]")
            
            start = time.perf_counter()
            test_avl, _ = create_avl(test_data)
            time_avl = time.perf_counter() - start
            self.log(f"  Tworzenie AVL:        {time_avl:.6f} s")
            
            start = time.perf_counter()
            test_bst, _ = build_degenerate_bst(test_data)
            time_bst = time.perf_counter() - start
            self.log(f"  Tworzenie BST (zdeg): {time_bst:.6f} s")
            
            start = time.perf_counter()
            get_max_path(test_avl)
            time_max_avl = time.perf_counter() - start
            self.log(f"  Szukanie MAX (AVL):   {time_max_avl:.6f} s")
            
            start = time.perf_counter()
            get_max_path(test_bst)
            time_max_bst = time.perf_counter() - start
            self.log(f"  Szukanie MAX (BST):   {time_max_bst:.6f} s")
            
            start = time.perf_counter()
            dummy = []
            get_inorder(test_avl, dummy)
            time_inorder = time.perf_counter() - start
            self.log(f"  In-order (AVL):       {time_inorder:.6f} s")
            
            start = time.perf_counter()
            test_bst = dsw_balance(test_bst)
            time_dsw = time.perf_counter() - start
            self.log(f"  DSW (na BST):         {time_dsw:.6f} s")
            
            delete_tree_postorder(test_avl)
            delete_tree_postorder(test_bst)

if __name__ == "__main__":
    root = tk.Tk()
    app = TreeApp(root)
    root.mainloop()