import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    input_data = list(map(int, input().split()))
    if len(input_data) == 1:
        array = []
        array.append(input_data)
    else:
        temp = []
        for i in range(len(input_data)):
            up = array[-1]
            if i == 0:
                temp.append(input_data[i]+up[0])
            elif i == len(input_data)-1:
                temp.append(input_data[i]+up[-1])
            else:
                temp.append(input_data[i]+max(up[i-1], up[i]))
        array.append(temp)
        
print(max(array[-1]))