import sys
sys.setrecursionlimit(100000)

# 좌표로 체크
def visit(x1, y1, x2, y2):
    global count
    global answer
    
    if x2 == x1+2 or y2 == y1+2:  # 2*2일때
        # (r, c)면 count 출력 후 종료
        if x1 == c and y1 == r:
            answer = count
        elif c == (x1+1) and y1 == r:
            answer = count+1
        elif x1 == c and r == (y1+1):
            answer = count+2
        elif c == (x1+1) and r == (y1+1):
            answer = count+3  
        return
    
    else:
        # 왼쪽위 방문
        if x1 <= c < x1+(x2-x1)//2 and y1 <= r < y1+(y2-y1)//2: 
            visit(x1, y1, x1+(x2-x1)//2, y1+(y2-y1)//2)
        else:
            count += (x2-x1)//2 * (y2-y1)//2
    
        # 오른쪽위 방문
        if x1+(x2-x1)//2 <= c < x2 and y1 <= r < y1+(y2-y1)//2: 
            visit(x1+(x2-x1)//2, y1, x2, y1+(y2-y1)//2)
        else:
            count += (x2-x1)//2 * (y2-y1)//2
            
        # 왼쪽아래 방문
        if x1 <= c < x1+(x2-x1)//2 and y1+(y2-y1)//2 <= r < y2: 
            visit(x1, y1+(y2-y1)//2, x1+(x2-x1)//2, y2)
        else:
            count += (x2-x1)//2 * (y2-y1)//2
            
        # 오른쪽아래 방문
        if x1+(x2-x1)//2 <= c < x2 and y1+(y2-y1)//2 <= r < y2: 
            visit(x1+(x2-x1)//2, y1+(y2-y1)//2, x2, y2)
        else:
            count += (x2-x1)//2 * (y2-y1)//2

    return
    
n, r, c = map(int, input().split())
count = 0
answer = 0
visit(0, 0, 2**n, 2**n)
print(answer)