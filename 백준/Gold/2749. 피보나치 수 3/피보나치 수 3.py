import sys
input = sys.stdin.readline

# 피사노 주기
M = 10**6
P = 15 * 10**5

n = int(input())
n %= P

memo = [0, 1]
for index in range(2, n+1):
    memo.append((memo[index-1] + memo[index-2])%1000000)

print(memo[n])