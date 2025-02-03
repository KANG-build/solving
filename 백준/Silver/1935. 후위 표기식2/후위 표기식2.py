
# 후위 연산자2 #

# 알파벳에 나오면 저장된 수 중 -ord('A')-ord('B') 번째를 뽑는다.

n = int(input())
string = input()
number = []
for i in range(n):
    number.append(int(input()))
    
stack = []
for i in string:
    if i in ['*', '+', '-', '/']:
        b = stack.pop()
        a = stack.pop()
        
        if i == '*':
            stack.append(a*b)
        elif i == '+':
            stack.append(a+b)
        elif i == '-':
            stack.append(a-b)
        elif i == '/':
            stack.append(a/b)
        
    else:
        stack.append(number[-(ord('A')-ord(i))])
        
print(f"{stack[0]:.2f}")