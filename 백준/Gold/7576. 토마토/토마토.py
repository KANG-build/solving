################
# 7576. 토마토 #
################

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import deque

m, n = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

queue = deque([])    

# 1마다 bfs가 시작해야 한다
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((j, i))    
        
def bfs():
    while queue:
        x, y = queue.popleft()
        
        for i in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            dx, dy = i[0], i[1]
            
            if dx < 0 or dx >= m or dy < 0 or dy >= n:
                continue
                
            if graph[dy][dx] != 0:
                continue
            
            if graph[dy][dx] == 0:
                graph[dy][dx] = graph[y][x] + 1
                queue.append((dx, dy))

bfs()

max_num = 0
loop = True
# 0 있는지 체크
for i in graph:
    for j in i:
        if j == 0:
            loop = False
            break
            
    if loop == False:
        print(-1)
        break
    
    max_i = max(i)
    if max_num < max_i:
        max_num = max_i

if loop == True:
    print(max_num-1)