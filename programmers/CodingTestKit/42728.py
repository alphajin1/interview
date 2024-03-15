from pprint import pprint


def solution(array, commands):
    answer = []

    for cmd in commands:
        a, b, c = cmd
        brr = array[a - 1:b].copy()  # 기억하자. copy()
        brr.sort()

        answer.append(brr[c - 1])

    return answer

# K번째 수
# https://school.programmers.co.kr/learn/courses/30/lessons/42748