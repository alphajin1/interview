from collections import defaultdict

def transform(n):
    x = n
    y = int(str(x)[::-1])
    return x - y
def solution(numbers):
    # numbers[i] - reverse(numbers[i]) == numbers[j] - reverse(numbers[j]
    # i < j 인 pair의 수를 찾아라.
    MOD = 10**9 + 7
    cache = defaultdict(int)
    answer = 0
    for i, v in enumerate(reversed(numbers)): # 거꾸로 탐색
        x = transform((v))
        if x in cache:
            print(v, x)
            answer += cache[x]
            answer %= MOD

        cache[x] += 1

    return answer




# Problem. 맞을까 ?
# numbers[i] + reverse(numbers[j]) == numbers[j] + reverse(numbers[i])
# 의 수를 return 할 것 (너무 많다면 mod 10^9 + 7)
# 설명
# (0, 1) 42 + r(97) = 42 + 79 = 121, 97 + r(42) = 121
# (2, 3) 13 + r(24) = 13 + 42 = 55, 24 + r(13) = 55
# 제약조건
    # len(numbers) = 10만
    # numbers[i] <= 10^9


if __name__ == '__main__':
    print(solution([42, 97, 13, 24, 1, 76]) == 2)