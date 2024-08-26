###########################
# 11724. 연결 요소의 개수 #
###########################

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)
        
N, M = map(int, input().split())

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * (N+1)

answer = 0

for V in range(1, N+1):
    if visited[V] == False:
        answer += 1
        dfs(graph, V, visited)

print(answer)