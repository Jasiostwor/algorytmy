import time

def insertion_sort(data):
    arr = data.copy()
    n = len(arr)
    
    start_time = time.perf_counter()
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
    end_time = time.perf_counter()
    total_time = end_time - start_time
    
    return arr, total_time