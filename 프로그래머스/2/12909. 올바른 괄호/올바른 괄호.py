def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append('(')
        if i == ')':
            if stack and stack[-1] == '(':
                stack.pop(-1)
            else: 
                return False
    if stack:
        return False
    
    return True
                
        