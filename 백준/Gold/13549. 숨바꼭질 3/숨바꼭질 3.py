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
    count = 0
    
    while queue:
        x = queue.popleft()
        
        if x == k:
            return world[k]
        
        for i in [2*x, x-1, x+1]:
            dx = i
                
            # 범위 확인
            if dx < 0 or dx >= 100001:
                continue
            
            if world[dx] == 0 or world[dx] > world[x]:
                if i == 2*x:
                    world[dx] = world[x]
                else:
                    world[dx] = world[x] + 1
                queue.append(dx)
            
            
    return world[k]

print(bfs())