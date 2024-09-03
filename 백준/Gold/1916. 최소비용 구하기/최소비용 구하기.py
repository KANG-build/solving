#########################
# 1916. 최소비용 구하기 #
#########################

import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)  

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())
    
def dj(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:   
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

print(distance[end])