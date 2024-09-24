count = 0

def solution(board):
    global count
    
    n = len(board)
    m = len(board[0])
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                count += 1
                dfs(i-1, j, n, m, board)
                dfs(i+1, j, n, m, board)
                dfs(i, j+1, n, m, board)
                dfs(i, j-1, n, m, board)
                dfs(i-1, j-1, n, m, board)
                dfs(i+1, j+1, n, m, board)
                dfs(i-1, j+1, n, m, board)
                dfs(i+1, j-1, n, m, board)
                
    print(board)
    return n*m-count

def dfs(i, j, n, m, board):
    global count
    
    if i < 0 or i >= n or j < 0 or j >= m:
        return
    
    if board[i][j] == 0:
        count += 1
        board[i][j] = 2
    else:
        return