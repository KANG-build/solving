import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))
num = list(map(int, input().split()))
app = []

for i in range(len(num)-2):
    for j in range(i+1, len(num)-1):
        for k in range(j+1, len(num)):
            app.append(num[i] + num[j] + num[k] - M)
       
result = [i for i in app if i <= 0]
print(sorted(result)[-1] + M)