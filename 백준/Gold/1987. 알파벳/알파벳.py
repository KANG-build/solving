import sys
input = sys.stdin.readline

def dfs(x, y, visit, count=0, alp=''):
    global board, n, m, answer
    # 범위 체크
    
    if 0 <= x < m and 0 <= y < n:
        pass
    else: 
        return
    
    # 방문했는지 체크
    if board[y][x] in alp:
        return
    
    # 방문을 체크
    if visit[y][x] == 0:
        visit[y][x] = 1
    count += 1
    alp += board[y][x]
    
    if answer < count:
        answer = count
    
    # dfs문
    dfs(x+1, y, visit, count, alp)
    dfs(x-1, y, visit, count, alp)
    dfs(x, y+1, visit, count, alp)
    dfs(x, y-1, visit, count, alp)
    
n, m = map(int, input().split())
board = []
answer = 0
visit = [[0] * m for j in range(n)]

for i in range(n):
    board.append(input().rstrip())

dfs(0, 0, visit)
print(answer)