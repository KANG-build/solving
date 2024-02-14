def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append('(')
        if i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else: 
                return False
            
    return len(stack) == 0

                
        