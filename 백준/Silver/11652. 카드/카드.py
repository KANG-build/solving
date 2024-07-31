import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
num = []

for i in range(N):
    a = int(input())
    num.append(a)

print(Counter(sorted(num)).most_common()[0][0])