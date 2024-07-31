import sys

a = int(input())
A = []
for i in range(a):
    num = sys.stdin.readline().rstrip()
    A.append(int(num))

for i in reversed(sorted(A)):
    print(i)