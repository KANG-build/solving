import sys
sys.setrecursionlimit(130000)
input = sys.stdin.readline

count = 1

# DFS 메서드 정의
def dfs(graph, v, visited):
    global count
    # 현재 노드를 방문 처리
    visited[v] = count
    count += 1
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in reversed(sorted(graph[v])):
        if not visited[i]:
            dfs(graph, i, visited)

N, M, V = map(int, input().split())  # 정점의 개수, 간선의 개수, 탐색 시작 정점

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [0] * (N+1)

# 정의된 DFS 함수 호출
dfs(graph, V, visited)

for i in visited[1:]:
    print(i)