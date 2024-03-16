def solution(str):
    targets = "aeiouAEIOU"

    temp = ""
    extracted = ""
    for i in str:
        if i in targets:
            temp += "_"
            extracted += i
        else:
            temp += i

    answer = ""
    j = len(extracted) - 1
    for i in temp:
        if i == "_":
            answer += extracted[j]
            j -= 1
        else:
            answer += i

    return answer


# Problem.
# a e i o u 의 순서를 뒤집어주세요. 대문자도 들어올 수 있음.

if __name__ == '__main__':
    print(solution("bucketplace"), solution("bucketplace") == "beckatplecu")
    # beckatplecu