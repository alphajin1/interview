import sys
import heapq
from collections import deque
from collections import defaultdict

INF = 987654321000
input = sys.stdin.readline


def hanoi(n, x, y, z):
    if n == 1:
        print(x, z)
    else:
        hanoi(n - 1, x, z, y)
        print(x, z)
        hanoi(n - 1, y, x, z)


if __name__ == '__main__':
    n = int(input())
    print(2 ** n - 1)
    hanoi(n, 1, 2, 3)
