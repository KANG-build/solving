import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()

p = 'IO' * n + 'I'
answer = 0

while True:
    if p in s:
        answer += 1
        index = s.index(p)
        s = s[index+2:]
    else:
        break

print(answer)