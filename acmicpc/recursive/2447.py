import sys

# FAILED, 별찍기 10
# https://edder773.tistory.com/39

def recursive_star(n):
    if n == 1:
        return ['*']
    star = recursive_star(n // 3)

    stars = []
    for i in star:
        stars.append(i * 3)
    for j in star:
        stars.append(j + ' ' * (n // 3) + j)
    for k in star:
        stars.append(k * 3)

    return stars


if __name__ == '__main__':
    n = int(input())  # n = 3^k (k = 1 ~ 8)

    print('\n'.join(recursive_star(n)))