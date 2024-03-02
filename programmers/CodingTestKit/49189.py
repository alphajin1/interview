from collections import deque


def solution(n, edge):
    answer = 0

    cache = {}
    for i, v in enumerate(edge):
        a, b = v
        if a not in cache:
            cache[a] = [b]
        else:
            cache[a].append(b)

        if b not in cache:
            cache[b] = [a]
        else:
            cache[b].append(a)

    # BFS
    visited = [False] * (n + 1)
    visited[1] = True

    distance = [float('inf')] * (n + 1)
    distance[1] = 0

    q = deque()
    q.append(1)

    max_distance = 0
    while len(q) > 0:
        here = q.popleft()
        for i, next in enumerate(cache[here]):
            if visited[next] is True:
                continue

            visited[next] = True
            distance[next] = distance[here] + 1
            max_distance = max(max_distance, distance[next])
            q.append(next)

    for i, v in enumerate(distance):
        if v == max_distance:
            answer += 1

    return answer

# 그래프 / 가장 먼 노드 / level 3 / BFS