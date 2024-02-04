import sys
input = sys.stdin.readline

num = input().strip()
for a in range(max(0, int(num)-100), int(num)):
    SUM = a + sum(int(i) for i in str(a))
    if SUM == int(num):
        print(a)
        break
else: print(0)