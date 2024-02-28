def solution(n):
    a = 1
    num = ''
    answer = 0

    while 3**a <= n: 
        a += 1
    
    for i in range(1, a+1):
        num += str(n//3**(a-i))
        n -= 3**(a-i)*(n//3**(a-i))
        
    for idx, s in enumerate(num):
        answer += int(s) * 3**idx
        
    return answer