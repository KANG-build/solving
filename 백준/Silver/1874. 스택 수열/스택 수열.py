import sys
input = sys.stdin.readline

n = int(input())

goal = []
for i in range(n):
    goal.append(int(input()))

answer = ['+']
num = 1
stack = [1]

while goal:
# 맨 마지막꺼가 i번째인지 확인, 맨 마지막꺼보다 작으면 아웃
    if goal and not stack:
        answer.append('+')
        num += 1
        stack.append(num) 
    elif stack[-1] == goal[0]:
        answer.append('-')
        goal.pop(0)
        stack.pop()
    elif stack[-1] > goal[0]:
        print('NO')
        break
    elif goal:
        answer.append('+')
        num += 1
        stack.append(num)
else:
    for i in answer:
        print(i)