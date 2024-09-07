import sys
import heapq

INF = 987654321
input = sys.stdin.readline

if __name__ == '__main__':
    max_x, max_y = map(int, input().split())

    arr = []
    for i in range(max_y):
        s = list(input())
        arr.append(s[:-1])

    visited = []
    for y in range(max_y):
        temp = []
        for x in range(max_x):
            temp.append(INF)

        visited.append(temp)

    visited[0][0] = 0
    res = 0
    q = []
    heapq.heappush(q, (0, 0, 0))

    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    while len(q) > 0:
        cost, here_y, here_x = heapq.heappop(q)
        for j in range(4):
            next_y = here_y + dy[j]
            next_x = here_x + dx[j]

            if next_y < 0 or next_x < 0:
                continue

            if next_y >= max_y or next_x >= max_x:
                continue

            next_cost = cost
            if arr[next_y][next_x] == '1':
                next_cost += 1

            if visited[next_y][next_x] <= next_cost:
                continue

            visited[next_y][next_x] = next_cost
            heapq.heappush(q, (next_cost, next_y, next_x))

    print(visited[max_y - 1][max_x - 1])

# 0-1 BFS 로도 풀 수 있다고 함 PASS
# 다익스트라 알고리즘으로 풀었음