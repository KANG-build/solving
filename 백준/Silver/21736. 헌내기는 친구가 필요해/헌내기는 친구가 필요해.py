import sys
sys.setrecursionlimit(1000000)

def dfs(i, j):
    global answer
    
    if (j < 0) or (j >= m) or  (i < 0) or (i >= n):
        return
    
    if world[i][j] != 'X':
        if world[i][j] == 'P':
            answer += 1
        world[i][j] = 'X'
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    else:
        return
    
n, m = map(int, input().split())
world = []

for i in range(n):
    input_data = list(input())
    if 'I' in input_data:
        x, y = input_data.index('I'), i
    world.append(input_data)

answer = 0
dfs(y, x)
    
# 정답 출력
if answer == 0:
    print('TT')
else:
    print(answer)