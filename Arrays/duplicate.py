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

def duplicate_count_2(arr):
    """
    duplicate count using two pointers
    """
    arr.sort()
    i=0
    j=0
    while j<len(arr):
        if arr[j]==arr[i]:
            j=j+1
        else:
            if j-i>0:
                print(arr[i], j-i)
            i=j


duplicate([1, 1, 2, 5, 4, 6, 6, 3, 2, 5, 4])
duplicate_count([1, 1, 2, 5, 4, 6, 6, 3, 2, 5, 4])
print()
duplicate_count_2([1, 1, 2, 5, 4, 6, 6, 3, 2, 5, 4])

