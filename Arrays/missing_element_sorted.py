def single_duplicate(arr):
    arr.sort()

    i = 0
    diff = arr[0]
    while(i < len(arr)):
        if((arr[i]-i) != diff):
            return i+diff
        i += 1


def multiple_duplicate(arr):
    arr.sort()
    i = 0
    diff = arr[0]
    while(i < len(arr)):
        if((arr[i]-i) != diff):
            while(diff < (arr[i]-i)):
                print(i+diff)
                diff += 1

        i += 1


#print(single_duplicate([1, 2, 3, 7, 9, 8, 4, 6, 5, 0, 11, 13, 17]))
multiple_duplicate([1, 2, 3, 7, 9, 8, 4, 6, 5, 0, 11, 13, 17])
