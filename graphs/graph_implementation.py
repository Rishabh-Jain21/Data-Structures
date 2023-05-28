from collections import deque
adj = [[0, 1, 1, 1],
       [1, 0, 0, 1],
       [1, 1, 0, 0],
       [0, 1, 0, 0]]
n = len(adj)
visited_adj_mat = [False for i in range(n)]
adj_list = {}
for i in range(n):
    adj_list[i] = [j for j in range((n)) if adj[i][j] != 0]

# print(adj_list)


def dfs(source):
    if visited_adj_mat[source]:
        return
    visited_adj_mat[source] = True
    # print(source)

    for i in range(n):
        if adj[source][i] != 0:
            dfs(i)


visited_adj = [False for i in range(n)]

count = [0]


def dfs_adja(source):
    if visited_adj[source]:
        return 1
    visited_adj[source] = True
    # print(source)
    count[0] = count[0]+1

    for i in adj_list[source]:

        return 1+dfs_adja(i)


# dfs(0)
# print("**********")
# print(dfs_adja(0))

print(adj_list)


def bfs(source):
    visited_bfs = [False for i in range(n)]
    d = deque([source])
    visited_bfs[source] = True
    print(source, end="->")

    while d:
        node = d.popleft()
        neighbours = adj_list[node]
        # print(neighbours)
        for next in neighbours:
            if visited_bfs[next] == False:
                visited_bfs[next] = True
                print(next, end="->")
                d.append(next)


bfs(0)
