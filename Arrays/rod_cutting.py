def rodcutter(n, cost):
    rod = [0 for _ in range(n+1)]
    for i in range(n+1):
        max_val = 0
        for j in range(1, i):
            max_val = max(max_val, cost[j]+rod[i-j])
        rod[i] = max_val
    print(rod)
    return rod[n]


print(rodcutter(5, [0, 2, 4, 5, 7]))
