def lcm(a, b):
    # 최대공약수 계산을 위한 함수
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    # 최소공배수 = (a * b) / 최대공약수
    return (a * b) // gcd(a, b)


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())
        print(lcm(a, b))
