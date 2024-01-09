def solution(s):
    p = list(s).count('p') + list(s).count('P')
    y = list(s).count('y') + list(s).count('Y')
    return p == y