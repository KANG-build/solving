import heapq

input_data = input().rstrip()
stack = {0:[]}
count = 0

# 연산자는 스택에 넣고 피연산자는 출력한다
for i in input_data:
    if i in ['+', '-']:
        while stack[count]:
            print(heapq.heappop(stack[count])[1], end='')
        heapq.heappush(stack[count], (1, i))
    elif i in ['/', '*']:
        for j in stack[count]:
            if j[1] == '*' or j[1] == '/':
                while stack[count]:
                    if stack[count][0][0] == 1:
                        break
                    print(heapq.heappop(stack[count])[1], end='')
                break
        heapq.heappush(stack[count], (0, i))
    elif i == '(':
        count += 1
        stack[count] = []
    elif i == ')':
        print(''.join(j[1] for j in stack[count]), end='')
        del stack[count]
        count -= 1
        for j in stack[count]:
            if j[1] == '*' or j[1] == '/':
                while stack[count]:
                    if stack[count][0][0] == 1:
                        break
                    print(heapq.heappop(stack[count])[1], end='')
                break
    else: print(i, end='')

print(''.join(j[1] for j in stack[0]))