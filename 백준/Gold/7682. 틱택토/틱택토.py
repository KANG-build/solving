# 1차원 리스트에서 동일한 문자가 수직선이나 수평선, 대각선으로 나타나면
# 승리한 것으로 한다.
def check_win(board, player):
    win_conf = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]]
    ]
    return win_conf.count([player, player, player])

while True:
    board = input().strip()
    
    if board == 'end':
        break
    
    # 3연 개수 파악하기
    x = check_win(board, 'X')
    y = check_win(board, 'O')
    
    # 3연의 개수 2 이상, 불가능
    if (x == 1 and y == 1) or (x > 2 or y > 2):
        print('invalid')
        continue
    
    # 3연의 개수 1, X의 승일 경우 O가 하나 적다 / O의 승일 경우 동등하다
    elif 1 <= x <= 2 or 1 <= y <= 2:
        if 1 <= x <= 2:
            if board.count('X')-1 != board.count('O'):
                print('invalid')
                continue
        elif 1 <= y <= 2:
            if board.count('X') != board.count('O'):
                print('invalid')
                continue
    # 3연의 개수 0, X와 O 수 동일, .이 없다
    else:
        if '.' in board:
            print('invalid')
            continue
        if board.count('X') != board.count('O')+1:
            print('invalid')
            continue
            
    print('valid')
    