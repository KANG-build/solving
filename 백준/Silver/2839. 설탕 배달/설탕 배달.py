import sys
input = sys.stdin.readline

a = int(input())

# 일단 5로 벅벅 나눈다
if a%5 == 0:
    print(a//5)
else: 
    if (a%5)%3 == 0:
        print(a//5 + (a%5)//3)
    else:
        num = 0
        i = 0
        while num < a:
            i += 1
            num = (a%5) + 5*i
            if num > a:
                print(-1)
                break
            if num%3 == 0:
                print((a-num)//5 + num//3)
                break
        else: print(-1)