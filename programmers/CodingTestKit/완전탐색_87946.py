answer = 0


def solution(k, dungeons):
    # 최소 필요 피로도, 소모 피로도
    # answer = 탐험가능한 최대 던전의 수
    global answer

    visited = [False] * len(dungeons)
    dfs(k, 0, visited, dungeons)
    return answer


def dfs(fatigue, count, visited, dungeons):
    global answer
    answer = max(answer, count)

    for i, v in enumerate(dungeons):
        required_fatigue, cost_fatigue = v
        if fatigue >= required_fatigue and not visited[i]:
            visited[i] = True
            dfs(fatigue - cost_fatigue, count + 1, visited, dungeons)
            visited[i] = False

# TODO 완전탐색 짜는 법을 까먹은 듯 하다.
# 완전탐색 / 피로도 / level 2