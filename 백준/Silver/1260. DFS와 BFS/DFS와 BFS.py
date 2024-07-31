from collections import deque
import sys
input= sys.stdin.readline

# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)
        
# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    
    #현재 노드를 방문 처리
    visited[start] = True
    
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M, V = map(int, input().split())  # 정점의 개수, 간선의 개수, 탐색 시작 정점                
                
# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

# 정의된 BFS 함수 호출
dfs(graph, V, visited_dfs)
print()
bfs(graph, V, visited_bfs)