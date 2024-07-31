from collections import deque
import sys
input= sys.stdin.readline

count = 1
        
# BFS 메서드 정의
def bfs(graph, start, visited):
    global count
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    #현재 노드를 방문 처리
    visited[start] = 1
    
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in reversed(sorted(graph[v])):
            if not visited[i]:
                queue.append(i)
                count += 1
                visited[i] = count

N, M, V = map(int, input().split())  # 정점의 개수, 간선의 개수, 탐색 시작 정점                
                
# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited_bfs = [0] * (N+1)

# 정의된 BFS 함수 호출
bfs(graph, V, visited_bfs)

for i in visited_bfs[1:]:
    print(i)