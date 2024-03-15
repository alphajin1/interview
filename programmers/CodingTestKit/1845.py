from collections import defaultdict
def solution(nums):
    cache = defaultdict(int)

    for i, num in enumerate(nums):
        cache[num] += 1

    answer = int(min(len(cache), len(nums) / 2))

    return answer

# 폰켓몬
# https://school.programmers.co.kr/learn/courses/30/lessons/1845