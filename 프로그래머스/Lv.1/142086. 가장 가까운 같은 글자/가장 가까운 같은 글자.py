def solution(s):
    answer = []
    b = ''
    for idx, num in enumerate(s):
        if num in b:
            answer.append(idx - b.rindex(num))
        else:
            answer.append(-1)
        b += num
    return answer