import sys
input = sys.stdin.readline

# 트로미노 함수
# board : 이차원 리스트
# start_row, start_col : 현재 분할의 시작 좌표
# size : 현재 분할의 크기
# empty_row, empty_col : 비어 있는 곳의 좌표


def tromino(board, start_row, start_col, size, empty_row, empty_col):
    if size == 1:
        return
        
    middle_row = start_row + size // 2 # 중간 row
    middle_col = start_col + size // 2 # 중간 col

    # 1 : 왼쪽 위
    # 2 : 왼쪽 아래
    # 3 : 오른쪽 위
    # 4 : 오른쪽 아래
    quad1_row, quad1_col = middle_row - 1, middle_col - 1
    quad2_row, quad2_col = middle_row - 1, middle_col
    quad3_row, quad3_col = middle_row, middle_col - 1
    quad4_row, quad4_col = middle_row, middle_col

    # 왼쪽 위에 빈칸 존재
    if empty_row < middle_row and empty_col < middle_col:
        fill(board, middle_row, middle_col, 1)
        quad1_row, quad1_col = empty_row, empty_col
    # 왼쪽 아래에 빈칸 존재
    elif (empty_row < middle_row and empty_col >= middle_col):
        fill(board, middle_row, middle_col, 2)
        quad2_row, quad2_col = empty_row, empty_col
    # 오른쪽 위에 빈칸 존재
    elif (empty_row >= middle_row and empty_col < middle_col):
        fill(board, middle_row, middle_col, 3)
        quad3_row, quad3_col = empty_row, empty_col
    # 오른쪽 아래에 빈칸 존재
    elif (empty_row >= middle_row and empty_col >= middle_col):
        fill(board, middle_row, middle_col, 4)
        quad4_row, quad4_col = empty_row, empty_col

    # 재귀 호출 : 분할
    tromino(board, start_row, start_col, size // 2, quad1_row, quad1_col)
    tromino(board, start_row, middle_col, size // 2, quad2_row, quad2_col)
    tromino(board, middle_row, start_col, size // 2, quad3_row, quad3_col)
    tromino(board, middle_row, middle_col, size // 2, quad4_row, quad4_col)







# 각 카운트를 통해 어떤 트로미노가 들어갔는지 기록
# part : 현재의 사분면
def fill(board, mrow, mcol, part):
    global tromino_count
    tromino_count += 1
    if (part != 1):
        board[mrow - 1][mcol - 1] = tromino_count
    if (part != 2):
        board[mrow - 1][mcol] = tromino_count
    if (part != 3):
        board[mrow][mcol - 1] = tromino_count
    if (part != 4):
        board[mrow][mcol] = tromino_count

# 원점을 재정의 
def XYsetting(x, y):
    new_x = n - y
    new_y = x - 1
    return (new_x, new_y)

# 입력
k = int(input())
x, y = map(int, input().split())

# 왼쪽 아래가 (1,1)이므로 변환
n = 2 ** k
new_x, new_y = XYsetting(x, y)

# 보드판 생성
board = [[0] * (2 ** k) for _ in range(2 ** k)]
board[new_x][new_y] = -1

# 트로미노 함수 실행
tromino_count = 0
tromino(board, 0, 0, 2 ** k, new_x, new_y)

# 출력
for i in board:
    print(*i)