def solution(n):
    # 이거 memo 쓰는거였는데 
    memo = [1, 1]
    
    for i in range(2, n+1):
        memo.append((memo[i-1] + memo[i-2]) %1000000007)
        
    return memo[n]