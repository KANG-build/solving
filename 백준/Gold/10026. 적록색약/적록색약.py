###################
# 10026. 적록색약 #
###################

import sys
sys.setrecursionlimit(100000)

def dfs(i, j, g):
    # 범위 체크
    if i < 0 or i >= n or j < 0 or j >= m:
        return
    
    if g[i][j] not in save:
        return
        
    g[i][j] = 'X'
    # 상하좌우
    dfs(i-1, j, g)
    dfs(i+1, j, g)
    dfs(i, j+1, g)
    dfs(i, j-1, g)

    
# 초기 세팅
n = int(input())
normal = 0 
abnormal = 0
graph = []
_graph_ = []
    
for i in range(n):
    a = list(input())
    graph.append(a)
    _graph_.append(a.copy())

m = len(graph[0])

# 도는 과정
for i in range(n):
    for j in range(m):
        if graph[i][j] != 'X':
            save = [graph[i][j]]
            normal += 1          
            dfs(i, j, graph)
            
        if _graph_[i][j] != 'X':
            save = [_graph_[i][j]]
            if _graph_[i][j] == 'R':
                save.append('G')
            elif _graph_[i][j] == 'G':
                save.append('R')
            
            abnormal += 1          
            dfs(i, j, _graph_)

print(normal)
print(abnormal)