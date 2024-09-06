import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = input().rstrip()
    n = int(input())
    line = input().rstrip()
    
    if len(line) <= 2:
        array = []
    else:
        array = deque(list(map(int, line[1:-1].split(','))))
    
    방향 = 0
    
    for op in p:
        if op == 'R':
            방향 = 1 if 방향 == 0 else 0
        elif op == 'D':
            if array:
                if 방향 == 0:
                    array.popleft()
                else: array.pop()
            else:
                print("error")
                break
    else:
        if 방향 == 1:
            array.reverse()
            
        print("[", end='')
        for i in range(len(array)):
            print(array[i], end='')
            if i != len(array)-1:
                print(",", end='')
        print("]")