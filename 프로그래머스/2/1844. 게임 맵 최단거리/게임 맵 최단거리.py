from collections import deque

def solution(maps):
    queue = deque([])
    queue.append((0, 0))

    while queue:
        # 위치 선정
        x, y = queue.popleft()
        # 이 위치에서 가능한 범위
        for i in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            temp_x, temp_y = i[0], i[1]
            
            # 범위 확인하고 이상하거나 벽이면 넘김
            # (1) 이상하다
            if temp_x < 0 or temp_x >= len(maps[0]) or temp_y < 0 or temp_y >= len(maps):
                continue
            # (2) 벽이다 
            if maps[temp_y][temp_x] == 0:
                continue
            
            # bfs라서 이미 가본 곳이면 무조건 전꺼가 더 빠름
            if maps[temp_y][temp_x] == 1:
                maps[temp_y][temp_x] = maps[y][x] + 1
                queue.append((temp_x, temp_y))
                
            # 도달했다
            if temp_x == len(maps[0])-1 and temp_y == len(maps)-1:
                return maps[-1][-1]

    return -1