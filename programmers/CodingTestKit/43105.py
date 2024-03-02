def solution(triangle):
    rows = len(triangle)
    cols = len(triangle)
    cache = [[0 for j in range(cols)] for i in range(rows)]

    answer = 0
    for y in range(len(triangle)):
        for x in range(len(triangle[y])):
            prev = 0
            if y - 1 >= 0:
                prev = max(prev, cache[y - 1][x])

            if y - 1 >= 0 and x - 1 >= 0:
                prev = max(prev, cache[y - 1][x - 1])

            cache[y][x] = triangle[y][x] + prev
            answer = max(answer, cache[y][x])

    return answer

# DP / 정수 삼각형 / level 3