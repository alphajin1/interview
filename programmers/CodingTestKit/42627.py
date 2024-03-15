import heapq


def solution(jobs):
    # 전략
    # 현재 선택할 수 있는 process 중에서, 가장 짧은 process를 선택해야 한다.
    # 하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리한다.

    answer = 0
    start = -1
    now = 0
    cache = []  # heap으로 사용할 것

    i = 0
    while i < len(jobs):
        for job in jobs:
            job_start, job_cost = job
            if start < job_start <= now: # 이것도 굉장히 좋은 트릭이라고 생각됨.
                heapq.heappush(cache, (job_cost, job_start))

        if len(cache) > 0: # 작업 요청시간이 0 ~ 1000 이므로 pop할 것이 없으면 now += 1을 수행하면 됨. (문제를 심플하게 만듬)
            here_cost, here_start = heapq.heappop(cache)
            start = now
            now += here_cost # 현재 시간
            answer += (now - here_start)
            i += 1
        else:
            now += 1

    return answer // len(jobs)

# 디스크 컨트롤러 (level 3)
# https://school.programmers.co.kr/learn/courses/30/lessons/42627
# TODO (failed)
# https://velog.io/@younge/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%94%94%EC%8A%A4%ED%81%AC-%EC%BB%A8%ED%8A%B8%EB%A1%A4%EB%9F%AC-%ED%9E%99