####################
# 1463. 1로 만들기 #
####################

import sys
sys.setrecursionlimit(1000000)

from collections import deque

n = int(input())

world = [0 for i in range(n+1)]

queue = deque([])
queue.append(n)

def bfs():
    while queue:
        x = queue.popleft()
        
        a = [x-1]
        if x%3 == 0:
            a.append(x//3)
        if x%2 == 0:
            a.append(x//2)
            
        for i in a:
            dx = i
            # 범위 확인
            if dx < 0:
                continue
            
            if world[dx] == 0 or world[dx] > world[x]+1:
                world[dx] = world[x] + 1
                queue.append(dx)
                
        if x == 1:
            return world[1]
            
            
    return world[1]

print(bfs())