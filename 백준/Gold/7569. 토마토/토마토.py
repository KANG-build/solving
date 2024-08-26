################
# 7569. 토마토 #
################

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import deque

m, n, h = map(int, input().split())
G = []
for H in range(h):
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    G.append(graph)
    
queue = deque([])    

# 1마다 bfs가 시작해야 한다
for H in range(h):
    for i in range(n):
        for j in range(m):
            if G[H][i][j] == 1:
                queue.append((j, i, H))    
        
def bfs():
    while queue:
        x, y, z = queue.popleft()
        
        for i in [(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1)]:
            dx, dy, dz = i[0], i[1], i[2]
            
            if dx < 0 or dx >= m or dy < 0 or dy >= n or dz < 0 or dz >= h:
                continue
                
            if G[dz][dy][dx] != 0:
                continue
            
            if G[dz][dy][dx] == 0:
                G[dz][dy][dx] = G[z][y][x] + 1
                queue.append((dx, dy, dz))

bfs()

max_num = 0
maxxx = 0
loop = True
# 0 있는지 체크
for H in G:
    for i in H:
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
            
    if loop == False:
        break

    if maxxx < max_num:
        maxxx = max_num
        

            
if loop == True:
    print(maxxx-1)