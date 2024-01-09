def solution(s):
    answer = 0
    for i in range(len(a := s.split(" "))):
        if a[i] != 'Z':
            answer += int(a[i])
        else:
            answer -= int(a[i-1])
    return answer