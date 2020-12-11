def duplicate(arr):
    arr.sort()
    last_duplicate = None
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1] and arr[i] != last_duplicate:
            print(arr[i])
            last_duplicate = arr[i]


def duplicate_count(arr):
    arr.sort()
    for i in range(len(arr)-1):
        if(arr[i] == arr[i+1]):
            j = i+1
            while(j < len(arr) and arr[j] == arr[i]):
                j += 1
            print(arr[i], j-i)
            i = j-1


duplicate([1, 1, 2, 5, 4, 6, 6, 3, 2, 5, 4])
duplicate_count([1, 1, 2, 5, 4, 6, 6, 3, 2, 5, 4])
