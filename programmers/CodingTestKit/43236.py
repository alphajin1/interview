def solution(distance, rocks, n):
    # 0 ~ distance 사이에 rocks 들이 있을 떄, n개의 rocks를 제거하여
    # 각 지점간 거리의 최솟값을 최대로 하는 값을 반환하라.
    # 바위는 50000개

    rocks.sort()
    rocks.append(distance)
    left = 0
    right = distance

    answer = 0
    while left <= right:
        mid = (left + right) // 2  # mid 는 거리의 최솟값을 의미한다.

        remove_count = 0
        prev_rock = 0
        for rock in rocks:
            diff = rock - prev_rock
            if diff < mid:  # rock 을 제거한 경우
                remove_count += 1
            else:
                prev_rock = rock # TODO 이 컨디션을 고려하지 못해서 틀렸음.

        if remove_count > n:  # impossible
            right = mid - 1
        else:
            answer = mid
            left = mid + 1

    return answer

# 징검다리 / 이분탐색 / Level 4
# https://school.programmers.co.kr/learn/courses/30/lessons/43236