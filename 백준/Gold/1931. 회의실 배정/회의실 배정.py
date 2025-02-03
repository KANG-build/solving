import sys
input = sys.stdin.readline

# 회의실 배정 #
n = int(input())
input_data = []

for i in range(n):
    a, b = map(int, input().split())
    input_data.append((a, b))
    
meetings = sorted(input_data, key=lambda x : (x[1], x[0]))
room = 0
count = 0
for i in meetings:
    if room:
        if room[1] <= i[0]:
            count += 1
            room = i
    else:
        room = i
        count = 1
    
print(count)