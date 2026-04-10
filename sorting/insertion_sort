def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        Issort = False
        key = arr[i]
        j = i-1
        
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            arr[j] = key
            j -= 1
            Issort = True
        if not Issort:
            break
    return arr

arr = [12, 11, 13, 5, 6]
print("Sorted array is:", insertion_sort(arr))
