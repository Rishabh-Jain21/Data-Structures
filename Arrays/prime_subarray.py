def prime(n):
    for i in range(2, n):
        if n == 2:
            return True
        if n % i == 0:
            return False
    return True


def subarray(arr):
    arr.append(0)
    output = []
    count = 0
    for i in arr:
        if (i != 1 and prime(i) == True):
            output.append(i)
        else:
            print(output)
            l = len(output)
            count = count+(l*(l+1))//2
            output = []
    return count


print(subarray([1, 2, 3, 4, 5, 6, 7, 8, 9]))
