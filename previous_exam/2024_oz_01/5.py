def solution(height1, height2):
    # 문제를 단순화 시킨다면, 언제 교환을 해야하는 걸까? > 연속 증가구간이 깨질 때 교환을 수행. 짧은 길이를


    return None


# Problem. TODO 모르겠다.
# height1, height2 에서 같은 위치에 있는 학생은 교환이 가능하다. 최소한의 교환 수로 각각 정렬시켜라.
# 제약조건
    # len(height1) = 10만, len(height2) = 10만
    # 답은 언제나 존재한다.

if __name__ == '__main__':
    print(solution([150, 170, 180, 180], [150, 160, 170, 190])) # 1
    print(solution([130, 140], [130, 140])) # 0

    # 뭔가 예상하지 못한 예제가 무엇이 있을까? > 뒤에서 sorting하는게 나은데 앞에서 sorting하는 경우는?
    # 10 20 50 40
    # 10 30 50 60
    # merge sort 했을 때 switching 의 수? > 아니다.
    # 10 20 31 40
    # 10 21 30 40