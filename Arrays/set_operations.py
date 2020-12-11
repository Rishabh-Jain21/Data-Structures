def union(arr1, arr2):
    arr1.sort()
    arr2.sort()
    new = [None for _ in range(len(arr1+arr2))]
    i = 0
    j = 0
    k = 0
    while(i < len(arr1) and j < len(arr2)):
        if(arr1[i] < arr2[j]):
            new[k] = arr1[i]
            k += 1
            i += 1
        elif(arr1[i] > arr2[j]):
            new[k] = arr2[j]
            j += 1
            k += 1
        else:
            new[k] = arr1[i]
            i += 1
            j += 1
            k += 1
    while i < len(arr1):
        new[k] = arr1[i]
        i += 1
        k += 1
    while j < len(arr2):
        new[k] = arr2[j]
        j += 1
        k += 1

    while(None in new):
        new.remove(None)
    return new


def difference(arr1, arr2):
    arr1.sort()
    arr2.sort()
    new = [None for _ in range(len(arr1+arr2))]
    i = 0
    j = 0
    k = 0
    while(i < len(arr1) and j < len(arr2)):
        if(arr1[i] < arr2[j]):
            new[k] = arr1[i]
            k += 1
            i += 1
        elif(arr1[i] > arr2[j]):
            j += 1

        else:
            i += 1
            j += 1
            k += 1
    while i < len(arr1):
        new[k] = arr1[i]
        i += 1
        k += 1

    while(None in new):
        new.remove(None)
    return new


def intersection(arr1, arr2):
    arr1.sort()
    arr2.sort()
    new = [None for _ in range(len(arr1+arr2))]
    i = 0
    j = 0
    k = 0
    while(i < len(arr1) and j < len(arr2)):
        if(arr1[i] < arr2[j]):
            i += 1
        elif(arr1[i] > arr2[j]):
            j += 1
        else:
            new[k] = arr1[i]
            i += 1
            j += 1
            k += 1

    while(None in new):
        new.remove(None)
    return new


print(union([1, 2, 3, 7], [1, 2, 4, 5, 6, 7, 9]))
print(intersection([1, 2, 3, 7], [1, 2, 4, 5, 6, 7, 9]))
print(difference([1, 2, 3, 7, 19], [1, 2, 4, 5, 6, 7, 9]))
