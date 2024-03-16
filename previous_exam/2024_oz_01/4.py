def sub_solution(input, pattern):
    temp = ""
    i, j = 0, 0
    N, M = len(input), len(pattern)

    while i < N and j < M:
        x = input[i]
        y = pattern[j]
        if x == y:
            temp += x
            i += 1
            j += 1
        else:
            i += 1

    return temp == pattern


def solution(inputs, pattern):
    answer = []
    for i in inputs:
        answer.append(sub_solution(i, pattern))

    return answer


# Problem.
# s와 pattern이 주어졌을 때 조건을 만족하면 True, 아니면 False 반환
# 조건. s에서 소문자를 제거하여 pattern과 동일한 문자열을 만들 수 있으면 true
# 제약조건
    # length = 1000, 영어로만 이루어짐.
    # len(inputs) = 100

if __name__ == '__main__':
    print(solution(["BucketPlace"], "BP"))  # True
    print(solution(["BucketPlace"], "BuPl"))  # True
    print(solution(["BucketPizza"], "BP"))  # True
    print(solution(["BucketList"], "BP"))  # False
