######################
# 20040. 사이클 게임 #
######################

import sys
input = sys.stdin.readline

def find_p(parent, x):
    if parent[x] != x:
        parent[x] = find_p(parent, parent[x])
    return parent[x]

def union_p(parent, a, b):
    a = find_p(parent, a)
    b = find_p(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

answer = 1
cycle = False

for _ in range(m):
    a, b = map(int, input().split())
    if find_p(parent, a) ==  find_p(parent, b):
        cycle = True
        break
    else:
        answer += 1
        union_p(parent, a, b)
        
if cycle:
    print(answer)
else:
    print(0)