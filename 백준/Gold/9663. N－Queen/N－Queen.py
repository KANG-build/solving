class State:
    def __init__(self, board, depth=0):
        self.board = board  # 현재의 보드 상태

    # 높이 번째를 채워야 합니다
    def get_new_board(self, i):
        new_board = self.board[:] + [i]
        return State(new_board)
    
    # 자식 노드 확장 (휴리스틱 0일때만)
    def expand(self, n):
        result = []
        # 몇 n인지에 따라        
        for i in range(n):
            valid = True
            for idx, j in enumerate(self.board):
                if i == j or abs(j-i) == abs(len(self.board)-idx):
                    valid = False
                    break
                
            if valid:
                result.append(self.get_new_board(i))
        return result

import sys
input = sys.stdin.readline

n = int(input())
start = []

open_queue = []
open_queue.append(State(start))

count = 0

while open_queue:
    current = open_queue.pop()
    
    if len(current.board) == n:
        count += 1
    
    for state in current.expand(n):
        if len(current.board) <= n:
            open_queue.append(state)
    
# 정답 출력
print(count)
