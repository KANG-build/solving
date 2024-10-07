#################
# 16953. A -> B #
#################

import sys
sys.setrecursionlimit(1000000)

from collections import deque

n, k = map(int, input().split())
world = {}

queue = deque([])
queue.append(n)
old = {n:1}

def bfs():
    while queue:
        x = queue.popleft()
            
        if x < 0 or x > k:
            break
        
        for dx in [int(str(x) + '1'), 2*x]:
            # 범위 확인
            if dx < 0 or dx > k:
                continue
            
            if dx == k:
                return old[x] + 1
            
            if dx not in old:
                old[dx] = old[x] + 1
                queue.append(dx)
                
    return -1

print(bfs())