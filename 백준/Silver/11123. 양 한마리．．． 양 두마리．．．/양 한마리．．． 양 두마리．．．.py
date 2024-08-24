####################################
# 11123. 양 한마리... 양 두마리... #
####################################

import sys
sys.setrecursionlimit(100000)

def dfs(i, j):
    # 범위 체크
    if i < 0 or i >= h or j < 0 or j >= w:
        return
    
    if graph[i][j] != '#':
        return
        
    graph[i][j] = '.'
    dfs(i-1, j)
    dfs(i+1, j)
    dfs(i, j+1)
    dfs(i, j-1)


t = int(input())
for T in range(t):
    h, w = map(int, input().split())
    graph = []
    
    # 초기 세팅
    for H in range(h):
        graph.append(list(input()))
    answer = 0
    
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '#':
                answer += 1          
                dfs(i, j)

    print(answer)
