def quick_sort(arr):
    quick_sort_help(arr, 0, len(arr)-1)


def quick_sort_help(arr, first, last):
    if first < last:
        splitpoint = partition(arr, first, last)
        quick_sort_help(arr, first, splitpoint-1)
        quick_sort_help(arr, splitpoint+1, last)


def partition(arr, first, last):
    pivot_value = arr[first]

    leftmark = first+1
    right_mark = last
    done = False

    while not done:
        while leftmark <= right_mark and arr[leftmark] <= pivot_value:
            leftmark += 1

        while arr[right_mark] >= pivot_value and right_mark >= leftmark:
            right_mark -= 1

        if right_mark < leftmark:
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[right_mark]
            arr[right_mark] = temp

    temp = arr[first]
    arr[first] = arr[right_mark]
    arr[right_mark] = temp

    return right_mark


arr = [2, 5, 4, 6, 7, 3, 1, 4, 12, 11]
quick_sort(arr)
print(arr)
