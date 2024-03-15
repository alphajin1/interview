from collections import deque

def solution(prices):
    answer = []

    # Thinking BruteForce
    # 뒤에 있는 가격들 중에서, 현재 가격보다 최초로 등장하며 가격이 낮은 index를 알아야 한다.
    # queue가 아니라 stack으로 생각해본다면, 되나?

    q = deque()
    q.append((prices[0], 0))
    i = 1
    while i < len(prices):
        price = prices[i]
        if len(q) == 0 or q[-1][0] <= price:
            q.append((prices[i], i))
        else:
            # 떨어지는 케이스
            while q and q[-1][0] > price:
                last_price, last_index = q.pop()
                answer.append((last_index, i - last_index))

            q.append((prices[i], i))

        i += 1

    while q:  # 끝까지 간 경우
        last_price, last_index = q.pop()
        answer.append((last_index, len(prices) - last_index - 1))

    answer.sort()
    result = []
    for i, v in enumerate(answer):
        index, diff = v[0], v[1]
        result.append(diff)

    return result

# 주식가격 / stack
# 방식은 맞으나, 너무 느리게 풀었음. TODO
# answer = [0] & len(prices) 를 생성해놓고 바로 정답을 assign하는게 편리한 것으로 판단.
# https://school.programmers.co.kr/learn/courses/30/lessons/42584