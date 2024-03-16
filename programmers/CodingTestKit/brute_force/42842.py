def solution(brown, yellow):
    answer = []
    total = brown + yellow  # yellow 는 반드시 center
    for x in range(1, total + 1):
        for y in range(1, x + 1):
            if x * y == total and (x - 2) * (y - 2) == yellow:
                return [x, y]

    return []


# 완전탐색 / level 2
# https://school.programmers.co.kr/learn/courses/30/lessons/42842