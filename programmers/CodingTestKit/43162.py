def solution(n, computers):
    visited = [False] * (n)

    def dfs(here):
        if visited[here]:
            return

        visited[here] = True
        for next, connected in enumerate(computers[here]):
            if connected == 1:
                dfs(next)

    answer = 0
    for i in range(n):
        if visited[i] is False:
            answer += 1
            dfs(i)

    return answer


# 네트워크 / DFS, BFS
# https://school.programmers.co.kr/learn/courses/30/lessons/43162