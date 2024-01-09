def solution(a, b):
    if a>b:
        return sum(range(b, a+1))
    elif b>a:
        return sum(range(a, b+1))
    else: return a