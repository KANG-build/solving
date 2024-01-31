import sys
input = sys.stdin.readline

a = int(input())
dot = []
for i in range(a):
    x, y = input().split()
    dot.append((int(x), int(y)))

for x, y in sorted(dot, key = lambda x : (x[1], x[0])):
    print(x, y)