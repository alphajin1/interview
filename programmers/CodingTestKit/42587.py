from collections import deque


def solution(priorities, location):
    answer = 0

    q = deque()
    for i, pr in enumerate(priorities):
        q.append([pr, i])

    while len(q) > 0:
        pr, index = q.popleft()

        is_first_priority = True
        for i, v in enumerate(q):
            q_pr, _ = v
            if pr < q_pr:
                is_first_priority = False
                break

        if is_first_priority:
            # 찾고자 하는 프로세스의 위치
            if index == location:
                break

            answer += 1
            continue
        else:
            q.append([pr, index])

    return answer + 1

# 스택/큐 프로세스 (Level 2)
# https://school.programmers.co.kr/learn/courses/30/lessons/42587