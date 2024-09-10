
import heapq
import sys
input = sys.stdin.readline

INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m, x = map(int, input().split())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    
    distance = [INF for _ in range(n+1)]
    heap = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    distance[start] = 0
    heapq.heappush(heap, (0, start))
    
    while heap:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(heap)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:  # distance[now]가 INF이면 진행, 다른 노드 돌면서 더 짧은거 찾을수도
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))
                
    return distance

dis = [0]     
# 다익스트라 알고리즘 '반복' 수행
for i in range(1, n+1):
    dis.append(dijkstra(i))
    
answer = []
# 최단거리는 각 노드마다 X번째 거리랑 X에서 각자의 거리로 가는 것이 합쳐져야 함 
for i in range(1, n+1):
    if i == x:
        continue
    
    answer.append(dis[i][x] + dis[x][i])
    
print(max(answer))
    