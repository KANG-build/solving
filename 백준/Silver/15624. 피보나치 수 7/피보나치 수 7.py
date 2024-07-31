import sys
input = sys.stdin.readline

n = int(input())
memo = [0, 1]
for index in range(2, n+1):
    memo.append((memo[index-1] + memo[index-2])%1000000007)

print(memo[n])