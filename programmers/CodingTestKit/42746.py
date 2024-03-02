def solution(numbers):
    number_str = [str(v) for v in numbers]
    number_str.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(number_str)))

# TODO 03-02 답지 확인
# numbers가 0 이상 1000 이하이므로
# sort key를 x * 3 로 하여, 정렬 우선순위를 명확하게 하기 위함. 3 > 30 condition
# 마지막에 int로 다시 바꾸는 [0, 0, 0, 0] 입력 케이스가 있기 때문. (아... 이건 문제가 함정이 있구만)
# 정렬 / 가장 큰 수 / level 2