import heapq
import queue
import sys

# 상태를 나타내는 클래스, f(n) 값을 저장한다.
class State:
    def __init__(self, board, goal, depth=0):
        self.board = board  # 현재의 보드 상태
        self.depth = depth  # 깊이
        self.goal = goal  # 목표 상태
        
    # i1과 i2를 교환하여서 새로운 상태를 반환한다.
    def get_new_board(self, i1, i2, depth):
        new_board = self.board[:]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
        return State(new_board, self.goal, depth)
    
    # 자식 노드를 확장하여서 리스트에 저장하여서 반환한다.
    def expand(self, depth):
        result = []
        i = self.board.index(0)  # 숫자 0(빈칸)의 위치를 찾는다.
        if not i in [0, 3, 6]:  # LEFT 연산자
            result.append(self.get_new_board(i, i-1, depth))
        if not i in [0, 1, 2]:  # UP 연산자
            result.append(self.get_new_board(i, i-3, depth))
        if not i in [2, 5, 8]:  # RIGHT 연산자
            result.append(self.get_new_board(i, i+1, depth))
        if not i in [6, 7, 8]:  # DOWN 연산자
            result.append(self.get_new_board(i, i+3, depth))
        return result
    
    # f(n)을 계산하여 반환한다.
    def f(self):
        return self.h() + self.g()
    
    # 휴리스틱 함수 값인 h(n)을 계산하여 반환한다.
    # 현재 제 위치에 있지 않은 타일의 개수를 리스트 함축으로 계산한다.
    def h(self):
        score = 0
        for i in range(9):
            if self.board[i] != 0:  # 0(빈칸)은 제외
                # 현재 타일 위치 (i)와 목표 위치 (goal.index(self.board[i]))의 좌표 계산
                current_row, current_col = divmod(i, 3)
                goal_row, goal_col = divmod(self.goal.index(self.board[i]), 3)
                # 맨해튼 거리 계산 (행 차이 + 열 차이)
                score += abs(current_row - goal_row) + abs(current_col - goal_col)
        return score
    
    # 시작 노드로부터의 깊이를 반환한다.
    def g(self):
        return self.depth
    
    def __eq__(self, other):  # 이것을 정의해야 in 연산자가 올바르게 계산한다.
        return self.board == other.board
    
    def __ne__(self, other):  # 이것을 정의해야 in 연산자가 올바르게 계산한다
        return self.board != other.board
    
    # 상태와 상태를 비교하기 위하여 less than 연산자를 정의한다.
    def __lt__(self, other):
        return self.f() < other.f()
    
    def __gt__(self, other):
        return self.f() > other.f()
    
    # 객체를 출력할 때 사용한다.
    def __str__(self):
        return f"f(n)={self.f()} h(n)={self.h()} g(n)={self.g()}\n"+\
        str(self.board[:3])+"\n"+\
        str(self.board[3:6])+"\n"+\
        str(self.board[6:])+"\n"

    def __hash__(self):  # hash 메서드를 추가해야 set에서 사용할 수 있다.
        return hash(tuple(self.board))
    
    
# 목표 상태
goal = [1, 2, 3,
       4, 5, 6,
       7, 8, 0]


t = int(input())

for _ in range(t):
    # 초기 상태
    puzzle = []
    blank = input()
    for i in range(3):
        input_data = input().replace('#', '0')
        puzzle += [int(i) for i in input_data]

    possible = True

    inv_count = 0
    for i in range(8):
        for j in range(i+1, 9):
            if puzzle[i] != 0 and puzzle[j] != 0 and puzzle[i] > puzzle[j]:
                inv_count += 1
                
    if inv_count % 2 != 0:
        possible = False
        print('impossible')

    # open 리스트는 우선순위 큐로 생성한다.
    open_queue = queue.PriorityQueue()
    open_queue.put(State(puzzle, goal))
    open_set = {tuple(puzzle):0}  # 중복 확인을 위한 집합

    depth = 0

    while possible and open_queue:
        current = open_queue.get()

        if current.board == goal:
            print(current.depth)
            break

        depth = current.depth+1
        for state in current.expand(depth):
            if tuple(state.board) not in open_set:
                open_queue.put(state)
                open_set[tuple(state.board)] = current.g()  # 새로운 상태 추가
            elif state.g() < open_set[tuple(state.board)]:
                open_queue.put(state)
                open_set[tuple(state.board)] = current.g()  # 갱신