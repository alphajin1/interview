import sys
# https://www.acmicpc.net/problem/15552

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        a, b = map(int, sys.stdin.readline().split())

        print(a + b)