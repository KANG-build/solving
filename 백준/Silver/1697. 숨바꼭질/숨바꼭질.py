##################
# 1697. 숨바꼭질 #
##################

import sys
sys.setrecursionlimit(1000000)

from collections import deque

n, k = map(int, input().split())

world = [0 for i in range(100001)]

queue = deque([])
queue.append(n)

def bfs():
    while queue:
        x = queue.popleft()
        
        if x == k:
            return world[k]
        
        for i in [x-1, x+1, 2*x]:
            dx = i
            # 범위 확인
            if dx < 0 or dx >= 100001:
                continue
            
            if world[dx] == 0 or world[dx] > world[x]+1:
                world[dx] = world[x] + 1
                queue.append(dx)
            
            
    return world[k]

print(bfs())