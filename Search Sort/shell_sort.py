def shell_sort(arr):
    sublist = len(arr)//2
    while sublist > 0:
        for start in range(sublist):
            gap_insertion(arr, start, sublist)

        print("after increment: ", sublist)
        print("list is: ", arr)
        sublist = sublist//2
    # return arr


def gap_insertion(arr, start, gap):
    for i in range(start+gap, len(arr), gap):
        currentvalue = arr[i]
        position = i
        while position >= gap and arr[position] > currentvalue:
            arr[position] = arr[position-gap]
            position = position-gap
        arr[position] = currentvalue


arr = [1, 4, 6, 8, 9, 4, 6, 5]
print(shell_sort(arr))
print(arr)
