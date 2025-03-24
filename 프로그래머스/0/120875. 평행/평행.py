from itertools import combinations

def cal(a, b):
    return (a[0]-b[0])/(a[1]-b[1])

def solution(dots):
    answer = 0
    if (cal(dots[0], dots[1]) == cal(dots[2], dots[3])) or (cal(dots[0], dots[2]) == cal(dots[1], dots[3])) or (cal(dots[0], dots[3]) == cal(dots[1], dots[2])):
        answer = 1
    
    return answer
