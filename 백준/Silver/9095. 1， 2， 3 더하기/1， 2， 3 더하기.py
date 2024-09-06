import sys
input = sys.stdin.readline

n = int(input())

memo = [1, 2, 4]

for i in range(n):
    num = int(input())
    if num < len(memo):
        print(memo[num-1])
        continue
        
    for j in range(len(memo), num):
        memo.append(0)
        memo[j] = memo[j-3] + memo[j-2] + memo[j-1]
    
    print(memo[-1])