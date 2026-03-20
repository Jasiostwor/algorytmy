import time
import sys
import random

sys.setrecursionlimit(200000)

def _partition_rp(arr, p, r):
    x = arr[random.randint(p, r)]
    i = p - 1
    j = r + 1
    
    while True:
        i += 1
        while arr[i] < x:
            i += 1
            
        j -= 1
        while arr[j] > x:
            j -= 1
            
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

def _quick_sort_rp_recursive(arr, p, r):
    if p < r:
        q = _partition_rp(arr, p, r)
        _quick_sort_rp_recursive(arr, p, q)
        _quick_sort_rp_recursive(arr, q + 1, r)

def quick_sort_random_pivot(data):
    arr = data.copy()
    n = len(arr)
    
    start_time = time.perf_counter()
    
    if n > 1:
        _quick_sort_rp_recursive(arr, 0, n - 1)
        
    end_time = time.perf_counter()
    
    return arr, end_time - start_time