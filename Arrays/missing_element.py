'''consider an array of non negative sorted integers.A second array is formed by shuffiling elements of first array and deleting a random element.FInd missing element'''

import time


def finder(arr1, arr2):
    for i in arr1:
        if i in arr2:
            arr1.remove(i)
            arr2.remove(i)
        else:
            return i


def finder2(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for i, j in zip(arr1, arr2):
        if i != j:
            return i
    return arr1[-1]


c1 = time.time()


def finder3(arr1, arr2):
    count = {}

    for num in arr1:
        count[num] = count.get(num, 0)+1

    for num in arr2:
        count[num] = count.get(num)-1

    for num in count:
        if count[num] == 1:
            return (num)


arr1 = [1, 2, 3, 4, 5, 6, 5, 7]
arr2 = [3, 7, 2, 1, 4, 6, 5]
print(finder3(arr1, arr2))
print(time.time()-c1)
