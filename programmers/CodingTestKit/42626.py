import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    while len(scoville) > 0:
        a = heapq.heappop(scoville)
        if a >= K:
            return answer

        if len(scoville) == 0:
            return -1

        answer += 1
        b = heapq.heappop(scoville)
        c = a + b * 2
        heapq.heappush(scoville, c)

    return -1

# 더 맵게 / heap / level 2