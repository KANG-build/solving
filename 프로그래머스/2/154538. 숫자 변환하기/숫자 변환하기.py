from collections import deque

# 해시
def solution(x, y, n):
    if x == y:
        return 0
    memo = [0] * (y*3+1)
    stack = deque([x])
    while True:
        temp = stack.popleft()
        for i in [temp+n, temp*2, temp*3]:
            if i > y or memo[i]!=0:
                continue
            memo[i] = memo[temp] + 1 
            stack.append(i)
            
            if i == y:
                return memo[i]
        
        if not stack:
            return -1
    return -1