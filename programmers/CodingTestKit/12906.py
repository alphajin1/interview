from collections import defaultdict


def solution(arr):
    answer = []

    for i, v in enumerate(arr):
        if len(answer) == 0 or answer[-1] != v:
            answer.append(v)

    return answer

# 같은 숫자는 싫어 (level 1)
# https://school.programmers.co.kr/learn/courses/30/lessons/12906
