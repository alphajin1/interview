import sys
# https://www.acmicpc.net/problem/15552


# n = int(sys.stdin.readline().rstrip('\n'))

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        a, b = map(int, sys.stdin.readline().split())

        print(a + b)