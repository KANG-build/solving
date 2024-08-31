########################
# 11727. 2×n 타일링 2 #
########################

import sys
input = sys.stdin.readline

n = int(input())
memo = [1, 3]
for i in range(2, n+1):
    memo.append((memo[i-2] * 2 + memo[i-1])%10007)

print(memo[n-1])