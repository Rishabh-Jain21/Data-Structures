# Given an array of elements of length N, ranging from 0 to N – 1. All elements may not be present in the array. If the element is not present then there will be -1 present in the array. Rearrange the array such that A[i] = i and if i is not present, display -1 at that place.

def rearrange(lst):
    l = len(lst)
    new_array = [-1]*l
    for i in range(len(lst)):
        if 0 <= lst[i] < len(lst):
            new_array[lst[i]] = lst[i]

    return new_array


def rearrange_2(arr):
    i = 0
    n = len(arr)
    while i < n:
        if (arr[i] >= 0 and arr[i] != i):
            (arr[arr[i]], arr[i]) = (arr[i], arr[arr[i]])
        else:
            i += 1
    return arr


arr_1 = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
arr_2 = [19, 7, 0, 3, 18, 15, 12, 6, 1, 8,
         11, 10, 9, 5, 13, 16, 2, 14, 17, 4]

print(rearrange(arr_2))
print(rearrange_2(arr_1))
