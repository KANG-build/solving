def solution(keyinput, board):
    answer = [0, 0]
    for i in keyinput:
        if i == "up":
            answer[1] = min(answer[1] + 1, (board[1]//2))
        elif i == "down":
            answer[1] = max(answer[1] - 1, -(board[1]//2))
        elif i == "left":
            answer[0] = max(answer[0] - 1, -(board[0]//2))
        elif i == 'right':
            answer[0] = min(answer[0] + 1, (board[0]//2))
    return answer