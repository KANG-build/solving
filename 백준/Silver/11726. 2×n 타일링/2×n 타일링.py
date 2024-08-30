import sys
input = sys.stdin.readline

n = int(input())
memo = [1, 1]
for i in range(2, n+1):
    memo.append((memo[i-1] + memo[i-2])%10007)

print(memo[n])