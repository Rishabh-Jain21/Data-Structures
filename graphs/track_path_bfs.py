from collections import deque
adj_list = {0: [], 1: [], 2: [], 3: []}


n = len(adj_list)


def solve(source, destination):
    pre = bfs(source)
    return path_construct(source, destination, pre)


def path_construct(source, destination, prev):
    path = []
    at = destination
    while at != None:
        path.append(at)
        at = prev[at]
    # path.append(source)
    path.reverse()
    print(path)
    if path[0] == source:
        return path
    return []


def bfs(source):
    n = len(adj_list)
    visited_bfs = [False for i in range(n)]
    d = deque([source])
    visited_bfs[source] = True
    pre = [None for i in range(n)]
    # pre[source] = source

    while d:
        node = d.popleft()
        neighbours = adj_list[node]
        # print(neighbours)
        for next in neighbours:
            if visited_bfs[next] == False:
                d.append(next)
                visited_bfs[next] = True
                pre[next] = node
    print("Pre", pre)
    return pre


print(solve(0, 3))
