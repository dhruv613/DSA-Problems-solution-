def partition(arr, l, r):
    key = arr[r]
    start = l 

    for i in range(l, r):
        if arr[i] < key:
            temp = arr[i]
            arr[i] = arr[start]
            arr[start] = temp
            start += 1

    temp = arr[start]
    arr[start] = arr[r]

    return start

def quick_sort(arr, l, r):  # noqa: E741
    if l >= r: 
        return 
    
    p  = partition(arr, l , r)
    quick_sort(arr, l, p - 1)
    quick_sort(arr, p+1, r)
    

def sort(arr):

    quick_sort(arr, 0, len(arr)-1)

    return arr

arr = [10, 7, 8, 9, 1, 5]

print("Sorted array is:", sort(arr))