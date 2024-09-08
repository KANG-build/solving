import sys
from collections import deque

input = sys.stdin.readline

move = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
t = int(input())

for _ in range(t):
    l = int(input())
    world = [[0 for _ in range(l)] for _ in range(l)]
    
    answer = 0
    # x, y에서 a, b까지
    x, y = map(int, input().split())
    a, b = map(int, input().split())

    queue = deque([])
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        if x == a and y == b:
            print(world[a][b])
            break
        
        for i in move:
            dx, dy = x+i[0], y+i[1]
            
            if dx < 0 or dy < 0 or dx >= l or dy >= l:
                continue
            
            
            if world[dx][dy] != 0:
                continue

            
            world[dx][dy] = world[x][y] + 1
            queue.append((dx, dy))