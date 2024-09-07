import sys

input = sys.stdin.readline


def recursive(n, m, arr):
    if len(arr) == m:
        for i, v in enumerate(arr):
            print(v, end=' ')

        print()
        return

    for i in range(1, n + 1):
        if i not in arr:
            arr.append(i)
            recursive(n, m, arr)  # select cases
            arr.pop()



if __name__ == '__main__':
    n, m = map(int, input().split())

    arr = [] # 참조형
    recursive(n, m, arr)

# another solutions.
# from itertools import permutations
#
# N, M = map(int, input().split())
# N = list(map(str, range(1, N+1)))
# print('\n'.join(list(map(' '.join, permutations(N, M)))))