 #######################
# 14940. 쉬운 최단거리 #
########################

from collections import deque

def bfs(x, y):
    queue = deque([])
    queue.append((x, y))
    
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        
        # 해당 칸이랑 연결된 칸들 전부 삽입
        for i in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
            dx, dy = i[0], i[1]
            # 범위 확인
            if dx < 0 or dx >= m or dy < 0 or dy >= n:
                continue
            
            # 0이 아닌지 확인
            if graph[dy][dx] == 0:
                continue
            
            if graph[dy][dx] == 1:
                graph[dy][dx] = graph[y][x] + 1
                queue.append((dx, dy))
            
                
    return graph[n-1][m-1]
            
            
n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

# 1마다 bfs가 시작해야 한다
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            bfs(j, i)

for i in graph:
    for j in i:
        if j == 0:
            print(0, end=' ')
        else: print(j-2, end=' ')
    print()