from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

count = [[0 for _ in range(n)] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    
    count[a][b] = 1
    count[b][a] = 1 

# 플로이드-워셜 먼저 가면 줄어듦
for k in range(n):
    for a in range(n):
        for b in range(n):
            if a != b:
                if count[a][k] != 0 and count[k][b] != 0:
                    if count[a][b] == 0 or count[a][b] > count[a][k] + count[k][b]:
                        count[a][b] = count[a][k] + count[k][b]

min_value = int(1e9)
min_index = 0
for i in range(n):
    if min_value > sum(count[i]):
        min_value = sum(count[i])
        min_index = i

print(min_index+1)