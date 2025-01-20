import sys
import heapq
from collections import deque
from collections import defaultdict


def combination(a, b):
    # aCb
    b = min(b, a - b)
    result = 1

    da = a
    db = 1

    while da >= 1 and db <= b:
        result *= da
        result /= db
        da -= 1
        db += 1

    return int(result)

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        a, b = map(int, input().split())
        print(combination(b, a))