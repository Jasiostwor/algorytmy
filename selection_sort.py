import time

def selection_sort(data):
    arr = data.copy()
    n = len(arr)
    
    start_time = time.perf_counter()
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    end_time = time.perf_counter()
    
    return arr, end_time - start_time