from pprint import pprint


def solution(n, lost, reserve):
    answer = 0
    # lost와 reserve가 같은 경우에는 빌려줄 수가 없다. 둘중에 한명만 빌려줄 수 있다.

    lost.sort()
    reserve.sort()

    cache = set()
    for i in range(n):
        cache.add(i + 1)

    for i, v in enumerate(lost):
        cache.remove(v)

    for i, v in enumerate(reserve):
        if v in lost:
            cache.add(v)
            continue

        # prev check
        prev = v - 1
        if prev > 0 and prev not in cache:
            cache.add(prev)  # 추가했다면 pass
            continue

        next = v + 1
        if next <= n and next not in cache:
            cache.add(next)

    pprint(cache)

    return len(cache)

# 체육복 / 탐욕법(Greedy)
# https://school.programmers.co.kr/learn/courses/30/lessons/42862