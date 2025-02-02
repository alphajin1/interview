def solution(people, limit):
    # 한번에 최대 2명씩만 탈 수가 있다.
    answer = 0
    people.sort()
    l = 0
    r = len(people) - 1

    while (l <= r):
        if (people[l] + people[r] <= limit):  # limit 보다 작거나 같으면 둘다 구출 가능
            l += 1
            r -= 1
        else:  # 안되면 일단 몸무게 큰 사람부터 먼저 구출
            r -= 1

        answer += 1
    return answer

# TODO 한번에 최대 2명만 탈 수 있다. 이것을 기억하자.
# 그리디 / 구명보트 / level 2
# https://school.programmers.co.kr/learn/courses/30/lessons/42885