import sys
input = sys.stdin.readline


for a in range(1, 10001):
    for i in range(max(0, a-100), a):
        if i+sum(int(j) for j in str(i)) == a:
            break
    else: print(a)