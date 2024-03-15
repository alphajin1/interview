def solution(answers):
    answer = []

    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    correct1 = 0
    correct2 = 0
    correct3 = 0

    i = 0
    for ans in answers:
        if ans == pattern1[i % len(pattern1)]:
            correct1 += 1
        if ans == pattern2[i % len(pattern2)]:
            correct2 += 1
        if ans == pattern3[i % len(pattern3)]:
            correct3 += 1

        i += 1

    max_correct = max(correct1, max(correct2, correct3))
    if max_correct == correct1:
        answer.append(1)
    if max_correct == correct2:
        answer.append(2)
    if max_correct == correct3:
        answer.append(3)

    return answer

# 모의고사 / 완전탐색
# correct 도 배열로 작성하는게 좋아보인다.
# https://school.programmers.co.kr/learn/courses/30/lessons/42840