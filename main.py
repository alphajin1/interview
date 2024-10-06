import sys
import heapq
from collections import deque
from collections import defaultdict

INF = 987654321000
input = sys.stdin.readline

white = 0
blue = 0  # value is = 1

board = []


def recursive_cutting(start_y, start_x, y, x, rect_size):

    global blue
    global white

    if rect_size == 1:
        if board[y - 1][x - 1] == 1:
            blue += 1
        else:
            white += 1

        print(f"rect_size = {rect_size}")
        return

    is_rect = True
    corner_color = board[start_y - 1][start_x - 1]
    for dy in range(start_y - 1, y):
        for dx in range(start_x - 1, x):
            if corner_color != board[dy][dx]:
                is_rect = False

    if is_rect:
        if corner_color == 1:
            blue += 1
        else:
            white += 1

        print(f"rect_size(big) = {rect_size}")
        return

    recursive_cutting(start_y, start_x, y // 2, x // 2, rect_size // 2)
    recursive_cutting(y // 2, start_x, y, x // 2, rect_size // 2)
    recursive_cutting(start_y, x // 2, y // 2, x, rect_size // 2)
    recursive_cutting(y // 2, x // 2, y, x, rect_size // 2)


if __name__ == '__main__':
    n = int(input())  # n = k^2

    for _ in range(n):
        temp = list(map(int, input().split()))
        board.append(temp)

    # for dy in range(n):
    #     for dx in range(n):
    #         print(board[dy][dx], end=" ")
    #
    #     print()
    recursive_cutting(1, 1, n, n, n)
    print(white)
    print(blue)
