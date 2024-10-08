import sys
import math
sys.setrecursionlimit(100000000)

# 중간점
def Mid(x1, y1, x2, y2):
	# 끝점으로 중간점 구하기
    return (x1+(x2-x1)//2, y1+(y2-y1)//2)
    
# 사분면 구분
def point(a, b, x, y): 
    if a <= x and b <= y:
        return 1
    elif  a > x and b <= y:
        return 2
    elif a <= x and b > y:
        return 3
    elif a > x and b > y:
        return 4
        
# 중간점이랑 사분면 구해서 어쩌구함
def tro(x1, y1, a, b, x2, y2):
    global count
        
    if x2 - x1 == 1 and y2 - y1 == 1:
        count += 1
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if board[j][i] == 0:  # 배수구가 아닌 곳에만 타일을 채움
                    board[j][i] = count
        return
    
    mid = Mid(x1, y1, x2, y2)
	# 칸 채움 (사분면 검사 함)
    count += 1
    if point(a, b, mid[0], mid[1]) == 1:
        board[mid[1]+1][mid[0]] = count
        board[mid[1]][mid[0]+1] = count
        board[mid[1]+1][mid[0]+1] = count
    elif point(a, b, mid[0], mid[1]) == 2:
        board[mid[1]][mid[0]] = count
        board[mid[1]+1][mid[0]] = count
        board[mid[1]+1][mid[0]+1] = count
    elif point(a, b, mid[0], mid[1]) == 3:
        board[mid[1]][mid[0]] = count
        board[mid[1]][mid[0]+1] = count
        board[mid[1]+1][mid[0]+1] = count
    elif point(a, b, mid[0], mid[1]) == 4:
        board[mid[1]][mid[0]] = count
        board[mid[1]+1][mid[0]] = count
        board[mid[1]][mid[0]+1] = count
               
    # 재귀적으로 각 사분면을 나누어 타일 배치
    tro(x1, y1, a if point(a, b, mid[0], mid[1]) == 1 else mid[0], 
        b if point(a, b, mid[0], mid[1]) == 1 else mid[1], mid[0], mid[1])
    
    tro(mid[0] + 1, y1, a if point(a, b, mid[0], mid[1]) == 2 else mid[0] + 1, 
        b if point(a, b, mid[0], mid[1]) == 2 else mid[1], x2, mid[1])

    tro(x1, mid[1] + 1, a if point(a, b, mid[0], mid[1]) == 3 else mid[0], 
        b if point(a, b, mid[0], mid[1]) == 3 else mid[1] + 1, mid[0], y2)

    tro(mid[0] + 1, mid[1] + 1, a if point(a, b, mid[0], mid[1]) == 4 else mid[0] + 1, 
        b if point(a, b, mid[0], mid[1]) == 4 else mid[1] + 1, x2, y2)

n = int(input())
board = [[0] * 2**n for _ in range(2**n)]
a, b = map(int, input().split())
a -= 1
b -= 1
board[b][a] = -1
count = 0
    
tro(0, 0, a, b, 2**n-1, 2**n-1)
for i in board[::-1]:
    for j in i:
        print(j, end=' ')
    print()