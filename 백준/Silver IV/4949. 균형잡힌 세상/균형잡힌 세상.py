import sys
input = sys.stdin.readline

while True:
    stack = []
    string = input().replace('\n', '')
    check = 0

    if string == '.':
        break

    for i in string:
        if i == '(':
            stack.append('(')
        if i == '[':
            stack.append('[')
        if i == ')':
            if stack and stack[-1] == '(':
                stack = stack[:-1]
            else: 
                check = 1
                break
        if i == ']':
            if stack and stack[-1] == '[':
                stack= stack[:-1]
            else:
                check = 1
                break

    if check == 1:
        print("no")
    else:
        if stack:
            print("no")
        else: print("yes")