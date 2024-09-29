def check_win(board, player):
    win_conf = [
        ([board[0], board[1]], 2), ([board[0], board[2]], 1), ([board[1], board[2]], 0),
        ([board[3], board[4]], 5), ([board[3], board[5]], 4), ([board[4], board[5]], 3),
        ([board[6], board[7]], 8), ([board[6], board[8]], 7), ([board[7], board[8]], 6),
        ([board[0], board[3]], 6), ([board[0], board[6]], 3), ([board[3], board[6]], 0),
        ([board[1], board[4]], 7), ([board[1], board[7]], 4), ([board[4], board[7]], 1),
        ([board[2], board[5]], 8), ([board[2], board[8]], 5), ([board[5], board[8]], 2),
        ([board[0], board[4]], 8), ([board[0], board[8]], 4), ([board[4], board[8]], 0),
        ([board[2], board[4]], 6), ([board[2], board[6]], 4), ([board[4], board[6]], 2)
    ]
    
    for i in win_conf:
        if i[0] == [player, player]:
            return i[1]
    return

import sys
input = sys.stdin.readline

k = int(input())
for i in range(k):
    board = ''
    board += input().rstrip()
    board += input().rstrip()
    board += input().rstrip()
    player = input().rstrip()
    
    board = board[:check_win(board, player)] + player + board[check_win(board, player)+1:]
    
    print(f"Case {i+1}:")
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])
    