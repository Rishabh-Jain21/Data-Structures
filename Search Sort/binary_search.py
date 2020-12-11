def binary_search(arr, ele):
    first = 0
    last = len(arr)-1
    found = False

    while first <= last and not found:

        mid = (first+last)//2

        if arr[mid] == ele:
            found = True
        else:
            if arr[mid] > ele:
                last = mid-1
            else:
                first = mid+1

    return found


def binary_search_recursive(arr, ele):
    if(len(arr) == 0):
        return False

    else:
        mid = len(arr)//2

        if arr[mid] == ele:
            return True
        else:
            if ele < arr[mid]:
                return binary_search_recursive(arr[:mid], ele)
            else:
                return binary_search_recursive(arr[mid:], ele)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search_recursive(arr, 10))
print(binary_search(arr, 10))
