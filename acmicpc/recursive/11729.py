import sys

# FAILED, 정확하게 이해는 가지 않음. 하노이의 탑
# https://dev-scratch.tistory.com/22
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
