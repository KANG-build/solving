from collections import deque

def solution(n):
    direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    direct_i = 0
    
    mapping = [[0] * n for i in range(n)] 
    num = 1
    # 지금 있는 부분 기록을 안했네 
    x, y = 0, 0
    mapping[y][x] = 1
    while True:
        dx, dy = direct[direct_i]
        temp_x = x + dx
        temp_y = y + dy
        
        if num >= n**2:
            break
        # 범위를 넘어서거나 이미 방문한 위치면 회전한다
        if (temp_x < 0 or temp_y < 0 or temp_x >= n or temp_y >= n) or (mapping[temp_y][temp_x] != 0):
            direct_i = (direct_i+1)%4
        else:
            num += 1
            x = temp_x
            y = temp_y
            mapping[y][x] = num     
        
    return mapping