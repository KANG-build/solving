def solution(n):
    answer = 0 
    
    # 시작점
    for i in range(1, n+1):
        sum_num = 0
        # 다음 숫자부터 더하기 시작한다
        for j in range(i, n+1):
            sum_num += j
            
            if sum_num == n:
                answer += 1
                break
            
            if sum_num > n:
                break
            
    return answer