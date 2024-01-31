import sys
input = sys.stdin.readline

a = int(input())
for i in range(a):
    b = input()
    b = b.replace(')', '),')
    try:
        eval(b)
        print('YES')
    except:
        print('NO')