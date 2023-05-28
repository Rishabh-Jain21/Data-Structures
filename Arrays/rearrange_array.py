""" Given an array of elements of length N, ranging from 0 to N 
    1. All elements may not be present in the array. 
    If the element is not present then there will be -1 present in the array. 
    Rearrange the array such that A[i] = i and if i is not present, display -1 at that place.
"""
def rearrange(lst):
    """
    Creating a new array containing of all -1.
    iterate over given array and if non negative index is found , populate the indx in new array
    
    Space COmplexity O(n)
    Time complexity O(n)
    """
    l = len(lst)
    new_array = [-1]*l
    for i in range(len(lst)):
        if 0 <= lst[i] < len(lst):
            new_array[lst[i]] = lst[i]

    return new_array


def rearrange_2(arr):
    """
    Swap the element of current index with the value present at the index of the current value ,until correct element is placed or negative value is found.
    then move to next index and repeat above process
    
    Space Complexity O(1)
    Time Complexity O(n)
    
    """
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
