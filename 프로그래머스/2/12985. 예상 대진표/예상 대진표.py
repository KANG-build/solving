import math

def solution(n,a,b):
    answer = 0

    # 뭔가 같아질때까지 일련의 과정을 반복한다...
    while a != b:
        answer += 1
        a = a//2 + a%2
        b = b//2 + b%2

    return answer