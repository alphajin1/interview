def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)

    def dfs(fatigue, count, visited, dungeons):
        nonlocal answer  # nonlocal or global
        answer = max(answer, count)

        for i, v in enumerate(dungeons):
            required_fatigue, cost_fatigue = v
            if fatigue >= required_fatigue and not visited[i]:
                visited[i] = True
                dfs(fatigue - cost_fatigue, count + 1, visited, dungeons)
                visited[i] = False

    dfs(k, 0, visited, dungeons)
    return answer

# 완전탐색 / 피로도 / level 2
# https://school.programmers.co.kr/learn/courses/30/lessons/87946