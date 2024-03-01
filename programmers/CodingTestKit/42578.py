def solution(clothes):
    answer = 0
    cache = {}
    for cloth in clothes:
        x, y = cloth
        if y in cache:
            cache[y] += 1
        else:
            cache[y] = 1

    temp = 1
    for k, v in cache.items():
        temp *= (v + 1)

    answer = temp - 1
    return answer

# 해시 / 의상 (Level 2)