import time

def shell_sort(data):
    arr = data.copy()
    n = len(arr)
    
    start_time = time.perf_counter()
    
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
        
    end_time = time.perf_counter()
    
    return arr, end_time - start_time