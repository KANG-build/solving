######################
# 1012. 유기농 배추 #
#####################

import sys
sys.setrecursionlimit(5000)

def dfs(i, j):
    # 범위 체크
    if i < 0 or i >= n or j < 0 or j >= m:
        return
    
    if graph[i][j] == 1:
        graph[i][j] = 0
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    else:
        return

t = int(input())
for T in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for i in range(m)] for j in range(n)]
    # 초기 세팅
    for K in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    answer = 0
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                answer += 1          
                dfs(i, j)

    print(answer)
