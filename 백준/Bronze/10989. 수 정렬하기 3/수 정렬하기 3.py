import sys
input = sys.stdin.readline

numList = dict(zip([i for i in range(10001)], [0 for i in range(10001)]))
a = int(input())
for i in range(a):
    num = int(input())
    numList[num] += 1
    
for key in numList.keys():
    if numList[key] > 0:
        for i in range(numList[key]):
            print(key)