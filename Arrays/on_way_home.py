'''
On way home

you are at top left corner of NxM matrix.Home is situated at bottom right corner.Count number of unique ways to reach home. 
'''


def ways(m, n):

    arr = [[0 for _ in range(n)] for k in range(m)]
    for i in range(n):
        arr[m-1][i] = 1
    for j in range(m):
        arr[j][n-1] = 1
    for i in range(m-2, -1, -1):
        for j in range(n-2, -1, -1):
            arr[i][j] = arr[i][j+1]+arr[i+1][j]
    return arr[0][0]


print(ways(2, 2))
