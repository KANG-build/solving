###################
# 1976. 여행 가자 #
###################

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

n = int(input())
m = int(input())
parent = [i for i in range(n+1)]

for a in range(1, n+1):
    line = list(map(int, input().split()))
    for b in range(1, n+1):
        if line[b-1] == 1:
            union_p(parent, a, b)

city = list(map(int, input().split()))
for i in range(1, len(city)):
    if find_p(parent, city[i]) != find_p(parent, city[i-1]):
        print("NO")
        break
else:
    print("YES")
    