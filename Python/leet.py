def qsort(arr, low, high):
    if high <= 0:
        return
    pivot = arr[low]
    i = low+1
    j = high
    while i < high:
        if pivot < arr[i]:
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1
        else:
            i+=1
    arr[j], arr[low] = arr[low], arr[j]
    print(arr)
    qsort(arr, low, j-1)

l = [23,42,13,1,24]
qsort(l, 0, len(l)-1)
print(l)