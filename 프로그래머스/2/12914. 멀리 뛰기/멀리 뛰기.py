def solution(n):
    board = [0] * (n+1)
    board[0] = 1
    board[1] = 2
    
    for i in range(2, n):
        board[i] = board[i-2] + board[i-1]
    return board[n-1] % 1234567  
        