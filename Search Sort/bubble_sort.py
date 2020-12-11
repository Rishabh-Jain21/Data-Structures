def bubble(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


def bubble2(arr):
    for n in range(len(arr)-1, 0, -1):
        for j in range(n):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


print(bubble2([4, 7, 2, 6, 5]))
print(bubble([4, 7, 5, 3, 2]))
