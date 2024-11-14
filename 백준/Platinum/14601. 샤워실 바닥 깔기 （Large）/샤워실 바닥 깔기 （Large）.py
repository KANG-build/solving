# board : 이차원 리스트
# prow, pcol : 현재 분할이 위치한 좌표
# size : 현재 분할의 크기
# xrow, xcol : 배수구가 있는 부분의 좌표

# n : 현재의 사분면
# 현재 좌표를 제외한 나머지 사분면을 칠하는 함수

import sys
input = sys.stdin.readline

def fillCenterExcept(board,size,prow,pcol,n):
    global count
    mrow=prow+(size//2)
    mcol=pcol+(size//2) 
    if n == 1:
      board[mrow-1][mcol-1] = count
      board[mrow][mcol-1] = count
      board[mrow][mcol] = count
    elif n == 2:
      board[mrow-1][mcol] = count
      board[mrow][mcol-1] = count
      board[mrow][mcol] = count    
    elif n == 3:
      board[mrow-1][mcol] = count
      board[mrow-1][mcol-1] = count
      board[mrow][mcol] = count    
    elif n == 4:
      board[mrow-1][mcol] = count
      board[mrow-1][mcol-1] = count
      board[mrow][mcol-1] = count
    count += 1
    
#트로미노가 들어갈 좌표를 찾아서 분할 재귀하는 함수
def tromino(board,size,prow,pcol,xrow,xcol):
    if size==1:
        return
    
    else:
        mrow=prow+(size//2)
        mcol=pcol+(size//2)

        xrow1,xcol1=mrow-1,mcol 
        xrow2,xcol2=mrow-1,mcol-1
        xrow3,xcol3=mrow,mcol-1
        xrow4,xcol4=mrow,mcol

        if xrow<mrow and xcol>=mcol:
           fillCenterExcept(board,size,prow,pcol,1)
           xrow1, xcol1 = xrow, xcol
        elif xrow<mrow and xcol<mcol:
           fillCenterExcept(board,size,prow,pcol,2)
           xrow2, xcol2 = xrow, xcol
        elif xrow>=mrow and xcol<mcol:
           fillCenterExcept(board,size,prow,pcol,3)
           xrow3, xcol3 = xrow, xcol
        elif xrow>=mrow and xcol>=mcol:
           fillCenterExcept(board,size,prow,pcol,4)
           xrow4, xcol4 = xrow, xcol
            
        tromino(board,size//2,prow,mcol,xrow1,xcol1)
        tromino(board,size//2,prow,pcol,xrow2,xcol2)
        tromino(board,size//2,mrow,pcol,xrow3,xcol3)
        tromino(board,size//2,mrow,mcol,xrow4,xcol4)
        
#화면에 트로미노를 출력하는 함수
def printscr(board):                                          
    for row in board: 
        sys.stdout.write(" ".join(map(str, row)))
        sys.stdout.write("\n")
        

#입력
K=int(input())
x,y=list(map(int,input().split()))

#왼쪽 아래가 (1,1) 좌표이므로 변환이 이루어짐
full=2**K
px=full-y
py=x-1

#보드판 생성하기
board = [[0]*(2**K) for _ in range(2**K)]
board[px][py]=-1

#트로미노 타일링을 위한 카운터 초기화
count = 1

#트로미노 실행
tromino(board, 2**K, 0, 0, px, py)

#화면에 출력
printscr(board)