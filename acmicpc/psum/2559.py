

n, m = map(int, input().split())
arr = list(map(int, input().split()))

psum = [0] * (n + 1)
for i, v in enumerate(arr):
    psum[i + 1] = psum[i] + v

result = -987654321
for i, v in enumerate(psum):
    if i < m:
        continue

    diff = psum[i] - psum[i - m]
    result = max(result, diff)

print(result)