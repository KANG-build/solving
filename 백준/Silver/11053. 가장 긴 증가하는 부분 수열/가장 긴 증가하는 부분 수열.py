import bisect

n = int(input())
arr = list(map(int, input().split()))
answer = []

for i in arr:
    idx = bisect.bisect_left(answer, i)
    if idx == len(answer):
        answer.append(i)
    else:
        answer[idx] = i
        
print(len(answer))