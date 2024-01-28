import sys
input = sys.stdin.readline

num = []
c = input().rstrip()
for i in range(int(c)):
    a = input().rstrip()
   
    if a == '0':
        num = num[:-1]
    else:
        num.append(int(a))
        
print(sum(num))