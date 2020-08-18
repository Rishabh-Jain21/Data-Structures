def sum1(n):
    '''
        546 -> 5+4+6
        123 -> 1+2+3
    '''
    if n > 0:
        return n % 10+sum(n//10)
    return 0


def sum2(n):
    """
    4 -> 4+3+2+1
    7 -> 7+6+5+4+3+2+1
    """
    if n == 0:
        return 0
    else:
        return n+sum2(n-1)


print(sum1(4))
print(sum2(4))
