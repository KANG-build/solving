def solution(s):
    answer = ""
    for n in s.split(' '):
        for i, m in enumerate(n):
            if i%2 == 0:
                answer += m.upper()
            else: answer += m.lower()
        answer += ' '
    return answer[:-1]