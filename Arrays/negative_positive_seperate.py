def seperate(arr):
    i = 0
    j = len(arr)-1
    while(i < j):
        if arr[i] < 0:
            i = i+1
        if arr[j] > 0:
            j = j-1
        if(i < j):
            arr[i], arr[j] = arr[j], arr[i]

    return arr


print(seperate([-1, -2, 1, 2, -3, 4, 5]))
