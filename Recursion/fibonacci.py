def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def iterative(n):
    a = 0
    b = 1
    for i in range(n):
        temp = b
        b = a+b
        a = temp
    return a

def fib_another(n):
    num = [0, 1]
    for i in range(n):
        num.append(num[-1]+num[-2])

    return num[n]


print(fibonacci(5))
print(iterative(10))

# print(fib_dyn(10))
print(fib_another(10))
