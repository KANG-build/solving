import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    string = list(input()) # 문자열을 list화 하면 모든 문자가 다 분리된다.
    check = 0
    stack = []

    for i in string:
        if i == '(':
            stack.append('(')
        if i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else: 
                check = 1
                break
    if check == 1:
        print("NO")
    else:
        if stack:
            print("NO")
        else: print("YES")