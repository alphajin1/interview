answer = 0


def solution(numbers, target):
    dfs(0, 0, target, numbers)
    return answer


def dfs(i, cur, target, numbers):
    global answer
    if i == len(numbers):
        if cur == target:
            answer += 1

        return

    dfs(i + 1, cur + numbers[i], target, numbers)
    dfs(i + 1, cur - numbers[i], target, numbers)

# DFS / 타겟 넘버 / level 2