from collections import deque

# 전역변수
edges = list()

# DFS
def dfs(s, visited):
    if visited[s] > 0:
        return

    print(s, end=' ')
    visited[s] = 1
    next_nodes = edges[s]
    for next_node, connected in enumerate(next_nodes):
        if visited[next_node] > 0 or connected == 0:
            continue

        dfs(next_node, visited)


# BFS
def bfs(s, visited):
    q = deque()
    q.append(s)

    while len(q) > 0:
        here = q.popleft()
        if visited[here] > 0:
            continue

        print(here, end=' ')
        visited[here] = 1

        next_nodes = edges[here]
        for next, connected in enumerate(next_nodes):
            if visited[next] > 0 or connected == 0:
                continue

            q.append(next)


if __name__ == '__main__':
    v, e, st = map(int, input().split())
    for _ in range(v + 1):
        edges.append([0 for _ in range(v + 1)])

    for _ in range(e):
        a, b = map(int, input().split())
        edges[a][b] = 1
        edges[b][a] = 1

    visited = [0 for _ in range(v + 1)]
    dfs(st, visited)
    print()
    visited = [0 for _ in range(v + 1)]
    bfs(st, visited)
    print()

# DFS, BFS