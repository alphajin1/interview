def solution(citations):
    citations.sort()
    answer = 0

    # n개의 논문이 n회 이상 인용되면 n이 정답
    for i, v in enumerate(citations):
        num_of_report = len(citations) - i
        value = v

        index = min(num_of_report, value)
        answer = max(answer, index)

    return answer

# H-Index / 정렬
# https://school.programmers.co.kr/learn/courses/30/lessons/42747