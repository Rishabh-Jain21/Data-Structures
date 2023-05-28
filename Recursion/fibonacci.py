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

def fibo_dp_mem(n):
    mem = [0, 1]
    for i in range(2, n + 1):
        mem[i % 2] = mem[0] + mem[1]
    return mem[n % 2]



memo_dict=dict()

def fib_memo(n):
    if n in memo_dict:
        return memo_dict[n]
    if n<=2:
        return 1
    memo_dict[n]=fib_memo(n-1)+fib_memo(n-2)
    return memo_dict[n]
print(fibonacci(5))
print(iterative(10))

memo_dict=dict()

def fib_memo_v2(n,dic={}):
    if n in memo_dict:
        return memo_dict[n]
    if n<=2:
        return 1
    dic[n]=fib_memo_v2(n-1,dic)+fib_memo_v2(n-2,dic)
    return dic[n]
print(fibonacci(5))
print(iterative(10))

# print(fib_dyn(10))
print(fib_another(15))
# print(fibo_dp_mem(4))
print(fib_memo(10))
print(fib_memo_v2(15))
