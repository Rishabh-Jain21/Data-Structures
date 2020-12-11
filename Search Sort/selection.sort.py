def selection(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp

    return arr


def selection_sort(arr):
    for fillslot in range(len(arr)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot+1):
            if arr[location] > arr[positionOfMax]:
                positionOfMax = location

        temp = arr[fillslot]
        arr[fillslot] = arr[positionOfMax]
        arr[positionOfMax] = temp
    return arr


print(selection([4, 5, 6, 1, 2, 4]))
print(selection_sort([4, 5, 6, 1, 2, 4]))
