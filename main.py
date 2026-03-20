import tkinter as tk
from tkinter import messagebox

from test_data import DataGenerator

# Import algorytmów (musisz je dostosować do nowego formatu - instrukcja poniżej)
from insertion_sort import insertion_sort
from shell_sort import shell_sort
from selection_sort import selection_sort
from heap_sort import heap_sort
from quick_sort_lp import quick_sort_left_pivot
from quick_sort_rp import quick_sort_random_pivot

class SortingTesterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tester Algorytmów Sortowania")
        self.root.geometry("600x750")

        self.create_widgets()

    def create_widgets(self):
        # --- SEKCJA: ROZMIAR DANYCH (N) ---
        tk.Label(self.root, text="Podaj ilość elementów (n):", font=("Arial", 10, "bold")).pack(pady=(10, 0))
        self.n_entry = tk.Entry(self.root, width=15, justify="center")
        self.n_entry.insert(0, "1000") # Domyślna wartość
        self.n_entry.pack(pady=5)

        # --- SEKCJA: GOTOWE ZESTAWY DANYCH ---
        tk.Label(self.root, text="Wybierz gotowy zestaw danych:").pack()
        data_frame = tk.Frame(self.root)
        data_frame.pack(pady=5)

        tk.Button(data_frame, text="Losowe", command=lambda: self.load_data("random")).grid(row=0, column=0, padx=5)
        tk.Button(data_frame, text="Rosnące", command=lambda: self.load_data("ascending")).grid(row=0, column=1, padx=5)
        tk.Button(data_frame, text="Malejące", command=lambda: self.load_data("descending")).grid(row=0, column=2, padx=5)
        tk.Button(data_frame, text="Stałe", command=lambda: self.load_data("constant")).grid(row=0, column=3, padx=5)
        tk.Button(data_frame, text="A-kształtne", command=lambda: self.load_data("a_shaped")).grid(row=0, column=4, padx=5)

        # --- SEKCJA: POLE TEKSTOWE NA DANE ---
        tk.Label(self.root, text="Dane wejściowe:", font=("Arial", 10, "bold")).pack(pady=(10, 0))
        self.input_text = tk.Text(self.root, height=5, width=70)
        self.input_text.pack(pady=5)

        # --- SEKCJA: WYBÓR ALGORYTMU ---
        tk.Label(self.root, text="Wybierz algorytm do testu:", font=("Arial", 10, "bold")).pack(pady=(15, 0))
        algo_frame = tk.Frame(self.root)
        algo_frame.pack(pady=5)

        tk.Button(algo_frame, text="Insertion Sort", width=15, command=lambda: self.run_test("insertion")).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(algo_frame, text="Shell Sort", width=15, command=lambda: self.run_test("shell")).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(algo_frame, text="Selection Sort", width=15, command=lambda: self.run_test("selection")).grid(row=0, column=2, padx=5, pady=5)
        tk.Button(algo_frame, text="Heap Sort", width=15, command=lambda: self.run_test("heap")).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(algo_frame, text="Quick Sort (Left)", width=15, command=lambda: self.run_test("qsl")).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(algo_frame, text="Quick Sort (Rand)", width=15, command=lambda: self.run_test("qsr")).grid(row=1, column=2, padx=5, pady=5)

        # --- SEKCJA: DANE POSORTOWANE ---
        tk.Label(self.root, text="Posortowane dane:", font=("Arial", 10, "bold")).pack(pady=(5, 0))
        self.output_text = tk.Text(self.root, height=5, width=70, state=tk.DISABLED)
        self.output_text.pack(pady=5)

        # --- SEKCJA: CZAS WYKONANIA ---
        tk.Label(self.root, text="Czas wykonania:", font=("Arial", 10, "bold")).pack(pady=(10, 0))
        self.time_text = tk.Text(self.root, height=2, width=70, state=tk.DISABLED, bg="#202020", fg="#00FF00", font=("Arial", 12, "bold"))
        self.time_text.pack(pady=5)

    def load_data(self, dataset_type):
        """Pobiera N z pola, generuje dane i wrzuca je do okna."""
        try:
            n = int(self.n_entry.get().strip())
            if n <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Błąd", "Podaj poprawną, dodatnią liczbę całkowitą w polu 'n'.")
            return

        # Zabezpieczenie przed zawieszeniem interfejsu przy ogromnych liczbach
        if n > 15000:
            messagebox.showwarning("Uwaga", "Dla n > 15000 interfejs graficzny może chwilę 'zamyślić się' przy wyświetlaniu danych w polu tekstowym.")

        data = []
        if dataset_type == "random":
            data = DataGenerator.get_random(n)
        elif dataset_type == "ascending":
            data = DataGenerator.get_ascending(n)
        elif dataset_type == "descending":
            data = DataGenerator.get_descending(n)
        elif dataset_type == "constant":
            data = DataGenerator.get_constant(n)
        elif dataset_type == "a_shaped":
            data = DataGenerator.get_a_shaped(n)

        self.input_text.delete(1.0, tk.END)
        self.input_text.insert(tk.END, " ".join(map(str, data)))

    def get_input_data(self):
        raw_data = self.input_text.get(1.0, tk.END).strip()
        raw_data = raw_data.replace(',', ' ')
        try:
            return [int(x) for x in raw_data.split()]
        except ValueError:
            messagebox.showerror("Błąd danych", "Upewnij się, że w polu tekstowym są tylko liczby całkowite.")
            return None

    def run_test(self, algo_name):
        original_data = self.get_input_data()
        if not original_data:
            return

        sorted_result = []
        time_taken = 0.0

        try:
            # Algorytmy teraz zwracają tylko krotkę: (posortowana_tablica, calkowity_czas)
            if algo_name == "insertion":
                sorted_result, time_taken = insertion_sort(original_data)
            elif algo_name == "shell":
                sorted_result, time_taken = shell_sort(original_data)
            elif algo_name == "selection":
                sorted_result, time_taken = selection_sort(original_data)
            elif algo_name == "heap":
                sorted_result, time_taken = heap_sort(original_data)
            elif algo_name == "qsl":
                sorted_result, time_taken = quick_sort_left_pivot(original_data)
            elif algo_name == "qsr":
                sorted_result, time_taken = quick_sort_random_pivot(original_data)
                
            self.display_results(sorted_result, time_taken)
            
        except RecursionError:
            messagebox.showerror("Błąd rekurencji", "Przekroczono limit rekurencji dla tego algorytmu i zestawu danych.")
        except Exception as e:
            messagebox.showerror("Błąd", f"Wystąpił błąd podczas sortowania: {e}")

    def display_results(self, sorted_data, time_taken):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, " ".join(map(str, sorted_data)))
        self.output_text.config(state=tk.DISABLED)

        self.time_text.config(state=tk.NORMAL)
        self.time_text.delete(1.0, tk.END)
        self.time_text.insert(tk.END, f" {time_taken:.6f} sekund")
        self.time_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = SortingTesterApp(root)
    root.mainloop()