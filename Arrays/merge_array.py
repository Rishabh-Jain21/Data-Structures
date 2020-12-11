def merge(arr1, arr2):
    arr1.sort()
    arr2.sort()

    new = [None for i in range(len(arr1)+len(arr2))]

    ind = 0
    i = 0
    j = 0
    while(i < len(arr1) and j < len(arr2)):
        if arr1[i] < arr2[j]:
            new[ind] = arr1[i]
            i = i+1
            ind = ind+1
        else:
            new[ind] = arr2[j]
            j = j+1
            ind += 1
    while i < len(arr1):
        new[ind] = arr1[i]
        i = i+1
        ind = ind+1
    while j < len(arr2):
        new[ind] = arr2[j]
        j = j+1
        ind = ind+1

    return new


print(merge([1, 2, 11, 17, 19, 41, 25], [6, 7, 8, 9, 14, 88, 99, 10]))
