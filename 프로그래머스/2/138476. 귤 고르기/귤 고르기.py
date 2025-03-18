def solution(k, tangerine):
    memo = [0] * (max(tangerine)+1)
    
    # 일단 개수를 세기 
    for i in tangerine:
        memo[i] += 1
            
    answer = 0
    full = 0
    for i in sorted(memo, reverse=True):
        full += i
        answer += 1
        if full >= k:
            break
    
    return answer