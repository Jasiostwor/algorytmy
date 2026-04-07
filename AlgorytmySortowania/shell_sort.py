import time

def shell_sort(data):
    arr = data.copy()
    n = len(arr)
    
    start_time = time.perf_counter()
    
    gaps = []
    k = 0
    while True:
        if k % 2 == 0:
            i = k // 2
            gap = 9 * (4**i - 2**i) + 1
        else:
            i = k // 2 + 2
            gap = 4**i - 3 * (2**i) + 1
            
        if gap >= n:
            break
            
        gaps.append(gap)
        k += 1
    gaps.reverse()

    for gap in gaps:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
            
    end_time = time.perf_counter()
    
    return arr, end_time - start_time