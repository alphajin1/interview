from collections import defaultdict
def solution(nums):
    cache = defaultdict(int)

    for i, num in enumerate(nums):
        cache[num] += 1

    answer = int(min(len(cache), len(nums) / 2))

    return answer

if __name__ == '__main__':
    print(solution([3, 1, 2, 3]))