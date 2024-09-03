##################
# 1753. 최단경로 #
##################

import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())

# 시작 노드 번호를 입력받기
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dj(start):
    q = []
    heapq.heappush(q, (0, start))
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    
    while q:   
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
# 다익스트라 알고리즘 수행
dj(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INF")
    # 도달할 수 있는 경우 거리를 출력
    else: print(distance[i])