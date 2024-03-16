def solution(numbers, goal):
    N = len(numbers)
    for i in range(N):
        for j in range(i + 1, N):
            if numbers[i] + numbers[j] == goal:
                return [i, j]

    return None


# Problem.
# 주어진 정수 배열 numbers 에서 두 정수의 합이 목표값 goal 과 동일한 수를 만들 수 있는 두 정수 찾기
# 정답은 유일하며, 해당 쌍이 존재하는 Index 값을 오름 차순으로 정렬하여 출력
# 제약사항
    # len(number) <= 10000
    # number = int
    # goal = int

if __name__ == '__main__':
    print(solution([4, 3, 5, 1], 4))
    # result = [1, 3]