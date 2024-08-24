####################
# 4963. 섬의 개수 #
###################

import sys
sys.setrecursionlimit(100000)

def dfs(i, j):
    # 범위 체크
    if i < 0 or i >= h or j < 0 or j >= w:
        return
    
    if graph[i][j] != 1:
        return
        
    graph[i][j] = 0
    # 상하좌우
    dfs(i-1, j)
    dfs(i+1, j)
    dfs(i, j+1)
    dfs(i, j-1)
    
    dfs(i+1, j+1)
    dfs(i-1, j+1)
    dfs(i+1, j-1)
    dfs(i-1, j-1)

while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break
    answer = 0 
    graph = []
    
    # 초기 세팅
    for H in range(h):
        graph.append(list(map(int, input().split())))
        
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                answer += 1          
                dfs(i, j)

    print(answer)
