def solution(N, number):
    answer = 0

    cache = []
    for i in range(1, 9):
        cases = set()
        base_case = int(str(N) * i)  # 5, 55, 555 ...
        cases.add(base_case)

        for j in range(0, i - 1):  # j개를 사용해서 만든 값
            for op1 in cache[j]:
                for op2 in cache[-j - 1]: # j 와 -j - 1은 array에서 반대위치 포지션
                    cases.add(op1 - op2)
                    cases.add(op1 + op2)
                    cases.add(op1 * op2)
                    if op2 != 0:
                        cases.add(op1 // op2)

        if number in cases:
            return i

        cache.append(cases)

    return -1

# N으로 표현 / DP
# TODO
# https://school.programmers.co.kr/learn/courses/30/lessons/42895

if __name__ == '__main__':
    solution(5, 12)