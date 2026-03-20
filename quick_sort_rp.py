import time
import random
import sys

sys.setrecursionlimit(200000)

def _partition_rp(arr, low, high):
    rand_idx = random.randint(low, high)
    arr[low], arr[rand_idx] = arr[rand_idx], arr[low]
    
    pivot = arr[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

def _quick_sort_rp_recursive(arr, low, high):
    if low < high:
        pi = _partition_rp(arr, low, high)
        _quick_sort_rp_recursive(arr, low, pi - 1)
        _quick_sort_rp_recursive(arr, pi + 1, high)

def quick_sort_random_pivot(data):
    arr = data.copy()
    n = len(arr)
    
    start_time = time.perf_counter()
    
    if n > 1:
        _quick_sort_rp_recursive(arr, 0, n - 1)
        
    end_time = time.perf_counter()
    
    return arr, end_time - start_time