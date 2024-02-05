import sys
input = sys.stdin.readline

a = int(input())
numList = []
for i in range(a):
    num = int(input())
    numList.append(num)

numList = sorted(numList)
i = round(a * 0.15 + 1e-9)
if a == 0:
    print(0)
elif i == 0:
    print(round(sum(numList)/len(numList) + 1e-9))
else: print(round(sum(numList[i:-i])/(len(numList)-(i*2)) + 1e-9))