"""
FAILED, 2024-05-05

N의 배수는 항상 N의 약수를 가진다.
- N 이하의 자연수에서 K를 약수로 가지는 개수는 N / K

https://data-flower.tistory.com/95
"""

if __name__ == '__main__':
    n = int(input())
    result = 0
    for i in range(1, n + 1):
        result += (n // i) * i

    print(result)
