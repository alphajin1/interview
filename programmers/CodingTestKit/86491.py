def solution(sizes):
    answer = 0
    max_width = 0
    max_height = 0

    for s in sizes:
        a, b = s

        if a > b:
            a, b = b, a
        max_width = max(max_width, a)
        max_height = max(max_height, b)

    return max_width * max_height

# 최소 직사각형 / 완전탐색
# https://school.programmers.co.kr/learn/courses/30/lessons/86491