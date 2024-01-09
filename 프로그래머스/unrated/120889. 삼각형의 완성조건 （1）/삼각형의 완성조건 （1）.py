def solution(sides):
    if 2 * max(sides) < sum(sides):
        answer = 1
    else: answer = 2    
    return answer