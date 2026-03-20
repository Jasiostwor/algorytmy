import time

def insertion_sort(data):
    # Kopiujemy dane, żeby nie nadpisywać oryginału z pola tekstowego
    arr = data.copy()
    n = len(arr)
    
    # Odpalamy stoper
    start_time = time.perf_counter()
    
    # --- Właściwe sortowanie ---
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    # ---------------------------
        
    # Zatrzymujemy stoper
    end_time = time.perf_counter()
    
    # Obliczamy czas całkowity
    total_time = end_time - start_time
    
    # Zwracamy posortowaną tablicę i jeden czas
    return arr, total_time