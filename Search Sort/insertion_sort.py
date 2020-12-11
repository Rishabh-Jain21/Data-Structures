def insertion(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        position = i
        while position > 0 and arr[position-1] > current:
            arr[position] = arr[position-1]
            position = position-1

        arr[position] = current

    return arr


print(insertion([1, 4, 8, 6, 2]))
