def solution(s):
    answer, right, wrong = 0, 0, 0
    for i in s:
        if right == wrong:
            answer += 1
            a = i
        if i == a:
            right += 1
        else:
            wrong += 1
    return answer