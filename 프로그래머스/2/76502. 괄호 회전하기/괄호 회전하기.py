def check(string):
    stack = []
    for i in string:
        if i in ['[', '(', '{']: 
            stack.append(i)
        elif i == ']':
            if not stack or stack[-1] != '[':
                return False
            else:
                stack.pop()
        elif i == ')':
            if not stack or stack[-1] != '(':
                return False
            else:
                stack.pop()
        elif i == '}':
            if not stack or stack[-1] != '{':
                return False
            else:
                stack.pop()
    return stack == []

def solution(s):
    answer = 0
    string = s*2
    for i in range(len(s)):
        if check(string[i:i+len(s)]):
            answer += 1
    
    return answer