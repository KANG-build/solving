def solution(n):
    result = n
    i = 0
    while True:
        i += 1
        if '3' in str(i) or i % 3 == 0:
            result += 1
        if i == result:
            break
        
    return result