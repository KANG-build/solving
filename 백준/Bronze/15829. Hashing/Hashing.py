import sys
input = sys.stdin.readline

alp = dict(zip([chr(i) for i in range(ord('a'), ord('z')+1)], [i for i in range(1, 27)]))

a = int(input())
s = input().strip()
SUM = 0

for idx, num in enumerate(s):
    SUM += alp[num] * 31**idx

print(SUM)